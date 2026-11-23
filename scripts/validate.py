#!/usr/bin/env python3
"""Lightweight repo checks, run locally or in CI. Exits non-zero on any failure."""
import json, re, struct, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
errors = []

def fail(msg): errors.append(msg)

def load_json(rel):
    try:
        return json.loads((root / rel).read_text())
    except Exception as e:
        fail(f"{rel}: invalid JSON ({e})")
        return {}

plugin = load_json(".claude-plugin/plugin.json")
market = load_json(".claude-plugin/marketplace.json")

for key in ("name", "version", "description", "author", "license", "icon"):
    if not plugin.get(key):
        fail(f"plugin.json: missing '{key}'")
if not re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", "")):
    fail("plugin.json: version must be semver x.y.z")
if not market.get("plugins"):
    fail("marketplace.json: no plugins listed")
elif market["plugins"][0].get("name") != plugin.get("name"):
    fail("marketplace.json plugin name does not match plugin.json")

# Icon: square PNG, 512-2048 px, under 2 MB
icon = root / plugin.get("icon", "")
if icon.is_file():
    data = icon.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        fail("icon is not a PNG")
    else:
        w, h = struct.unpack(">II", data[16:24])
        if w != h or not 512 <= w <= 2048:
            fail(f"icon must be square, 512-2048 px (got {w}x{h})")
    if len(data) > 2 * 1024 * 1024:
        fail("icon larger than 2 MB")
else:
    fail("plugin.json: icon file not found")

# SKILL.md frontmatter and references
skill_dir = root / "skills" / "test-framework-architect"
skill = (skill_dir / "SKILL.md").read_text()
m = re.match(r"---\n(.*?)\n---\n", skill, re.S)
if not m:
    fail("SKILL.md: missing frontmatter")
else:
    fm = m.group(1)
    for key in ("name", "description"):
        if not re.search(rf"^{key}:\s*\S", fm, re.M):
            fail(f"SKILL.md: frontmatter missing '{key}'")

for ref in sorted(set(re.findall(r"references/[\w.\-]+", skill))):
    if not (skill_dir / ref).is_file():
        fail(f"SKILL.md references missing file: {ref}")

for step in ("### Step 0b:", "### Step 0c:"):
    if step not in skill:
        fail(f"SKILL.md: missing '{step}' section")
if "Step 0c" not in (skill_dir / "references" / "phases.md").read_text():
    fail("phases.md: Phase 5 must reference Step 0c")

questions = (skill_dir / "references" / "questions.md").read_text()
if "Q1 or Q2" not in questions or "REVISITABLE" not in questions.split("**Q2.")[0]:
    fail("questions.md: Q1 needs a default and the unsure follow-up must cover Q1 or Q2")

# Every phase handoff line must be present in the phase spec
phases = (skill_dir / "references" / "phases.md").read_text()
if "Ready to move to Phase N+1? Or would you like to adjust anything?" not in phases:
    fail("phases.md: handoff line missing")
for n in range(1, 9):
    if not re.search(rf"^## Phase {n}:", phases, re.M):
        fail(f"phases.md: missing '## Phase {n}:' heading")

# CI template must parse and keep always-upload behaviour
ci = skill_dir / "references" / "ci-github-actions.yml"
if "if: always()" not in ci.read_text():
    fail("ci-github-actions.yml: artifact upload must use 'if: always()'")
try:
    import yaml
    for f in [ci, *sorted((root / ".github" / "workflows").glob("*.yml"))]:
        yaml.safe_load(f.read_text())
except ImportError:
    print("note: PyYAML not installed, skipping YAML parse")
except Exception as e:
    fail(f"YAML parse error: {e}")

if errors:
    print("FAILED:")
    for e in errors: print(f"  - {e}")
    sys.exit(1)
print("OK: all repo checks passed")

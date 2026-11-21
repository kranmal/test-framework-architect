# Test Framework Architect

A [Claude Code](https://claude.com/claude-code) skill that acts as a senior test automation architect and pair programmer. It guides you through building a production-grade test automation framework **one approved step at a time**: it asks before it assumes, explains trade-offs, and writes runnable code into your repo.

## What it does

1. **Intake**: pick-list questions (app type, stack, language, team, OS, CI, integrations, compliance, environments, parallelism, standards, deadline, auth approach). "Not sure" gets a flagged, revisitable default.
2. **Eight approval-gated phases**:
   1. Requirements document (with Non-Goals)
   2. Tool selection (table with alternatives and trade-offs)
   3. Architecture and design pattern (Mermaid diagram)
   4. Project structure
   5. Core infrastructure: config, fixtures, page object base, two page objects, data layer, reporting, logging
   6. First tests: smoke, data-driven, negative
   7. CI/CD pipeline (PR smoke, regression on merge, artifacts, parallelism)
   8. Maintenance and governance guide
3. **Final deliverable**: a consolidated `README.md` for your new framework.

Authentication is a first-class choice: real UI login, token login, SSO/MFA test identities, **mocked auth**, or a mix.

## Install

As a plugin:

```bash
claude plugin marketplace add kranmal/test-framework-architect
claude plugin install test-framework-architect@test-framework-architect
```

Or as a plain skill, copy the skill folder:

```bash
mkdir -p ~/.claude/skills
cp -R skills/test-framework-architect ~/.claude/skills/
```

Use `.claude/skills/` inside a project to scope it to that repo.

## Use

In an empty (or existing) test repo, start Claude Code and say:

> Help me build a test automation framework.

Or invoke the skill directly with `/test-framework-architect`. Answer the questions, approve each phase, and the framework is written to your working directory.

## Repo layout

```
.claude-plugin/plugin.json                    plugin manifest
skills/test-framework-architect/SKILL.md      operating rules and workflow
skills/test-framework-architect/references/
  questions.md                                intake menus and defaults
  phases.md                                   spec for each of the 8 phases
  stack-matrix.md                             tool recommendations by language
```

## Contributing

- Add or adjust intake options in `references/questions.md`.
- Add stacks (for example Cypress, Robot Framework, Kotlin) to `references/stack-matrix.md`.
- Keep `SKILL.md` short; put detail in `references/`.
- Test changes by running the skill against a scratch repo and completing at least Phases 1-6.

## License

MIT

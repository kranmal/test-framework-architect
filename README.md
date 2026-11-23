# Test Framework Architect

A [Claude Code](https://claude.com/claude-code) skill that acts as a senior test automation architect and pair programmer. It guides you through building a production-grade test automation framework **one approved step at a time**: it asks before it assumes, explains trade-offs, and writes runnable code into your repo.

## What it does

1. **Intake**: pick-list questions (app type, stack, language, team, OS, CI, integrations, compliance, environments, parallelism, standards, deadline, auth approach). "Not sure" gets a flagged, revisitable default.
   After the questions it shows a short plain-English note on what your choices let you do and what they rule out.
   If you pick GitHub Actions, it then asks which repository to use (the current folder's repo, one from `gh repo list`, a new private repo, or decide later). It only reads until you approve each action.
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

## What a session looks like

Illustrative, abridged flow (your answers drive the choices; exact wording varies):

```text
You:     Help me build a test automation framework.

Claude:  Four grouped pick-lists (app and scope, team and environment,
         integrations and constraints, standards and authentication).
         You choose from the options or pick "Other". "Not sure" applies
         a default and flags it REVISITABLE.

Claude:  ## Intake summary
         | Decision | Answer            |
         |----------|-------------------|
         | App      | REST API only     |
         | Language | TypeScript        |
         | CI       | GitHub Actions    |
         ...

Claude:  ## Phase 1: Requirements document
         (one page, with Non-Goals and every REVISITABLE default)
         Ready to move to Phase 2? Or would you like to adjust anything?

You:     Approve.

         ...Phases 2-5 repeat the pattern. Phase 5 is confirmed sub-step by
         sub-step. In Phase 6 it writes three tests, runs them, then adds a
         deliberate failing test to prove screenshots, traces, JUnit and the
         HTML report appear on failure, and deletes it again.
```

The framework is written into your working directory as you approve each phase, with decisions tracked in `docs/decisions.md`.

## Repo layout

```
.claude-plugin/plugin.json                    plugin manifest
.claude-plugin/marketplace.json               marketplace entry for installs
.claude-plugin/icon.png                       plugin icon
skills/test-framework-architect/SKILL.md      operating rules and workflow
skills/test-framework-architect/references/
  questions.md                                intake menus and defaults
  guidance.md                                 plain-English notes on what each choice allows
  phases.md                                   spec for each of the 8 phases
  stack-matrix.md                             tool recommendations by language
  ci-github-actions.yml                       verified CI template
scripts/validate.py                           repo checks (also run in CI)
.github/workflows/validate.yml                CI for this repo
```

## Contributing

- Add or adjust intake options in `references/questions.md`.
- Add stacks to `references/stack-matrix.md`.
- Run `python3 scripts/validate.py` (and `claude plugin validate .`) before opening a PR; CI runs the same checks.
- Keep `SKILL.md` short; put detail in `references/`.
- Test changes by running the skill against a scratch repo and completing at least Phases 1-6.

## License

MIT

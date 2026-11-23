# Re-scan mode: do our tests cover what changed?

Use this when a framework already exists (look for `docs/decisions.md`, `docs/coverage-map.md` or the test folders) and the user wants to know whether recent changes to the application are covered. It never needs the 8 phases again.

Everything is read-only until the user approves creating tests. Speak in plain English, no jargon.

## 1. Find the starting point
- If `docs/coverage-map.md` exists, use the "Last scanned at" commit or date recorded in it.
- Otherwise ask one question: scan since a date, since a branch or tag, or since the last release. If the folder is not a git repo, ask the user to describe what changed, or point at the changed files.
- Say what range you are scanning before you start.

## 2. List what changed
- Read-only git only: `git log`, `git diff --name-status`, `git diff` on the files that matter. Ignore changes that cannot alter behaviour (comments, formatting, docs, lock files) and say you ignored them.
- Group the remaining changes into user-visible behaviours in plain words, for example "customers can now reset their password" or "the transfer API rejects amounts over the limit". One line each, naming the files behind it.

## 3. Check what is already covered
For each behaviour, look in the existing tests (feature files, specs, API tests, page objects) for a test that would fail if that behaviour broke. Judge by what the test checks, not by its name alone.
- **Covered**: name the test and what it checks.
- **Partly covered**: say what is checked and what is missing (for example the happy path but not the error).
- **Not covered**: nothing would fail if it broke.
- **Cannot tell**: say why (for example behaviour depends on data or a service you cannot see) and ask.
Never mark something covered without naming the test that covers it.

## 4. Report and advise
Show a table: change, status, why it matters, suggested test. Order by risk: money, login, data loss and security first. Then a short plain-English summary: how many are covered, partly covered, not covered, and which gaps matter most. If everything is covered, say so and stop.

## 5. Offer the choice
Ask with AskUserQuestion: create tests for all the gaps / let me pick which / not now (record the findings only). Never create tests without a yes.

## 6. Create the tests, one at a time
For each approved gap, follow the framework's existing conventions (its page objects, data layer, naming, language) and the Phase 6 style:
- show the test, run it, show the real pass or fail output;
- if it fails because the app is wrong, report it as a possible bug rather than weakening the test;
- ask "Does this match how you'd actually test this flow? What's missing?" before the next one.
Ask before downloading anything and before touching existing tests. Do not commit or push without an explicit yes.

## 7. Record the result
Write or update `docs/coverage-map.md`: one line per behaviour (behaviour, status, test name, date), and a "Last scanned at" line with the commit hash and date. Add a line to `docs/decisions.md` for any new test conventions. Finish by telling the user what is now covered and what they chose to leave open.

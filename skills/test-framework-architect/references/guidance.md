# What your choices mean (plain-English guidance)

Used right after intake. For each answer the user gave, say in plain words what that choice lets them do, what it rules out, and what they should watch for. Only include entries for options they actually chose. No jargon, no tool names unless the user already used them. Keep each line to one or two sentences.

Present it as a short list headed "What your choices mean", then go straight on to the contradiction check. Do not ask extra questions here unless an entry reveals a conflict between two answers; then name the conflict and ask the user to resolve it. If an answer was "not sure", say which default was applied and that it can be changed later.

## Application type (Q1)
- **Web**: you can test what people see and do in a browser (pages, forms, logging in). You cannot test things that only exist on the server unless you also choose API.
- **API**: you can test the server directly, quickly and without a browser. You cannot check how pages look or whether buttons work.
- **Mobile**: you can test a phone app, but it needs emulators or real devices and a signed build. It is a separate, later package from web and API, and adds time and cost.
- **Desktop**: you can test an installed program. It needs a matching operating system, and on CI usually a Windows machine with a screen. It is also a separate, later package.
- **More than web and API together**: do web and API first, then add the rest. Doing everything at once is the most common way these projects stall.
- **Not sure**: web plus API is assumed, and a short question follows to check what the target really is.

## What is being tested (Q2)
- **Single-page app (React, Vue, Angular)**: you can test it in a real browser. You cannot rely on page loads to tell you when something is ready, so tests wait for things to appear.
- **Server-rendered website**: you can test it in a browser, and pages are usually simpler to wait for.
- **REST or GraphQL API**: you can test requests and responses with no browser. You cannot tell from these tests whether the screen looks right.
- **Native app or desktop program**: see the Mobile and Desktop notes above.
- **Unsure whether there is a screen, an API, or both**: you will be asked one plain question, and the real repository is checked later to confirm.

## How much testing (Q3)
- **Under 100 tests**: a simple structure is enough, and it is fast to run on every change.
- **Hundreds to thousands**: you can run them, but only by splitting the work across machines and keeping tests independent. Plan that now, not later.

## New or migrating (Q4)
- **New**: you start clean, with nothing to match.
- **Migrating manual tests**: you can import them as test outlines, but they will still need writing and checking by a person. They will not run on their own.
- **Existing automation in the repo**: say so. You can extend it or start fresh, but mixing two frameworks in one place causes confusion.

## Language and tool (Q5)
- **TypeScript**: one language covers web and API tests, with the most complete tooling. You cannot reuse a Java or Python team's existing helpers.
- **Python, Java, C#**: fine for both. You give up some of the newest browser features in some tools and may need extra setup.
- **Not sure**: TypeScript is used, and it can be changed before any code is written.

## Team (Q6)
- **New to automation or mostly manual testers**: the framework stays simple, with fewer layers and more comments. You cannot expect to handle advanced structure without help.
- **Dedicated test engineers**: more structure is fine, but it needs the team to keep it consistent.

## Computer and CI (Q7, Q8)
- **Windows, Mac or Linux**: all work. A mixed team means scripts must avoid system-specific commands.
- **GitHub Actions, GitLab CI and similar**: tests can run automatically on every change. You cannot prove the pipeline works until it is pushed to a real repository and run there.
- **No CI yet**: tests run only on someone's machine until you add one. That is fine to start with, but results are not shared.

## Integrations (Q9)
- **None**: nothing is linked to Jira, TestRail or chat. Test results are saved as standard files, so you can link them later without redoing work.
- **Jira, TestRail, Slack or similar**: you can send results there. Each one needs access you set up, and keys must never be put in code.

## Compliance and safety (Q10)
- **Synthetic data only**: tests never use real customer details. You cannot test with a copy of live data.
- **No cloud services or a secrets vault**: some online testing services are ruled out, and passwords must come from your approved store.
- **None special**: passwords and keys still always come from environment variables, never from files in the repository.

## Environments (Q11)
- **One environment**: tests run in one place only. You cannot check how a release behaves in staging or live.
- **More than one**: you can run the same tests in each. Never run anything that changes or deletes data against the live system; use read-only checks there.
- **A static page**: there is nothing to deploy, so no separate environments are needed.

## Parallel runs (Q12)
- **No parallel runs**: simplest, but slowest as the suite grows.
- **A few workers or splitting across machines**: much faster, but every test must be able to run on its own, with its own data, in any order.
- **A cloud testing service**: lets you test on many browsers and devices, but costs money and needs an account and keys you create.

## Standards (Q13)
- **None**: you get sensible defaults.
- **Plain-English test scenarios required (Gherkin or BDD)**: non-coders can read the tests, but there is an extra layer to keep up to date, so changes take longer.
- **A mandated tool or style guide**: you will be asked to name it or share the file, and your choice limits what else can be used.

## Delivery time (Q14)
- **One week**: only a small first set is realistic: setup, a basic structure and one or two checks. You cannot also expect pipeline, reports and a full maintenance guide, so you will be asked which to keep.
- **Two weeks**: a first set of checks running automatically is realistic.
- **Four weeks or more**: the full framework is realistic.

## Logging in (Q15)
- **Real login once, then reuse**: fast and realistic. If login is broken, every test fails.
- **Token or direct login**: the fastest, but it skips the login screen, so it proves nothing about that screen.
- **Single sign-on, codes or multi-step login**: needs a test account set up by whoever owns the login system. You cannot automate against a real person's account.
- **Fake (mocked) login**: no real passwords, and it is quick. It does not prove the real login works, so keep at least one test with the real thing.
- **Mix (recommended)**: one real login test, and quick logins for everything else.

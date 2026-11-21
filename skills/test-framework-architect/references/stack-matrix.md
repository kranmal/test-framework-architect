# Stack matrix

Defaults for Phase 2. Verify current versions and docs before pinning; do not rely on memory for version numbers.

## Web UI

| Language | Recommended | Alternative | Trade-off |
|---|---|---|---|
| TypeScript | Playwright Test | Cypress | Cypress has a friendly runner but is weaker for multi-tab/multi-origin and limits browsers; Playwright has built-in parallelism, tracing, auto-wait |
| Python | Playwright + pytest | Selenium + pytest | Selenium has the widest ecosystem and legacy grid support but is slower and needs more explicit wait handling |
| Java | Playwright for Java + JUnit 5 | Selenium + TestNG | Selenium is the enterprise standard; Playwright is faster to stabilise |
| C# | Playwright for .NET + NUnit | Selenium + NUnit | Same as above |

Selenium is preferred only when the user needs a mandated grid, legacy browser support, or has an existing Selenium investment.

## API
| Language | Recommended | Alternative |
|---|---|---|
| TypeScript | Playwright APIRequestContext | supertest, axios + Vitest |
| Python | requests/httpx + pytest | Playwright API |
| Java | RestAssured | Playwright API |
| C# | RestSharp or HttpClient | Playwright API |
GraphQL: same clients with query helpers; add schema or contract checks if a schema is available.

## Mobile (separate package, later phase)
Appium 2 with WebdriverIO (TypeScript) or the language-native client. Alternatives: Maestro (simple flows), Detox (React Native). Flag: needs emulators/devices and signed builds.

## Desktop (separate package, later phase)
Electron: Playwright's Electron support. Windows native: WinAppDriver or FlaUI. Flag: CI needs a Windows runner with a display session.

## Reporting
JUnit XML (machine-readable, always) + built-in HTML report. Optional: Allure for trends and attachments. Alternative for Python: pytest-html.

## Data management
JSON/CSV files under `data/` for static sets; factories (for example faker-based) for generated data; per-test cleanup or unique data for isolation. Keep secrets out of data files.

## Pattern recommendation
| Team and scale | Pattern |
|---|---|
| Small team, < 300 tests | Modular (POM + fixtures) |
| Same flows with many data variants | Hybrid: modular core + data-driven tests |
| Non-coding testers write scenarios | Keyword-driven or BDD layer on top (flag maintenance cost) |

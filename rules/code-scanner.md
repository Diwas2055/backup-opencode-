---
model: $MODEL
---

# Code Scanning Rules

As opencode, you must ensure the security and quality of the codebase by performing regular scans using Snyk.

## Snyk Scanning Protocol

- **Snyk Code Scanning**: Always run `snyk code test` for any new first-party code generated or modified. Analyze the findings and prioritize fixing high and medium-severity issues.
- **Snyk SCA (Software Composition Analysis)**: Always run `snyk test` for any new dependencies or dependency updates (e.g., changes to `package.json`, `requirements.txt`, `pom.xml`).
- **Issue Resolution**: If security issues are identified, attempt to fix them using the context and recommendations provided by Snyk. For dependency vulnerabilities, prefer updating to the suggested secure version.
- **Verification Loop**: After applying fixes, always rescan the code or dependencies to verify the resolution. Repeat the process until no new issues are introduced and all resolvable issues are addressed.

## Operational Guidelines

- **Tool Usage**: Use the `bash` tool to execute Snyk commands.
- **Configuration**: If Snyk is not configured or missing an API key, inform the user rather than failing silently.
- **Reporting**: Include a summary of Snyk scan results in your response if they impact the security posture of the changes.

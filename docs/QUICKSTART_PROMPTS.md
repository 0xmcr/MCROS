# Quick-start prompts

Use these as user prompts in Antigravity. Adapt the scope and constraints.

## A. Start a new product
"Use the MCROS V3 workflow. First inspect this workspace and identify whether it is empty or an existing project. Ask only for decisions that materially affect the outcome. Research current technical options and market claims where needed, create/update the PRD and architecture docs, then implement the highest-priority approved scope. Run relevant tests and report evidence, limitations, and next steps. Do not deploy or incur costs without my approval."

## B. Improve an existing application
"Inspect the existing codebase before changing anything. Map the architecture, identify the highest-impact defects and risks, and propose a small implementation plan. Then implement the agreed improvements without unrelated rewrites. Run targeted tests and regression checks. Summarize files changed and actual verification results."

## C. Conduct a security audit
"Run the authorized defensive security-audit workflow against this workspace only. Inspect code, dependencies, configuration, authentication, authorization, API boundaries, data handling, and deployment files. Do not attack external systems or perform destructive tests. Report evidence, severity, impact, remediation, and retest status. Do not claim absence of vulnerabilities beyond the checks performed."

## D. Conduct market research
"Run the market-research workflow. Use current, credible sources and distinguish verified data, estimates, hypotheses, and unknowns. Compare competitors, customer needs, pricing, market positioning, and product gaps. Cite primary sources and disclose limitations. Do not invent market size or demand."

## E. Prepare a release
"Run the release-readiness workflow. Verify build, tests, dependencies, secrets hygiene, migrations, security findings, observability, backups, rollback, and documentation. Do not deploy. Produce a release decision with blockers and evidence."

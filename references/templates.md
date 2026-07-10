# Templates

Use these lightweight templates to keep the workflow auditable across agents.

## Project Status

```markdown
# Project Status

last updated:
target:
current stage:
state vocabulary:
current gate:
next gate:
working title:
active files:

## Boundary

This workspace only covers:
Do not mix with:

## Current decision

## Gate status

- completed gates:
- current incomplete gate:
- stale or invalidated artifacts:
- manual confirmations:

## Verified requirements

## Evidence status

## Next actions

## Stop conditions
```

## Topic Decision Record

```markdown
# Topic Decision Record

date:
topic:
target:
decision owner:
decision status: exploratory / provisional / proceed / stop

## Research problem

## Field map and gap evidence

| search source | query | date | scope/language | included/excluded | saturation result |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Gap chain

| gap-chain link | claim | source IDs/pages | what the evidence establishes | remaining uncertainty |
| --- | --- | --- | --- | --- |
| field finding |  |  |  |  |
| limitation or tension |  |  |  |  |
| consequence |  |  |  |  |
| research question |  |  |  |  |
| contribution |  |  |  |  |

## Narrow corpus

## Research questions

## Central thesis

## Contribution and counterargument

primary contribution:
secondary contribution, if any:
strongest counterargument:

## Relevance pathway

finding -> reader/beneficiary -> decision, interpretation, or practice -> demonstrated impact or potential use:

## Why this target fits

## What this paper will not claim

## Similarity or overlap risks

## Eight-Test Score and Decision

| criterion | score (0-2) | evidence or reason |
| --- | --- | --- |
| reader fit |  |  |
| problem strength |  |  |
| gap evidence |  |  |
| question strength |  |  |
| evidence feasibility |  |  |
| method fit |  |  |
| contribution clarity |  |  |
| relevance integrity |  |  |

total:
hard thresholds: gap evidence = 2; reader fit/problem/question/feasibility/method/contribution/relevance integrity >= 1:
decision date:
decision and next gate:
```

## Project State Snapshot

```markdown
# Project State Snapshot

date:
workspace:
track:
current state:
current gate:
next gate:
latest authoritative draft:
latest audit/checklist:
source/evidence files:
submitted or frozen files:

## What is safe to edit

## What must not be changed

## Conflicts or uncertainties

## Resume instruction

Continue from:
Do not repeat unless:
```

## Handoff Packet

Use this at the end of a long turn, before switching agents, or after context compaction. Keep it short enough for a future agent to trust quickly.

```markdown
# Handoff Packet

date:
workspace:
track:
target:
current state:
current gate:
next gate:
latest authoritative draft:
latest status/checklist:
source/evidence files:
review/revision files:
frozen or submitted files:

## Completed this turn

## Still unresolved

## Manual confirmations needed

## Do not do

## Resume from here
```

## Prospectus or Chapter Plan

```markdown
# Prospectus or Chapter Plan

date:
working title:
dissertation/article function:

## Summary of argument

## Justification

## Research questions

## Method and corpus

## Outline or table of contents

## Bibliography/source readiness

## Limits and stop conditions
```

## Source Matrix

```tsv
source_id	source_type	original_title	english_title	author_or_institution	year	source_language	evidence_available	planned_section	claim_supported	status	notes
S001
```

## Evidence Log

```tsv
claim_id	claim_text	claim_type	evidence_source	source_location_or_page	manuscript_location	risk_level	verification_status	notes
C001
```

## Source Synthesis Map

```tsv
group_id	relationship_type	sources	shared_issue	tension_or_outlier	gap_or_contribution_use	use_in_manuscript	notes
G001	agreement/disagreement/method/corpus/outlier
```

## Page Locator Audit

```tsv
source_id	short_citation	claim_or_section	printed_page	file_page	page_status	verification_method	adjacent_pages_checked	html_or_publisher_checked	notes
S001		Introduction	91	5	verified	rendered page	yes	n/a
```

## Footnote Audit

```tsv
note_id	manuscript_location	sources_in_note	style_ok	page_locators_ok	action_needed	notes
1	Introduction paragraph 2	2	yes	yes	none
```

## Claim-Evidence Outline

```markdown
# Claim-Evidence Outline

## Thesis

## Problem, gap, contribution, and relevance pathway

## Section 1
- section claim:
- evidence:
- interpretation/warrant/stake:
- pages/snapshots:
- risk:
- word target:

## Section 2
```

## Reverse Outline Audit

```tsv
location	paragraph_function	thesis_connection	evidence_used	interpretation_or_stake	action	notes
Introduction paragraph 1	problem statement	yes	none yet	field consequence	keep/add evidence
```

## Reading Note

```markdown
# Reading Note

source_id:
citation:
full text status:

## Useful claims

## Key terms

## Pages to cite

## Limits

## How it fits the manuscript
```

## Reviewer Comment Tracker

```tsv
comment_id	reviewer	role	comment	severity	action	location	status	notes
R001
```

## Response to Reviewers Table

```tsv
comment_id	reviewer_comment	action_taken	location_in_revision	response_text	status
R001
```

## Final Readiness Checklist

```markdown
# Final Readiness Checklist

- [ ] Target requirements verified from official/saved source.
- [ ] Scope matches evidence.
- [ ] Current Topic Decision Record includes a search ledger, gap-chain ledger, eight-test score, and hard-threshold result.
- [ ] Problem, gap, contribution, counterargument, and relevance pathway match the completed manuscript.
- [ ] Demonstrated impact is separated from proposed or potential use.
- [ ] Source matrix updated.
- [ ] Evidence log updated.
- [ ] All paginated claims have exact pages.
- [ ] Web sources have URL and access date.
- [ ] Chinese titles/translations checked.
- [ ] Citation/reference correspondence checked.
- [ ] Similarity-risk wording checked.
- [ ] Writing-quality/style gate completed when drafting, polishing, or finalizing.
- [ ] Insight/style audit records the strongest evidence-backed interpretation and remaining limitation.
- [ ] Reviewer pass completed.
- [ ] Contribution/relevance report gives a verdict against the Topic Decision Record.
- [ ] Required revisions completed.
- [ ] Anonymous file scrubbed if required.
- [ ] DOCX/PDF layout checked if required.
- [ ] Comments/tracked changes removed.
- [ ] Metadata checked.
- [ ] Declarations truthful and complete.
- [ ] Submission record prepared.
- [ ] Manual confirmations listed for the author.
```

## Dissertation DOCX Checklist

```markdown
# Dissertation DOCX Checklist

- [ ] DOCX is the final deliverable unless PDF was explicitly requested.
- [ ] Footnote references and footnote definitions match.
- [ ] Footnote style is consistent across the whole dissertation.
- [ ] No stacked note numbers where a single note callout is expected.
- [ ] Multiple sources in one Chicago footnote are separated by semicolons.
- [ ] Printed pages were extracted from original source files and visually checked where available.
- [ ] `file p.` is used only where printed pagination cannot be confirmed or does not exist.
- [ ] No page-placeholder wording remains.
- [ ] Writing-quality/style gate confirms the chapter is evidence-first and not generic AI-like prose.
- [ ] Layout inspection or rendered pages show no blank pages or severe overflow.
```

## Journal Lane Status

```markdown
# Journal Lane Status

target:
status:
submission route:
submission id:
last verified:
active files:

## Official requirements checked

## Evidence and citation status

## Similarity-risk notes

## Submission/monitoring record
```

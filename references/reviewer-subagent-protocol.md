# Reviewer and Subagent Protocol

Use this reference before finalization, major revision, or response to reviewers.

## Non-Skip Gate

Reviewer review is a workflow gate, not optional polish, in these cases:

- the user asks to follow the full skill workflow;
- the user asks for final delivery, final draft, DOCX/final manuscript, submission package, or dissertation-chapter completion;
- the task is a major revision, response to reviewers, or evidence-sensitive dissertation/publication draft;
- the user explicitly mentions subagents, external review, reviewer passes, strict checking, or "不要跳过".

Do not mark the project as final-ready until this gate has a visible artifact:

1. reviewer reports or role-labeled self-review reports;
2. a synthesis of duplicate/conflicting comments;
3. a prioritized revision plan;
4. a record of which revisions were applied, rejected, or left for manual follow-up.

If subagent tools are available and the user has explicitly requested subagents, independent agents, or parallel review, spawn separate subagents for distinct roles. If subagents are unavailable or not explicitly authorized in the current tool environment, state that limitation and run the same roles sequentially in the main thread. Do not silently replace a requested subagent review with an unlabelled internal check.

When a user asks for the full workflow, says not to skip steps, or the current thread or project handoff explicitly requires subagents, treat the reviewer gate as automatic for the current dissertation or publication task. Actual subagent spawning still depends on tool availability and user authorization; if subagents cannot be spawned, run distinct role-labeled reports and record that limitation. Do not wait for a second reminder before running the reviewer gate.

## Default Reviewer Passes

Run at least one strict pass. For high-stakes submission, use several distinct perspectives:

1. Editor-in-chief: scope, journal fit, contribution, desk-rejection risk.
2. Field reviewer: musicology/music education relevance, literature positioning, terminology.
3. Method reviewer: corpus, source selection, document-analysis logic, limits.
4. Citation auditor: page numbers, reference correspondence, Chinese titles/translations, DOI/URL accuracy.
5. Structure reviewer: reverse outline, paragraph function, section order, repetition, and whether the draft is organized by argument rather than by source list.
6. Devil's advocate: strongest counterargument, overclaiming, missing alternative explanation, similarity risk.

If subagents are available and explicitly authorized for the current task, run them independently. If not, perform separate role-labeled passes in one thread and keep the outputs separate.

For dissertation-chapter work, the minimum independent roles are:

1. dissertation examiner: argument, structure, chapter scope, contribution;
2. field reviewer: musicology / music education / reception-history accuracy;
3. citation and evidence auditor: source matrix, page locators, primary/secondary source boundaries;
4. devil's advocate: overclaiming, similarity risk, strongest objections.

For reception-history dissertation chapters, add a horizon-of-expectation check to the dissertation examiner or field reviewer brief: the review must identify any section that is only chronology, biography, repertoire inventory, or source summary without explaining receiver horizon and change in meaning.

For final DOCX or submission packages, add a layout/format auditor after the revised document exists.

## Inputs to Give Reviewers

Provide:

- manuscript draft;
- target journal or thesis requirements;
- source matrix and evidence log if available;
- source-synthesis map, reverse outline, or chapter/article plan if available;
- current research questions;
- known constraints such as word limit, anonymity, similarity risk, or no new sources.

Do not provide the desired answer, your planned fix, or hidden conclusions unless the review task explicitly requires them.

## Reviewer Output Template

```markdown
# Reviewer Report

## Recommendation
Accept / minor revision / major revision / reject / not ready

## Blocking issues
1.

## Major comments
1. Issue:
   Evidence:
   Required revision:

## Minor comments
1.

## Citation or evidence risks
1.

## Journal/thesis fit risks
1.

## Revision priorities
1.
```

Every criticism should name what is wrong, where it occurs, why it matters, and how to fix it.

## Revision Planning

After reviewer reports:

1. Merge duplicate comments.
2. Separate blocking issues from optional polish.
3. Reject suggestions that would violate the evidence boundary, target scope, or deadline.
4. Create a prioritized revision plan.
5. If the critique concerns structure, create or update a reverse outline before editing.
6. Apply surgical edits first.
7. Re-review only the changed risk areas unless the article was structurally rewritten.

Record the synthesis and plan in the project workspace before editing when the project is long-running or evidence-sensitive. A concise `*_review_synthesis_*` or `*_revision_plan_*` file is enough; do not bury the plan only in chat if later agents will continue the work.

## Re-Review

A re-review verifies whether changes actually addressed the prior issues. It should check:

- each reviewer concern;
- author's claimed action;
- exact manuscript location;
- whether the issue is resolved, partially resolved, or unresolved;
- whether new problems were introduced.

Do not rubber-stamp. If a claim says “fixed,” verify it in the revised text.

## Subagent Prompt Pattern

Use a prompt like:

```text
Use the skill in this folder to review the attached manuscript for [target journal/thesis requirement]. Act as [reviewer role]. Give a decision-style report with blocking issues, major comments, citation/evidence risks, and concrete revision priorities. Do not rewrite the manuscript.
```

For a citation-only pass:

```text
Audit the manuscript against the source matrix and evidence log. Identify unsupported claims, missing page numbers, reference-list mismatches, web citation weaknesses, and Chinese-title translation issues. Do not edit the manuscript.
```

For a dissertation Chicago-footnote pass:

```text
Audit the dissertation chapter's Chicago Notes-Bibliography footnotes. Verify that each citation position has one note callout where appropriate, that multiple sources in one note are separated clearly, that printed pages were checked from the source files when available, that `file p.` appears only when printed pagination cannot be confirmed or does not exist, and that no unresolved page placeholders remain. Do not rewrite the chapter.
```

For a dissertation chapter full-workflow pass:

```text
Review this dissertation chapter as [role]. Use the current evidence log, source matrix, page-locator audit, and manuscript draft. Do not edit files. Return a decision-style report with blocking issues, major comments, citation/evidence risks, and concrete paragraph-level revision priorities. Flag any unsupported claim, overclaim, primary/secondary source confusion, or missing printed-page verification.
```

For a reverse-outline structure pass:

```text
Create a reverse outline of this draft. For each paragraph or paragraph group, identify its function, relationship to the thesis or research question, evidence used, repetition, and whether it should be kept, moved, merged, split, or cut. Do not rewrite the manuscript.
```

For a full-dissertation consistency pass:

```text
Audit the whole dissertation for citation-style consistency. Check that Chicago Notes-Bibliography rules are applied across every chapter, that first and shortened notes are consistent, that multiple same-position sources are inside one footnote separated by semicolons, that bibliography entries correspond to cited sources, that printed pages were verified from original source files, and that DOCX remains the final deliverable unless PDF was requested. Do not rewrite the dissertation.
```

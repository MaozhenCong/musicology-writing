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

If the user or a current project instruction explicitly requires subagents, run the capability preflight below and spawn separate subagents for distinct roles. Do not silently replace a requested subagent review with an internal check.

When a user asks for the full workflow, says not to skip steps, or the current thread or project handoff explicitly requires subagents, treat the reviewer gate as automatic for the current dissertation or publication task. A project-local standing instruction that requires actual subagents counts as authorization. Do not wait for a second reminder before running the reviewer gate.

## Capability Preflight and Agent Receipts

Before declaring that subagents are unavailable:

1. Inspect the complete callable-tool metadata, including deferred, lazy-loaded, orchestrator, or plugin-provided tools. Search names and descriptions for `subagent`, `multi-agent`, `spawn`, `delegate`, or equivalent capabilities.
2. Do not rely only on the tools printed in the initial prompt. In Codex environments, deferred tools may be discoverable through the global tool registry; `multi_agent_v1__spawn_agent` is one current example.
3. If a matching capability appears, call it for a real, bounded reviewer task. A registry match without an attempted call is not proof that the gate ran.
4. Record each spawned agent's ID, reviewer role, input files, completion status, and saved report path in the reviewer synthesis or execution log.
5. Declare unavailability only after the complete registry search returns no matching capability or an actual spawn call fails. Save the exact error or discovery result.
6. Close completed agents after their reports have been integrated when the environment requires explicit cleanup.

If actual subagents are explicitly required and the preflight genuinely fails, mark the reviewer gate `blocked: actual subagent unavailable`. Sequential role-labeled self-review may keep work moving, but it does not make the package final-ready unless the user explicitly waives the requirement. Never describe a self-review as a subagent report.

## Default Reviewer Passes

Run at least one strict pass. For high-stakes submission, use several distinct perspectives:

1. Editor-in-chief: scope, journal fit, contribution, desk-rejection risk.
2. Field reviewer: musicology/music education relevance, literature positioning, terminology.
3. Method reviewer: corpus, source selection, document-analysis logic, limits.
4. Citation auditor: page numbers, reference correspondence, Chinese titles/translations, DOI/URL accuracy.
5. Structure reviewer: reverse outline, paragraph function, section order, repetition, and whether the draft is organized by argument rather than by source list.
6. Devil's advocate: strongest counterargument, overclaiming, missing alternative explanation, similarity risk.
7. Style-quality reviewer: evidence-first prose, paragraph rhythm, repeated formulae, over-abstract terminology, and AI-like style risk. This reviewer improves clarity and authorial control; it must not hide required AI-use disclosure.
8. Contribution and relevance reviewer: field problem, evidence-backed gap, contribution, strongest counterargument, and the boundary between demonstrated impact and a proposed use.

If subagents are required and available, run them independently. If actual subagents were not required or authorized, perform separate role-labeled passes in one thread and keep the outputs separate.

For dissertation-chapter work, the minimum independent roles are:

1. dissertation examiner: argument, structure, chapter scope, contribution;
2. field reviewer: musicology / music education / reception-history accuracy;
3. citation and evidence auditor: source matrix, page locators, primary/secondary source boundaries;
4. devil's advocate: overclaiming, similarity risk, strongest objections.

For reception-history dissertation chapters, add a horizon-of-expectation check to the dissertation examiner or field reviewer brief: the review must identify any section that is only chronology, biography, repertoire inventory, or source summary without explaining receiver horizon and change in meaning.

For a new topic, a major dissertation expansion, or a manuscript whose central contribution changed during revision, include the contribution and relevance role. This role is also mandatory for every final manuscript, final DOCX, or submission package. It may be combined with an editor-in-chief report only when the report explicitly gives a contribution/relevance verdict against the Topic Decision Record. This role must reject claims of novelty, originality, significance, or practical impact that are not supported by the field map, corpus, or manuscript.

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

For a style-quality pass:

```text
Review this manuscript for writing quality and AI-like style risk. Use `references/writing-quality-style.md`. Do not rewrite the manuscript. Identify paragraphs where concepts replace evidence, where sentence rhythm is formulaic, where repeated terms or triads weaken the prose, and where the author should use more concrete source-specific wording. Preserve required AI-use disclosure and do not suggest hiding AI assistance.
```

For a contribution and relevance pass:

```text
Review this manuscript or topic decision record for research design. Verify that it distinguishes topic, research problem, evidence-backed gap, research question, contribution, and practical relevance. Test the strongest counterargument. Flag any novelty claim based only on absence, any gap unsupported by mapped literature, and any claim that confuses demonstrated impact with a proposed use. Do not rewrite the manuscript.
```

For a full-dissertation consistency pass:

```text
Audit the whole dissertation for citation-style consistency. Check that Chicago Notes-Bibliography rules are applied across every chapter, that first and shortened notes are consistent, that multiple same-position sources are inside one footnote separated by semicolons, that bibliography entries correspond to cited sources, that printed pages were verified from original source files, and that DOCX remains the final deliverable unless PDF was requested. Do not rewrite the dissertation.
```

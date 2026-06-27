# Reviewer and Subagent Protocol

Use this reference before finalization, major revision, or response to reviewers.

## Default Reviewer Passes

Run at least one strict pass. For high-stakes submission, use several distinct perspectives:

1. Editor-in-chief: scope, journal fit, contribution, desk-rejection risk.
2. Field reviewer: musicology/music education relevance, literature positioning, terminology.
3. Method reviewer: corpus, source selection, document-analysis logic, limits.
4. Citation auditor: page numbers, reference correspondence, Chinese titles/translations, DOI/URL accuracy.
5. Devil's advocate: strongest counterargument, overclaiming, missing alternative explanation, similarity risk.

If subagents are available, run them independently. If not, perform separate role-labeled passes in one thread and keep the outputs separate.

## Inputs to Give Reviewers

Provide:

- manuscript draft;
- target journal or thesis requirements;
- source matrix and evidence log if available;
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
5. Apply surgical edits first.
6. Re-review only the changed risk areas unless the article was structurally rewritten.

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

For a full-dissertation consistency pass:

```text
Audit the whole dissertation for citation-style consistency. Check that Chicago Notes-Bibliography rules are applied across every chapter, that first and shortened notes are consistent, that multiple same-position sources are inside one footnote separated by semicolons, that bibliography entries correspond to cited sources, that printed pages were verified from original source files, and that DOCX remains the final deliverable unless PDF was requested. Do not rewrite the dissertation.
```

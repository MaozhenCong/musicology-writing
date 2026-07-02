---
name: musicology-writing
description: >-
  Use for end-to-end musicology, music education, piano pedagogy,
  cross-cultural music education, Western classical music in China, or
  doctoral-publication writing workflows: full PhD dissertations, dissertation
  chapters or introductions, journal articles, Zotero intake, evidence
  matrices, source-safe drafting, Chicago or journal-style footnotes, verified
  printed-page citations, DOCX/final manuscript preparation, non-fabrication
  checks, reviewer/subagent critique, OJS/email submission, response to
  reviewers, and withdrawal/resubmission (/cancel-subscription). Trigger when
  the user mentions musicology/music education papers, PhD dissertations,
  doctoral chapters, dissertation introductions, journal articles, Zotero,
  literature review, source matrix, exact page citations, real printed pages,
  "不要杜撰", footnotes, reviewer/subagent review, target journal requirements,
  similarity risk, anonymous manuscript, final draft, response to reviewers,
  withdraw submission, cancel submission, 撤稿, or /cancel-subscription.
---

# Musicology / Music Education Academic Writing

## Purpose

Use this skill to run a source-safe academic writing workflow for musicology and music education projects. Prioritize verifiable scholarship, exact source handling, target-journal or doctoral-rule compliance, and iterative reviewer-style revision.

The default success criterion is not “a polished-looking essay.” It is a manuscript package whose claims can be traced to sources, whose scope matches the evidence, and whose final files fit the target journal or thesis requirement.

This is one v1 skill with two explicit tracks, not two separate skills: a doctoral-dissertation track and a journal-article track. Keep them inside one skill because Zotero intake, evidence matrices, page verification, no-fabrication rules, and reviewer passes are shared. Separate them only at the workflow-reference level so citation style, output format, and project-state rules do not drift.

## Operating Principles

1. State assumptions and unresolved ambiguities before making consequential choices.
2. Choose the track early: dissertation chapter, journal article, response to reviewers, withdrawal/resubmission, or exploratory planning.
3. Keep each project, thesis chapter, or target journal in its own folder/status record unless the user explicitly asks for comparison.
4. For journal articles, prefer the smallest publishable topic over a broad dissertation-scale theme; for thesis chapters, preserve breadth but make every claim evidence-bound.
5. For full-dissertation or dissertation-chapter DOCX work, default to a DOCX deliverable and do not generate a final PDF unless the user asks for it. Render pages only for layout QA when needed.
6. Treat citation priority as content-driven: do not drop or demote relevant literature merely because page extraction is difficult.
7. Treat official requirements, source PDFs, verified web snapshots, and saved correspondence as stronger evidence than memory or search snippets.
8. Do not invent facts, page numbers, source contents, deadlines, fees, editorial policies, issue timing, or reviewer comments.
9. Preserve project artifacts: source matrix, evidence log, reading notes, outline, draft, reviewer reports, revision plan, final checklist, and submission record.
10. Treat workflow stages as gates, not suggestions. When the user asks to follow the full skill workflow, continue through every required gate until complete or explicitly blocked; do not stop after drafting, citation checking, or file generation if reviewer, revision, audit, or final-package gates remain.
11. Before large edits or automated file repair, create a clearly named backup or working copy. Do not overwrite the user's only editable manuscript.
12. Classify work before editing: substantive argument revision, source verification, style polishing, formatting repair, journal compliance, or final-package assembly. Report which category was handled.
13. After editing, hand off the updated file path, change summary, unresolved issues, user-confirmation items, and verification status.

## DOCX and Word Safety

Use native Word/DOCX handling conservatively because musicology manuscripts often depend on footnotes, italics, non-Latin characters, and bibliography formatting.

1. Prefer editing and saving native `.docx` files. Avoid format round-trips through LibreOffice, ODT, HTML, PDF, or other intermediates for final formatting unless needed to rescue a damaged file or explicitly requested.
2. Preserve Word footnotes as real footnotes with superscript body references and page-bottom note text; do not replace them with typed numbers, endnotes, plain paragraphs, or manually assembled note lists.
3. Preserve headings, bibliography, italics, Chinese characters, Polish/French/Spanish diacritics, and Chicago note punctuation during automated edits.
4. If Microsoft Word reports unreadable content or asks to recover a document, stop iterative blind repair. Preserve the original, open the recovered content only when necessary, and save the recovered document immediately under a new clean `.docx` filename before continuing.
5. When automating Word on macOS, operate on the active recovered document when Word is in a dialog/recovery state. Avoid fragile assumptions such as `count documents`; first verify the active document name and save a new copy.
6. After automated DOCX repair or generation, validate both structurally and practically: check footnote-reference/definition counts, inspect rendered pages, and when possible confirm that Microsoft Word opens the file without a recovery dialog.
7. Long footnotes can still cross pages in real Word layout. To reduce this risk, split overloaded prose into source-specific sentences, keep each footnote compact, and avoid large authority-accumulation notes.

## Musicology Argumentation Standards

1. Keep primary-source strategy inside the general source and methodology discussion unless the genre explicitly requires a separate citation-policy section.
2. Use secondary scholarship for its own argument. If a secondary source merely points to an accessible primary source, trace through to the primary source and cite it directly whenever feasible.
3. Avoid unnecessary second-hand citation. Use "quoted in," "cited in," or "discussed in" only when the primary source cannot be accessed and the dependency must be disclosed.
4. Do not overclaim direct influence, lineage, reception, classroom practice, or audience effect unless the evidence proves it. Use careful formulations such as "mediating framework," "analytical metalanguage," "institutional discourse," "pedagogical adaptation," "published pedagogical discourse," or "documented reception trace" when the evidence supports a more limited claim.
5. Keep claims modest, defensible, and evidence-bound for doctoral musicology and peer review. Prefer a narrower proven claim over a broader attractive claim.

## Workflow Router

- Starting from scratch: read `references/end-to-end-workflow.md` and begin at intake/topic selection.
- Writing or revising a dissertation chapter, introduction, or literature review: read `references/dissertation-chapter-workflow.md`.
- Writing, submitting, revising, or monitoring a journal article: read `references/journal-article-workflow.md`.
- Searching or importing literature: read `references/evidence-citation-zotero.md`.
- Drafting, revising, or checking citations: read `references/evidence-citation-zotero.md` and the current project evidence files.
- Adapting to a journal, OJS, email submission, or doctoral thesis rule: read `references/journal-thesis-adaptation.md`.
- Running reviewer/subagent critique: read `references/reviewer-subagent-protocol.md`.
- Needing reusable tables/checklists: read `references/templates.md`.
- Needing examples from the three observed submission patterns: read `references/case-patterns.md`.
- Withdrawing a submission, cancelling a submission, or resubmitting to a new target: read `references/withdraw-resubmit.md`.
- Sharing through GitHub or using this skill with non-Codex agents: read `references/agent-portability.md`.

Load only the reference files required for the current phase.

## End-to-End Stages

1. Intake and boundaries: identify track, output type, language, target, deadline, evidence already available, and what must not be mixed with other projects.
2. Topic selection: narrow the topic until it can be supported by available sources without overclaiming.
3. Target fit: verify journal or thesis requirements from official sources and save the evidence.
4. Literature discovery and Zotero intake: search, download, import, tag, and record what is readable.
5. Reading and annotation: create source notes and extract exact claims with page numbers or stable web evidence.
6. Evidence system: maintain a source matrix and evidence log before heavy drafting.
7. Architecture: build a claim-evidence outline, not just a heading list.
8. Literature review and method: synthesize by theme and state corpus limits honestly.
9. Drafting: write section by section from the evidence map; mark gaps instead of filling them with guesses.
10. Citation audit: check every substantive claim, quote, paraphrase, page number, and reference-list entry.
11. Reviewer loop: use strict reviewer passes or subagents to identify desk-rejection risks, weak claims, missing evidence, and format problems. This gate is complete only after reviewer reports or role-labeled reports are saved or summarized, and a revision plan is created.
12. Revision: revise against a prioritized plan; avoid broad rewrites when two surgical edits solve the issue. This gate is complete only after the revised text is checked against the reviewer plan.
13. Final package: generate the manuscript, metadata, declarations, cover letter or OJS fields, and final checklist.
14. Submission and monitoring: record exact submission details; after submission, freeze the submitted version unless the journal requests revision.
15. Withdrawal and resubmission (/cancel-subscription): verify withdrawal reason, draft withdrawal letter, freeze records, update project status, and if resubmitting, re-check target fit and similarity risk before creating a new lane.

## Source and Citation Rules

1. Every central claim must trace to a source ID or evidence-log item.
2. Paginated sources require exact checked page numbers for citation-sensitive claims. When the user asks for real printed pages, inspect the source file or rendered pages rather than trusting automated extraction.
3. Do not drop relevant literature merely because automatic printed-page extraction fails; preserve the source and keep PDF/file locator pages or other locators for manual page correction.
4. Web sources require title, responsible institution/author where available, URL, access date, and a saved copy or snapshot when possible.
5. Chinese sources should preserve the original Chinese title and provide an English translation; do not replace titles with pinyin.
6. Across all writing tracks, avoid piling several footnote callouts after one sentence. When possible, split the prose into separate evidence-specific sentences and give each source or source group its own note callout.
7. Use one note callout at a citation position. Put multiple sources in that single footnote, separated by semicolons, only when the same sentence or clause genuinely requires several sources together.
8. For high-traceability drafting, prefer source-specific footnotes over large authority-accumulation notes. Do not merge sources merely to reduce note count.
9. If no printed pagination exists after inspection, cite a concise locator such as `file p. 6`; do not add verbose page-warning prose inside the footnote.
10. Treat machine translations and AI summaries as reading aids only. Do not cite them as sources.
11. If a source is unreadable, incomplete, or only metadata-level, label it as such and do not use it for exact claims.
12. Similarity-risk control is a writing constraint: avoid reusing dissertation phrasing, previously submitted article structures, or high-risk topic-word clusters.
13. Do not invent DOI, page numbers, publication places, journal issue numbers, translated titles, institutional titles, or source contents. If DOI or other metadata is absent, mark it absent or needs verification instead of fabricating it.
14. For Chinese sources in English-language manuscripts, use one consistent format: English translation or romanized author/title form first when appropriate, with Chinese characters in parentheses for verification. Preserve original Chinese titles, publishers, and institutions where needed.
15. Verify every added reference before inserting it. Add references only when they support a specific claim, strengthen the argument, or broaden a comparison in a defensible way; never inflate a bibliography for appearance.
16. Separate primary sources, secondary scholarship, institutional documents, and methodological references in notes, matrices, or discussion when the distinction helps the reader understand evidentiary status.

## Journal Submission Compliance

1. Check official journal guidelines directly before making claims about word/character limit, anonymity, author-information files, abstract and keyword requirements, reference style, file format, cover letters, declarations, fees, or submission route.
2. Do not infer anonymous-manuscript requirements, separate title pages, or cover-letter rules unless the guidelines explicitly say so.
3. Record journal rules as `required`, `recommended`, or `not specified`. If a guideline says 4000-8000 words, do not replace it with an invented limit.
4. Keep a submission checklist and save evidence from official pages, OJS screens, editor emails, or downloaded guidelines.

## Reviewer / Subagent Rule

Before finalization, run at least one strict reviewer pass. For dissertation chapters, final manuscripts, major revisions, or any request that says to follow the full workflow, use the reviewer/subagent gate before final delivery. If subagents or fresh threads are available and the user has explicitly requested subagents, independent agents, or parallel review, spawn distinct reviewer subagents rather than silently doing a single self-review. Give them the manuscript and target requirements, not the intended answer. Ask for specific, evidence-based criticism and a decision-style recommendation. If subagents are unavailable or not explicitly authorized in the current tool environment, say so explicitly and perform separate role-labeled passes in sequence, keeping their reports distinct.

The reviewer pass is read-only by default. Convert criticism into a prioritized revision plan before editing. Do not mark the final package ready until the handoff can identify the reviewer reports, the synthesis or revision plan, and the actions taken. If the reviewer gate is intentionally skipped by user instruction, state that exception in the final checklist.

## Final Package Rule

A final package is ready only when these items are checked:

1. Current target requirements were verified from official or saved sources.
2. Manuscript scope matches available evidence.
3. Source matrix and evidence log agree with the final text.
4. Citation style, bibliography, page numbers, URLs, and access dates were audited.
5. Reviewer/subagent gate was completed or explicitly documented as unavailable or user-skipped.
6. Required declarations are present and truthfully worded.
7. Anonymous and authored versions are handled according to the target rules.
8. DOCX/PDF layout and metadata were inspected when those formats matter; if the user asks for DOCX only, do not deliver a final PDF.
9. The user-facing handoff names the ready files and manual confirmations still required.

## Portability for Other Agents

This skill is intentionally plain Markdown. Other agents should follow `SKILL.md` first, then load the relevant files in `references/`. Do not rely on local absolute paths, private memories, or one product's tool names. When moving this skill to another repository, keep the folder name, `SKILL.md`, `agents/openai.yaml`, and all `references/` files together. See `references/agent-portability.md` for cross-agent usage.

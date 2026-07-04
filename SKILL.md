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

This is one v1 skill with two explicit tracks, not two separate skills: a doctoral-dissertation track and a journal-article track. Keep them inside one skill because Zotero intake, evidence matrices, page verification, no-fabrication rules, and reviewer passes are shared. Separate them at the workflow-reference level so citation style, output format, and project-state rules do not drift. Dissertation defaults do not override a target journal's official instructions.

## Track Boundaries

- **Always shared:** source verification, no fabrication, exact page discipline, primary/secondary evidence distinction, backup-before-large-edit, reviewer/audit gates, and clear handoff.
- **Dissertation defaults:** chapter-scale breadth, Chicago-style footnotes unless the institution says otherwise, full DOCX chapter delivery, dissertation bibliography consistency, and source/method framing designed for thesis chapters.
- **Journal-specific:** word limit, anonymity, title page, abstract/keywords, reference style, footnote/endnote policy, file format, cover letter, declarations, figures/tables, and metadata. Verify these from the target journal's official site or submission system every time.
- If a dissertation rule and a journal rule conflict, follow the journal rule for journal work and record the difference in the submission checklist.

## Operating Principles

1. State assumptions and unresolved ambiguities before making consequential choices.
2. Choose the track early: dissertation chapter, journal article, response to reviewers, withdrawal/resubmission, or exploratory planning.
3. Treat recent DOCX, citation, and primary-source lessons as doctoral-dissertation safety defaults unless they are listed above as always shared. For journal submissions, re-check and follow the specific journal's official guidelines even when they differ from dissertation practice.
4. Before editing an existing long-running workspace, read its status or handoff files, latest audit/checklist, active draft, source/evidence records, and any submission record. Identify whether the work is drafting, submitted/under review, revision, monitoring, or withdrawn.
5. Keep each project, thesis chapter, or target journal in its own folder/status record unless the user explicitly asks for comparison.
6. For journal articles, prefer the smallest publishable topic over a broad dissertation-scale theme; for thesis chapters, preserve breadth but make every claim evidence-bound.
7. For full-dissertation or dissertation-chapter DOCX work, default to a DOCX deliverable and do not generate a final PDF unless the user asks for it. Render pages only for layout QA when needed.
8. Treat citation priority as content-driven: do not drop or demote relevant literature merely because page extraction is difficult.
9. Treat official requirements, source PDFs, verified web snapshots, saved correspondence, and project-local status records as stronger evidence than memory or search snippets.
10. Do not invent facts, page numbers, source contents, deadlines, fees, editorial policies, issue timing, or reviewer comments.
11. Preserve project artifacts: status snapshot, source matrix, evidence log, reading notes, claim-evidence outline, reverse-outline or structure audit, draft, reviewer reports, revision plan, final checklist, and submission record.
12. Treat workflow stages as gates, not suggestions. When the user asks to follow the full skill workflow, continue through every required gate until complete or explicitly blocked; do not stop after drafting, citation checking, or file generation if reviewer, revision, audit, or final-package gates remain.
13. Before large edits or automated file repair, create a clearly named backup or working copy. Do not overwrite the user's only editable manuscript.
14. Classify work before editing: substantive argument revision, source verification, style polishing, formatting repair, journal compliance, or final-package assembly. Report which category was handled.
15. After editing, hand off the updated file path, change summary, unresolved issues, user-confirmation items, and verification status.
16. For reception-history dissertation work, keep the chapter centered on the receiver's horizon of expectation: identify the receiver group, prior musical/cultural horizon, source-proven trigger, and horizon change before expanding chronology, repertoire, or institutional background.

## DOCX and Word Safety

Use native Word/DOCX handling conservatively because musicology manuscripts often depend on footnotes, italics, non-Latin characters, and bibliography formatting.

1. Prefer editing and saving native `.docx` files. Avoid format round-trips through LibreOffice, ODT, HTML, PDF, or other intermediates for final formatting unless needed to rescue a damaged file or explicitly requested.
2. For dissertation chapters using footnotes, preserve Word footnotes as real footnotes with superscript body references and page-bottom note text; do not replace them with typed numbers, endnotes, plain paragraphs, or manually assembled note lists. For journal manuscripts, first check whether the journal requires footnotes, endnotes, author-date citations, or another system.
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
6. For reception-aesthetics work, do not let a source inventory become the argument. Use prior dissertations and catalogues as source maps or baselines, then build the manuscript around historically specific receivers, expectations, media, institutions, and changes in meaning.

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
- Reassessing or improving this workflow from real project use: read `references/end-to-end-workflow.md`, then the relevant track file, `references/evidence-citation-zotero.md`, and `references/templates.md`.
- Withdrawing a submission, cancelling a submission, or resubmitting to a new target: read `references/withdraw-resubmit.md`.
- Sharing through GitHub or using this skill with non-Codex agents: read `references/agent-portability.md`.

Load only the reference files required for the current phase.

## End-to-End Stages

1. Project-state discovery: identify the active folder/lane/chapter, current status, latest authoritative draft, frozen submitted files, and stop conditions before changing anything.
2. Intake and boundaries: identify track, output type, language, target, deadline, evidence already available, and what must not be mixed with other projects.
3. Topic selection: narrow the topic until it can be supported by available sources without overclaiming.
4. Target fit: verify journal or thesis requirements from official sources and save the evidence.
5. Literature discovery and Zotero intake: search, download, import, tag, and record what is readable.
6. Reading and annotation: create source notes that summarize, assess, and state how each source can be used; extract exact claims with page numbers or stable web evidence.
7. Evidence system: maintain a source matrix, evidence log, page-locator audit, and source-synthesis map before heavy drafting.
8. Architecture: build a claim-evidence outline or prospectus-style plan, not just a heading list. For reception-history chapters, include a horizon-of-expectation spine before drafting.
9. Literature review and method: synthesize by theme, method, corpus, and outlier evidence; state corpus limits honestly.
10. Drafting: write section by section from the evidence map; mark gaps instead of filling them with guesses.
11. Structural audit: after a full draft, create a reverse outline or paragraph-function check before polishing.
12. Citation audit: check every substantive claim, quote, paraphrase, page number, and reference-list entry.
13. Reviewer loop: use strict reviewer passes or subagents to identify desk-rejection risks, weak claims, missing evidence, and format problems. This gate is complete only after reviewer reports or role-labeled reports are saved or summarized, and a revision plan is created.
14. Revision: revise against a prioritized plan; avoid broad rewrites when two surgical edits solve the issue. This gate is complete only after the revised text is checked against the reviewer plan.
15. Final package: generate the manuscript, metadata, declarations, cover letter or OJS fields, and final checklist.
16. Submission and monitoring: record exact submission details; after submission, freeze the submitted version unless the journal requests revision.
17. Withdrawal and resubmission (/cancel-subscription): verify withdrawal reason, draft withdrawal letter, freeze records, update project status, and if resubmitting, re-check target fit and similarity risk before creating a new lane.

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
14. For dissertation chapters in English, use one consistent Chinese-source format unless the institution requires otherwise: English translation or romanized author/title form first when appropriate, with Chinese characters in parentheses for verification. For journal articles, follow the target journal's citation style while still preserving enough Chinese metadata for verification.
15. Verify every added reference before inserting it. Add references only when they support a specific claim, strengthen the argument, or broaden a comparison in a defensible way; never inflate a bibliography for appearance.
16. Separate primary sources, secondary scholarship, institutional documents, and methodological references in notes, matrices, or discussion when the distinction helps the reader understand evidentiary status.

## Journal Submission Compliance

1. For journal work, official target-journal guidelines control over dissertation defaults, prior experience, and generic style assumptions.
2. Check official journal guidelines directly before making claims about word/character limit, anonymity, author-information files, abstract and keyword requirements, reference style, file format, cover letters, declarations, fees, or submission route.
3. Do not infer anonymous-manuscript requirements, separate title pages, or cover-letter rules unless the guidelines explicitly say so.
4. Record journal rules as `required`, `recommended`, or `not specified`. If a guideline says 4000-8000 words, do not replace it with an invented limit.
5. Do not apply dissertation footnote, bibliography, heading, file-naming, or DOCX layout defaults to a journal article until the official journal requirements have been checked.
6. Keep a submission checklist and save evidence from official pages, OJS screens, editor emails, or downloaded guidelines.

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

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
11. Reviewer loop: use strict reviewer passes or subagents to identify desk-rejection risks, weak claims, missing evidence, and format problems.
12. Revision: revise against a prioritized plan; avoid broad rewrites when two surgical edits solve the issue.
13. Final package: generate the manuscript, metadata, declarations, cover letter or OJS fields, and final checklist.
14. Submission and monitoring: record exact submission details; after submission, freeze the submitted version unless the journal requests revision.
15. Withdrawal and resubmission (/cancel-subscription): verify withdrawal reason, draft withdrawal letter, freeze records, update project status, and if resubmitting, re-check target fit and similarity risk before creating a new lane.

## Source and Citation Rules

1. Every central claim must trace to a source ID or evidence-log item.
2. Paginated sources require exact checked page numbers for citation-sensitive claims. When the user asks for real printed pages, inspect the source file or rendered pages rather than trusting automated extraction.
3. Do not drop relevant literature merely because automatic printed-page extraction fails; preserve the source and keep PDF/file locator pages or other locators for manual page correction.
4. Web sources require title, responsible institution/author where available, URL, access date, and a saved copy or snapshot when possible.
5. Chinese sources should preserve the original Chinese title and provide an English translation; do not replace titles with pinyin.
6. For full-dissertation Chicago Notes-Bibliography work, use one note callout at a citation position throughout the dissertation; put multiple sources in that single footnote separated by semicolons unless the user or institution requires otherwise. Do not stack several footnote numbers at the same sentence.
7. For journal-article drafting, keep one source per footnote by default for traceability unless the target style or user asks to merge.
8. If no printed pagination exists after inspection, cite a concise locator such as `file p. 6`; do not add verbose page-warning prose inside the footnote.
9. Treat machine translations and AI summaries as reading aids only. Do not cite them as sources.
10. If a source is unreadable, incomplete, or only metadata-level, label it as such and do not use it for exact claims.
11. Similarity-risk control is a writing constraint: avoid reusing dissertation phrasing, previously submitted article structures, or high-risk topic-word clusters.

## Reviewer / Subagent Rule

Before finalization, run at least one strict reviewer pass. If subagents or fresh threads are available, give them the manuscript and target requirements, not the intended answer. Ask for specific, evidence-based criticism and a decision-style recommendation. If subagents are unavailable, perform separate role-labeled passes in sequence and keep their reports distinct.

The reviewer pass is read-only by default. Convert criticism into a prioritized revision plan before editing.

## Final Package Rule

A final package is ready only when these items are checked:

1. Current target requirements were verified from official or saved sources.
2. Manuscript scope matches available evidence.
3. Source matrix and evidence log agree with the final text.
4. Citation style, bibliography, page numbers, URLs, and access dates were audited.
5. Required declarations are present and truthfully worded.
6. Anonymous and authored versions are handled according to the target rules.
7. DOCX/PDF layout and metadata were inspected when those formats matter; if the user asks for DOCX only, do not deliver a final PDF.
8. The user-facing handoff names the ready files and manual confirmations still required.

## Portability for Other Agents

This skill is intentionally plain Markdown. Other agents should follow `SKILL.md` first, then load the relevant files in `references/`. Do not rely on local absolute paths, private memories, or one product's tool names. When moving this skill to another repository, keep the folder name, `SKILL.md`, `agents/openai.yaml`, and all `references/` files together. See `references/agent-portability.md` for cross-agent usage.

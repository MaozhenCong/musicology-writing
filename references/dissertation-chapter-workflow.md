# Dissertation Chapter Workflow

Use this reference for full PhD dissertations, doctoral dissertation chapters, introductions, literature reviews, source-backed expansions, and thesis-format DOCX work.

## Track Rule

Use the dissertation track when the user asks for a full PhD dissertation, chapter, introduction, 30-40 page expansion, thesis draft, supervisor-facing revision, Chicago-style footnotes, or precise printed-page citations. Do not apply journal-lane assumptions such as anonymous submission files, OJS metadata, or aggressive article narrowing unless the user asks for a publication version.

Keep this track in the same skill as journal writing because it shares Zotero, evidence matrices, citation auditing, and reviewer critique. Do not create a separate skill unless the user explicitly wants a different installable package.

## Intake

Confirm or infer:

- chapter type and working title;
- required language and citation style;
- expected length or page target;
- source collection, PDFs, Zotero collection, prior draft, and reviewer comments;
- output format, usually DOCX;
- whether PDF output is forbidden or simply unnecessary;
- known manual page-correction tolerance.

If the user says DOCX only, generate DOCX as the final artifact. Rendering pages for QA is allowed, but do not hand off a final PDF.

For continuation work, identify the latest authoritative draft, latest page/citation audit, latest reviewer synthesis, and any known unresolved primary-page or full-text issues before editing. Do not choose a draft by filename alone if a newer audit says another file is authoritative.

For this user's dissertation work, apply the same footnote logic as all other writing tracks: avoid stacking several note callouts after one sentence; split prose into source-specific claims where possible; use one note callout per citation position; put multiple same-position sources inside that note separated by semicolons only when the claim genuinely needs them together.

For University of Warsaw / WNKS formatting work, also read `warsaw-doctoral-format.md`. Treat checked UW/WNKS documents as authoritative for submission package, APD, summary, and title-page requirements; treat body/footnote typography as working defaults unless a supervisor or doctoral office template says otherwise.

## Full-Dissertation Workspace

For a multi-chapter thesis, keep a stable workspace so future agents do not mix chapter states:

```text
dissertation/
├── status.md
├── source_matrix.tsv
├── evidence_log.tsv
├── page_locator_audit.tsv
├── footnote_audit.tsv
├── chapters/
│   ├── chapter_01_introduction.docx
│   └── chapter_02_*.docx
├── notes_by_source/
└── outputs/
```

Use whatever folder names already exist in the user's workspace, but preserve the same logical separation: dissertation-wide status, dissertation-wide source/evidence/page audits, chapter drafts, and final outputs.

## Prospectus or Chapter-Plan Gate

Before expanding a dissertation chapter substantially, create or update a prospectus-style plan with:

1. working title and chapter function in the full dissertation;
2. summary of the chapter argument;
3. justification for why this chapter belongs in the dissertation;
4. intended method and source corpus;
5. outline or table of contents;
6. bibliography/source-readiness list;
7. page target and what must not be inflated without evidence.

For a full dissertation, maintain both dissertation-wide and chapter-level plans so future agents can distinguish overall thesis logic from the current chapter task.

## Chapter Architecture

Build the chapter as a claim-evidence argument:

1. research problem and dissertation-level stakes;
2. historiographical or pedagogical context;
3. state of scholarship by theme, not by bibliography dump;
4. source corpus and limitations;
5. chapter contribution and research questions;
6. transition to the next chapter or dissertation structure.

For introductions, expand breadth through more literature, clearer field positioning, and sharper research questions. Do not inflate length with unsupported generalizations.

## Reception-Aesthetic Spine

For dissertation chapters about reception history, build a horizon-of-expectation spine before drafting or expanding. Each major section should answer:

1. Who is the receiver or interpretive community?
2. What prior knowledge, practice, institution, medium, repertoire, or political need shaped that receiver's horizon?
3. What feature of the composer, work, genre, performer, or event became meaningful in that horizon?
4. What source proves presence only, and what source proves interpretation or meaning?
5. Did the evidence show confirmation, adjustment, narrowing, rupture, or transformation of the prior horizon?

Do not organize the dissertation chapter merely by chronology, repertoire list, article inventory, or institutional timeline unless that structure directly explains changes in reception. Use earlier dissertations, bibliographies, and catalogues as source maps and baselines, not as the chapter's analytical architecture.

When revising a chapter that has drifted toward summary, add a reverse-outline column for "horizon function." Paragraphs that only say "this happened" or "this source exists" should be revised or cut unless they support a receiver-specific horizon claim.

## Source Coverage Rule

Do not omit relevant literature because page extraction is difficult. Rank sources by relevance, authority, and citation value. Page uncertainty affects the locator label, not whether the source deserves attention.

When a source is locally unavailable or unreadable, do not cite it for exact claims. Either obtain/read the source, use only verified metadata-level claims with caution, or remove the citation.

## Printed-Page Verification Protocol

Use this protocol before final footnotes:

1. Open or render the original source file around each intended citation area.
2. Identify the printed page number visible in the page header/footer or publisher pagination.
3. Map PDF/file page to printed page when they differ.
4. Treat isolated OCR digits, footnote numbers, issue numbers, volume numbers, and running headers as suspect until visually checked.
5. If automatic extraction gives implausible pages, inspect rendered pages manually rather than accepting the extractor.
6. If no printed pagination exists after inspection, use a concise locator such as `file p. 6`.
7. If a local source cannot be found, do not invent a page. Remove the citation or mark the source as unavailable outside the final footnote text.

For every final citation, verify the exact cited page from the original source. For large chapters with many citations, batching is acceptable, but sampling is not enough for final footnotes.

Use `file p.` only after enough inspection to justify that printed pagination is unavailable. Minimum check:

- title/front matter or first article page;
- the cited file page;
- at least one adjacent page before and after when available;
- page header/footer area in rendered view, not text extraction alone;
- publisher/article HTML if the PDF has no printed pages.

If those checks show no printed pagination, use `file p.`. If they show printed pages, cite printed pages.

Record both values in working notes when useful:

```tsv
source_id	claim	printed_page	file_page	status	note
S001	Reception framework	91	5	verified	printed page visible
S002	Web PDF article	file p. 3	3	no printed page	no continuous printed pagination
```

## Chicago Notes-Bibliography Footnotes

For full-dissertation work using Chicago Notes-Bibliography:

- place one note callout at the end of the sentence or clause being supported;
- prefer splitting overloaded citation sentences into several shorter evidence-specific sentences, each with its own note;
- do not leave a note at paragraph end when it only supports one earlier sentence, phrase, or clause;
- if different parts of a sentence rely on different sources, split the sentence or place the callouts after the corresponding clauses;
- put multiple sources for the same citation position in one footnote, separated by semicolons, only when the claim genuinely needs them together;
- do not stack multiple note numbers at one sentence unless the institution explicitly requires it;
- format main text as Times New Roman 12 pt, justified, and double-spaced unless the institution or supervisor requires otherwise;
- format footnote text as Times New Roman 10 pt, justified, and single-spaced unless the institution or supervisor requires otherwise;
- use Word automatic footnote numbering; keep both body callouts and footnote-area numbers superscript; do not type note numbers manually;
- convert Markdown italics or other manuscript markup into real Word formatting so book and standalone-work titles use real italics in body text, footnotes, and bibliography;
- group same-author references only when it improves clarity and does not hide distinct source identities;
- include exact pages for paginated claims;
- extract real printed pages from the original source file whenever available;
- use `file p.` only when printed pagination cannot be confirmed or does not exist after inspection;
- keep non-English source titles in English (original-language) form.

Dissertation-wide Chicago style sheet:

- First citation: use a full note with author, title, container/publisher facts, year, and exact page(s).
- Later citation: use a shortened note, normally author surname or romanized family name, short title, and exact page(s).
- Avoid `ibid.` by default because it becomes fragile during editing; use shortened notes unless the institution requires `ibid.`.
- Bibliography: keep one bibliography entry per cited source. Do not merge different sources in the bibliography merely because they appear in the same footnote.
- Repeated same-position sources: keep one note callout and separate sources inside the note with semicolons.
- Non-English source titles: use English title followed by the original-language title in parentheses; include Chinese author/name or institution in parentheses at first citation when useful. Do not use a French, Chinese, Polish, or other original-language title first with the English title in parentheses in final dissertation prose, footnotes, or bibliography.

Examples:

```text
Kenneth Hamilton, "The Virtuoso Tradition," in The Cambridge Companion to Piano, ed. David Rowland (Cambridge: Cambridge University Press, 1998), 64.

Cyril Ehrlich, The Piano: A History (Oxford: Oxford University Press, 1990), 9-10.

Zhao Feng (赵沨), "Great Victory of the Music Education Revolution" (音乐教育革命的伟大胜利), People's Music (人民音乐), Beijing: People's Music Publishing House (人民音乐出版社), no. 9 (1960): 21.
```

## Drafting Rules

Write from the evidence map:

- Every paragraph should have a clear function in the chapter.
- In reception-history chapters, every paragraph group should identify the receiver horizon it advances or qualifies.
- Long literature sections should synthesize debates, methods, and gaps rather than list sources one by one.
- Use transition sentences to show why musicology, music education, reception history, and piano pedagogy sources belong in the same argument.
- Avoid claiming national, institutional, pedagogical, or student-outcome effects unless the cited corpus directly supports them.
- Mark unresolved evidence in working notes, not in polished prose, unless the limitation belongs in the method section.

After a complete draft exists, create a reverse outline before polishing: one short function statement per paragraph or paragraph group, plus whether it advances the chapter claim, supplies evidence, handles historiography, explains method, or should be cut/merged.

## Reviewer Passes

Before final delivery, run these passes or subagents:

1. dissertation examiner: argument, scope, chapter logic;
2. musicology reviewer: reception/history/conceptual positioning;
3. music education reviewer: pedagogy, curriculum, institutional claims;
4. citation auditor: Chicago notes, Chinese titles, printed pages, missing sources;
5. layout auditor: DOCX footnotes, page flow, blanks, metadata.

The citation auditor must inspect original files for page locators. Do not accept "page needs correction" as final when the user asked for real printed pages.

For long dissertation chapters, combine the musicology and music education roles only if the chapter's content makes them genuinely inseparable; do not combine citation auditing with argument review. The citation/evidence auditor must remain separate because page locators, primary-source boundaries, and bibliography correspondence are common failure points.

When subagents are available and the user has explicitly requested subagents, independent agents, or parallel review, spawn separate reviewer subagents for the independent roles before finalizing. If the user asks for full workflow, strict process, or "不要跳过" without explicit subagent authorization, the reviewer gate still applies; run separate role-labeled reports in the main thread and state whether subagents were not authorized or not available. Save or summarize the reports and create a revision plan before editing.

The dissertation-chapter reviewer gate is complete only when the project has:

- reviewer reports or role-labeled reports;
- a merged synthesis of issues;
- a prioritized revision plan;
- a revised draft that can be checked against the plan;
- a final audit naming unresolved source or page-verification risks.

## Final DOCX Checklist

- [ ] DOCX is the final deliverable unless PDF was requested.
- [ ] Body text is justified and double-spaced unless the institution or supervisor requires otherwise.
- [ ] Footnotes are justified and single-spaced unless the institution or supervisor requires otherwise.
- [ ] Footnote references and footnote definitions match.
- [ ] Book and standalone-work titles use real italics in body text, footnotes, and bibliography.
- [ ] No stacked note numbers where one note callout with semicolons is expected.
- [ ] No unresolved page placeholders remain.
- [ ] `file p.` appears only for sources without verifiable printed pagination.
- [ ] Non-English source titles use English title followed by original-language title in parentheses.
- [ ] Bibliography or references correspond to cited sources.
- [ ] Reviewer/subagent gate was completed, with reports, synthesis, revision plan, and execution notes.
- [ ] Reverse-outline or paragraph-function audit confirms the chapter is not just an expanded source list.
- [ ] For reception-history chapters, a horizon-of-expectation spine or reverse-outline horizon-function check confirms that receiver, prior horizon, evidence type, and horizon change are explicit.
- [ ] Rendered page QA or Word inspection confirms no blank pages or severe footnote overflow.
- [ ] QA page images or temporary render files are not described as the final deliverable unless the user requested them.
- [ ] Handoff states any remaining manual confirmations honestly.

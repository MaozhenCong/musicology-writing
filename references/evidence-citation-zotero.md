# Evidence, Citation, and Zotero Rules

Use this reference whenever the task involves literature search, Zotero, reading notes, citation checking, source matrices, or “不要杜撰”.

## Zotero Intake

For each project, create or identify one project-specific collection. Use tags to separate:

- core secondary literature;
- context literature;
- theory/method literature;
- primary institutional or web sources;
- sources considered but excluded;
- missing full text or unreadable records.

For each imported item, verify:

1. Full text exists and opens.
2. Metadata matches the source: author, title, year, journal/book, volume, issue, pages, DOI/URL.
3. PDF pages or publisher pages are usable for exact citations.
4. The source belongs in the current project rather than a different article lane.

Importing metadata is not enough. A source becomes citation-ready only after it is readable and evidence has been extracted.

## Reading Note Format

Use this compact note for each important source:

```markdown
## Source
source_id:
full citation:
type:
language:
full text status:

## Summary
- main argument or documented fact:

## Assessment
- reliability/method:
- scope:
- limits:

## What it can support
- claim:
- page/evidence location:
- usable section:

## What it cannot support
- limits:
- risks:

## Citation notes
- corrected metadata:
- DOI/URL:
- translation/title handling:

## How it changes the project
- use in argument:
- relation to other sources:
```

## Source Matrix Minimum Columns

Use a table or TSV with:

- source_id
- source_type
- original_title
- english_title
- author_or_institution
- year
- source_language
- evidence_available
- planned_section
- claim_supported
- status
- notes

The matrix answers: “What is in the corpus, what can it prove, and where will it be used?”

## Evidence Log Minimum Columns

Use a table or TSV with:

- claim_id
- claim_text
- evidence_source
- source_location_or_page
- manuscript_location
- risk_level
- verification_status
- notes

The log answers: “Which claims are safe to write?”

## Source Synthesis Map

For literature reviews, dissertation introductions, and theoretical sections, create a source-synthesis map before drafting. It should group sources by relationship rather than bibliography order:

- agreement or shared premise;
- disagreement or tension;
- methodological family;
- corpus or archive type;
- historical period or institution;
- outlier or counterexample;
- source-locating aid rather than direct evidence.

Use the map to decide paragraph order. A paragraph that cites only one source may still be valid, but a long literature review made of one-source paragraphs is usually summary rather than synthesis.

Do not force a relationship between sources. If a source does not belong in a synthesis group, mark it as an outlier, context source, or excluded source.

## Page and Web Evidence Rules

1. If a source has stable page numbers, cite exact pages for claim-level evidence.
2. Do not drop relevant literature only because printed pagination cannot be extracted automatically. Preserve the source in the matrix, keep a PDF/file locator page or other locator for rechecking, and mark the page status explicitly.
3. If a PDF viewer page differs from printed pagination, record both values: the printed page for citation and the PDF/file locator page for rechecking.
4. If printed page numbers are detected automatically, mark them as requiring visual spot-check rather than treating them as infallible.
5. When the user asks for real printed pages, inspect the original source file or rendered page images. Do not rely only on OCR, text extraction, or bibliography snippets.
6. Treat isolated digits, footnote numbers, volume numbers, issue numbers, and running-header fragments as suspect page evidence until visually confirmed.
7. If printed page numbers cannot be verified or do not exist after inspection, do not invent them. Use a concise fallback such as `file p. 6` and keep the source if it is relevant.
8. Page uncertainty should not lower a source's citation priority. Relevance and evidentiary value decide whether to use the source; page status decides only how the locator is written.
9. If a source is a webpage, save title, institution, URL, date if visible, access date, and snapshot path if possible.
10. Do not cite a source for a claim it only loosely resembles.

## Primary-Locator Provenance

Sometimes a secondary source, database record, or institutional summary identifies the exact primary source and page, while the primary page image is not yet locally available. Handle this in two layers:

1. In working evidence files, record both the intended primary locator and the provenance source that supplied it.
2. In the final manuscript, follow the user's citation rule only after the exhausted-primary-search gate below has been satisfied. If the user requires direct primary-page citation after that gate, cite the primary locator directly in final prose, footnotes, and bibliography; do not write "as cited in," "quoted in," "transmitted in," "citing," or similar secondary-transfer labels in final-facing text.
3. In the audit or completion note, state whether the primary page image has actually been visually checked.
4. Do not claim visual inspection of the primary page until it has happened.
5. If the page is central to the argument and still unverified visually, keep it in the manual follow-up list rather than silently treating it as fully verified.

This avoids both errors: hiding the source trail from future agents, and making the polished manuscript look like a secondary transfer when the user's rule is to use the primary page locator.

## Exhausted Primary Search

When a primary source cannot be found, use a two-step exhaustion rule before relying on a transmitted locator or quotation:

1. Automatic search: local workspace, Zotero, saved snapshots, publisher/archive pages, public web, and legal/open databases that are available to the agent.
2. Manual search: the user's library access, CNKI/NLC/archive request, institutional database, or other human-access route when automatic search cannot reach the file.

If both steps fail or the manual step is genuinely blocked, and the user explicitly permits it, a primary locator quoted or cited in reliable literature may be used. Record the dependency in working files:

- missing primary source;
- automatic search routes attempted;
- manual search route attempted, unavailable, or blocked;
- user permission to use the transmitted locator despite the missing primary file;
- secondary source that transmitted the primary locator, quotation, or claim;
- whether the primary image/text was visually inspected;
- whether the final manuscript cites the primary locator directly or discloses "as cited/discussed in."

Do not claim visual inspection of an unseen primary source. Do not quote unseen primary wording unless the secondary source quotes it and the transmission is recorded. If the transmitted source contains an internal conflict, downgrade the claim to a search lead until a primary image or independent corroboration resolves it.

## Replacement and Similar-Source Assessment

When an exact source is missing and similar or additional sources have been imported:

1. Decide what the missing source was supposed to prove.
2. Compare each replacement source against that claim, not against the title alone.
3. Classify replacements as:
   - direct substitute: proves the same claim at comparable or stronger authority;
   - partial substitute: supports context, method, or adjacent evidence only;
   - source-locating aid: helps find primary material but should not support the final claim;
   - not a substitute: belongs in excluded or background notes.
4. Do not cite a replacement as if it were the missing source.
5. Keep missing but important sources in the manual acquisition list when their evidentiary role is unique.

## Footnote Style Rules

These rules apply across dissertation chapters, journal articles, conference papers, and revision packages unless a target style guide explicitly requires another system:

- avoid piling several footnote callouts after one sentence;
- when possible, split the prose into separate evidence-specific sentences and place one note callout after each supported claim;
- place each footnote callout immediately after the cited word, phrase, sentence, or clause; use paragraph-final notes only when the same source group supports the whole paragraph;
- if one sentence contains different facts supported by different sources, split the sentence or place separate callouts at the corresponding clauses;
- during citation audit, verify that each footnote position clearly answers which word, phrase, sentence, or clause the note supports;
- use one note callout at a citation position;
- put multiple sources in that same footnote, separated by semicolons, only when they jointly support the same sentence or clause;
- do not merge sources merely to reduce note count or make a paragraph look shorter;
- avoid stacked note numbers unless the institution, journal, or style guide explicitly requires them;
- keep exact checked pages for each source.

For English academic DOCX files using notes:

- keep main text in Times New Roman 12 pt unless the target requires otherwise;
- for dissertation DOCX output, keep main body paragraphs justified and double-spaced unless the institution or supervisor requires another format;
- keep footnote text in Times New Roman 10 pt, justified, and single-spaced unless the institution or supervisor requires otherwise;
- keep footnote spacing consistent, usually 0 pt or 6 pt after according to the target;
- for dissertation DOCX output, verify double-spaced body paragraphs and single-spaced footnotes unless a later official rule requires otherwise;
- keep bibliography/reference-list entries single-spaced within entries unless the institution or target requires otherwise;
- let Word generate the footnote references automatically;
- keep body-text note callouts superscript;
- keep Word-generated footnote-area numbers superscript as well;
- do not type footnote numbers manually in the body or in the footnote area.
- final Word/DOCX citations must not contain literal Markdown formatting markers such as asterisks around titles; convert book and standalone-work titles to real Word italics in body text, footnotes, and bibliography.
- final English dissertation footnotes and bibliography should put English source titles first, followed by original-language titles in parentheses; do not use original-language titles first with English titles in parentheses.
- if a Markdown source uses inline footnotes such as `^[...]`, the DOCX generator must explicitly parse that form and convert each inline note to a real Word footnote; do not silently drop notes because the generator expected only bottom-defined `[^1]: ...` notes.

For Chicago Notes-Bibliography work:

- use full notes on first citation and shortened notes on later citation unless institutional guidance says otherwise;
- avoid `ibid.` by default because chapter edits can make it ambiguous;
- keep one bibliography entry per cited source even when several sources appear in one footnote.

Use `file p.` only after checking the original source, cited page, adjacent pages when available, and visible page header/footer areas. Do not call an OCR failure a missing printed page.

For author-date or journal-specific styles, keep the same evidence logic during drafting and convert only after page locators have been audited.

## Zotero Reading Note Writeback

When writing generated reading notes back to Zotero:

- Prefer Zotero-supported APIs or connector paths. If those are read-only for child notes, do not silently pretend the writeback succeeded.
- If direct SQLite writeback is necessary, first quit Zotero, create a timestamped backup of `zotero.sqlite`, insert/update notes idempotently using a stable marker such as `codex-source-id`, then reopen Zotero and verify parent-child note counts.
- Reading notes must preserve source coverage even when full text or printed page extraction is incomplete.
- Each note should expose both machine-readable fields and human-readable prose: `source_id`, Zotero parent key, full text status, claim supported, page status, printed page if detected, PDF locator page if needed, and citation risk.

## Chinese-Source Handling

Preserve Chinese specificity:

- In English manuscripts and footnotes, write English translation first and put the original Chinese title in parentheses unless a target style requires another order.
- Keep original Chinese titles in the source matrix and bibliography notes.
- Translate key terms conservatively and consistently.
- For direct quotations, keep a short Chinese excerpt only when necessary and provide English translation.
- For paraphrases, cite the source and page/snapshot; do not rely on AI-generated summaries.

If a Chinese source is used to support an international English argument, explain its institutional context rather than assuming readers know it.

## No-Fabrication Rules

Never fabricate or infer:

- page numbers;
- source contents;
- official journal rules;
- fees or deadlines;
- issue timing;
- editor decisions;
- DOI or publication metadata;
- claims about actual teaching practice from curriculum documents alone;
- claims about student outcomes from documents that only state intended curriculum.

When evidence is missing, write “not verified,” “not specified in the document,” or narrow the claim.

## Similarity-Risk Rules

Before finalization:

1. Compare title, abstract, headings, and central terms against prior submissions and dissertation text.
2. Avoid reusing the same argument architecture across different journal submissions.
3. Use a distinct corpus, thesis, and vocabulary for each article lane.
4. Replace broad or high-risk repeated clusters with precise corpus-bound wording.
5. Do not import attractive paragraphs from another paper just because they are relevant.

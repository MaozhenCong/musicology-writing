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

## Footnote Style Rules

These rules apply across dissertation chapters, journal articles, conference papers, and revision packages unless a target style guide explicitly requires another system:

- avoid piling several footnote callouts after one sentence;
- when possible, split the prose into separate evidence-specific sentences and place one note callout after each supported claim;
- use one note callout at a citation position;
- put multiple sources in that same footnote, separated by semicolons, only when they jointly support the same sentence or clause;
- do not merge sources merely to reduce note count or make a paragraph look shorter;
- avoid stacked note numbers unless the institution, journal, or style guide explicitly requires them;
- keep exact checked pages for each source.

For English academic DOCX files using notes:

- keep main text in Times New Roman 12 pt unless the target requires otherwise;
- keep footnote text in Times New Roman 10 pt, single-spaced;
- keep footnote spacing consistent, usually 0 pt or 6 pt after according to the target;
- let Word generate the footnote references automatically;
- keep body-text note callouts superscript;
- do not type footnote numbers manually in the body or in the footnote area.

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

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
2. Do not drop relevant literature only because printed pagination cannot be extracted automatically. Preserve the source in the matrix, keep a PDF locator page or other locator for manual correction, and mark the page status explicitly.
3. If a PDF viewer page differs from printed pagination, record both values: the printed page for citation and the PDF locator page for rechecking.
4. If printed page numbers are detected automatically, mark them as needing spot-check rather than treating them as infallible.
5. If printed page numbers cannot be verified, do not invent them. Use the PDF locator page as a temporary correction aid and flag the evidence as not final-citation-ready until the user or agent checks the printed page.
6. If a source is a webpage, save title, institution, URL, date if visible, access date, and snapshot path if possible.
7. Do not cite a source for a claim it only loosely resembles.

## Zotero Reading Note Writeback

When writing generated reading notes back to Zotero:

- Prefer Zotero-supported APIs or connector paths. If those are read-only for child notes, do not silently pretend the writeback succeeded.
- If direct SQLite writeback is necessary, first quit Zotero, create a timestamped backup of `zotero.sqlite`, insert/update notes idempotently using a stable marker such as `codex-source-id`, then reopen Zotero and verify parent-child note counts.
- Reading notes must preserve source coverage even when full text or printed page extraction is incomplete.
- Each note should expose both machine-readable fields and human-readable prose: `source_id`, Zotero parent key, full text status, claim supported, page status, printed page if detected, PDF locator page if needed, and citation risk.

## Chinese-Source Handling

Preserve Chinese specificity:

- Keep original Chinese titles.
- Add English translations for international readers.
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

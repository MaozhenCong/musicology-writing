# Dissertation Horizon Architecture

Use this reference for a reception-history dissertation with several historical chapters. It preserves one analytical program across periods without forcing identical section titles or claims.

## Stable Analytical Functions

Every empirical chapter must perform these functions:

1. **Society**: identify the political, educational, institutional, media, diplomatic, market, family, or class conditions that shaped access and value.
2. **Music**: identify the works, genres, techniques, editions, recordings, programmes, repertory hierarchies, and performance practices through which the composer became available.
3. **Reception Profile**: reconstruct observable acts by named receiver groups, distinguishing presence from interpretation and repeated practice.
4. **Horizon of Expectation**: explain which prior knowledge, needs, values, and institutional habits made particular meanings possible or difficult.
5. **Historical Change**: identify confirmation, adjustment, narrowing, rupture, displacement, recoding, institutionalisation, canonisation, expansion, or unresolved competition, then state what horizon the next chapter inherits.

These are analytical functions, not mandatory headings. Evidence density and the period's actual receiver groups determine section order and length.

The dependency is fixed even when headings vary: the horizon claim must be derived from the documented reception profile, and historical change must compare the inherited horizon with the evidence-supported resulting horizon. Context alone cannot establish reception; occurrence alone cannot establish meaning; a later chapter cannot silently redefine what it inherited.

## Project-Level Master Record

Maintain one current, undated dissertation-wide architecture file in the project workspace. Dated plans may remain as provenance, but the undated file is authoritative. Its chapter registry must contain:

| Field | Required content |
|---|---|
| period | Chapter dates and boundary event or condition |
| horizon_in_id | Stable ID for the horizon inherited from the preceding chapter |
| horizon_out_id | Stable ID for the resulting horizon that the next chapter must inherit verbatim |
| receiver_groups | Named interpretive communities or institutions |
| inherited_horizon | What the period receives from the preceding chapter |
| social_conditions | Conditions that alter access, value, or use |
| musical_objects | Works, genres, techniques, media, or performance practices |
| reception_profile | Observable acts and their evidence types |
| evidence_threshold | Trace, tendency, provisional horizon, established horizon, competing horizon, or displaced horizon |
| horizon_change | The chapter's evidence-supported transformation |
| alternative_explanation | Strongest competing account and how evidence limits the claim |
| next_transition | What the following chapter must test rather than assume |
| artifact_paths | Current draft, matrix, reverse outline, reviewer reports, and audit |

Do not fill unknown later chapters with speculative claims. Mark them `pending evidence` and update them only after source intake.

For adjacent chapters, `chapter_n.horizon_out_id` must equal `chapter_n+1.horizon_in_id`. If new evidence changes an inherited horizon, revise the earlier chapter record explicitly and rerun the cross-chapter audit; do not repair the mismatch only in the later chapter.

## Per-Chapter Gates

Before drafting:

- read the current master record and preceding chapter's final mini-conclusion;
- create or update the chapter architecture card;
- state the chapter-specific research problem and difference from a source-map chronology;
- identify which evidence proves presence and which proves meaning.

After drafting:

- produce a reverse outline with a `horizon_function` column;
- write a mini-conclusion for each major receiver group or mechanism;
- state the inherited horizon, chapter-specific change, and next transition;
- run an actual subagent cross-chapter consistency review when project instructions require subagents;
- update the master record before calling the chapter final-ready.

## Consistency Without Repetition

Consistency means the same questions recur, not that the same answer is repeated. A later chapter must not merely rename institutions while retaining an earlier horizon claim. The audit should ask:

1. Which receiver group changed or newly appeared?
2. Which inherited expectation persisted, weakened, or became unavailable?
3. Which new source type permits a stronger or different claim?
4. Does the chapter explain meaning, or only enumerate circulation and teaching?
5. What would falsify the proposed horizon change?
6. Does the transition give the next chapter a testable inherited horizon?

## Cross-Chapter Subagent Brief

Give an independent reviewer the current chapter, preceding chapter conclusion, dissertation master record, source matrix, and reverse outline. Ask the reviewer to identify missing analytical functions, unsupported continuity claims, mechanical repetition, chronology drift, competing horizons, and whether the final transition is testable. Save the agent ID and report path with the chapter audit.

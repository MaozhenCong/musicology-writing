#!/usr/bin/env python3
"""Validate durable reviewer and cross-chapter workflow guards."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "SKILL.md": (
        r"complete callable-tool registry.*deferred",
        r"sequential self-review is not an equivalent substitute",
        r"unavailability blocks final-ready status",
        r"dissertation-horizon-architecture\.md",
        r"Society -> Music -> Reception Profile -> Horizon of Expectation -> Historical Change",
        r"foundational theorists and direct theory texts as the authority layer",
        r"Reserve `acceptance` for demonstrated approval or adoption",
    ),
    "references/reviewer-subagent-protocol.md": (
        r"Capability Preflight and Agent Receipts",
        r"complete callable-tool metadata.*deferred",
        r"actual spawn call fails",
        r"Record each spawned agent's ID",
        r"blocked: actual subagent unavailable",
    ),
    "references/dissertation-chapter-workflow.md": (
        r"Cross-Chapter Horizon Consistency Gate for Reception-History Dissertations",
        r"Apply this gate only when.*reception history.*Do not impose it on all dissertation work",
        r"project-level dissertation horizon architecture",
        r"agent IDs, roles, completion states, and report paths",
        r"Establish a theory-authority hierarchy before drafting",
        r"Build the Reception Profile from documented acts before inferring the resulting Horizon of Expectation",
        r"Context alone cannot prove a composer-specific horizon",
        r"Use `received as X` only when an identifiable receiver",
        r"publication or textual availability alone does not establish uptake",
    ),
    "references/dissertation-horizon-architecture.md": (
        r"Stable Analytical Functions",
        r"Theory Authority and Terminology",
        r"Project-Level Master Record",
        r"Cross-Chapter Subagent Brief",
        r"Music-specific reception theorists authorize the transfer",
        r"Interaction or response theory may constrain.*without automatically carrying the historical architecture",
        r"prior composer-in-country dissertation is an applied precedent",
        r"Reception Profile establishes observable acts; Horizon of Expectation is inferred from those acts",
        r"published interpretation establishes textual availability.*not reader uptake",
    ),
    "references/end-to-end-workflow.md": (
        r"run the capability preflight",
        r"blocked actual-subagent requirement never satisfies the reviewer gate",
        r"never substitute for an explicitly required actual-subagent review",
    ),
    "agents/openai.yaml": (
        r"route this dissertation or journal task",
        r"For reception-history dissertations",
    ),
}

FORBIDDEN = {
    "references/end-to-end-workflow.md": (
        r"reviewer gate.*(?:blocked|manual-follow-up).*notes",
        r"reviewer gate.*explicit unresolved manual items",
    ),
    "SKILL.md": (
        r"actual subagents.*(?:unavailable|failed).*(?:complete|satisf(?:y|ies)|final-ready)",
    ),
}


def validate_texts(texts: dict[str, str]) -> list[str]:
    failures = []
    for relative_path, patterns in REQUIRED.items():
        text = texts.get(relative_path)
        if text is None:
            failures.append(f"missing file: {relative_path}")
            continue
        for pattern in patterns:
            if not re.search(pattern, text, re.IGNORECASE | re.DOTALL):
                failures.append(f"{relative_path}: missing semantic guard /{pattern}/")
    for relative_path, patterns in FORBIDDEN.items():
        text = texts.get(relative_path, "")
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                failures.append(f"{relative_path}: forbidden bypass /{pattern}/")
    return failures


def self_test(texts: dict[str, str]) -> list[str]:
    failures = []
    mutations = (
        (
            "SKILL.md",
            "sequential self-review is not an equivalent substitute",
            "sequential self-review is an equivalent substitute",
            "self-review equivalence mutation",
        ),
        (
            "references/reviewer-subagent-protocol.md",
            "complete callable-tool metadata, including deferred",
            "initially displayed tool list",
            "deferred-registry removal mutation",
        ),
        (
            "references/end-to-end-workflow.md",
            "a blocked actual-subagent requirement never satisfies the reviewer gate",
            "a blocked actual-subagent requirement satisfies the reviewer gate",
            "blocked-gate bypass mutation",
        ),
        (
            "references/dissertation-chapter-workflow.md",
            "Apply this gate only when the dissertation's research problem is reception history or explicitly uses horizon of expectation across historical chapters. Do not impose it on all dissertation work.",
            "Apply this gate to all dissertation work.",
            "reception-history scope mutation",
        ),
        (
            "references/dissertation-horizon-architecture.md",
            "A prior composer-in-country dissertation is an applied precedent, operational comparison, or source map. Do not present it as the source from which the foundational theory derives.",
            "A prior composer-in-country dissertation supplies the model from which foundational theory derives.",
            "theory-authority inversion mutation",
        ),
        (
            "SKILL.md",
            "Reserve `acceptance` for demonstrated approval or adoption.",
            "Use `acceptance` as a synonym for reception.",
            "reception-acceptance collapse mutation",
        ),
        (
            "references/dissertation-horizon-architecture.md",
            "Music-specific reception theorists authorize the transfer from literary reception aesthetics to musical works, performance, institutions, listeners, and music-cultural history.",
            "Music-specific reception theory is optional and supplies no authority for the transfer to music history.",
            "music-specific authority removal mutation",
        ),
        (
            "references/dissertation-horizon-architecture.md",
            "Interaction or response theory may constrain fixed-meaning and private-psychology claims without automatically carrying the historical architecture.",
            "Interaction or response theory automatically carries the complete historical architecture.",
            "interaction-theory overreach mutation",
        ),
        (
            "references/dissertation-horizon-architecture.md",
            "Reception Profile establishes observable acts; Horizon of Expectation is inferred from those acts; Historical Change compares the resulting and inherited horizons.",
            "Horizon of Expectation is established first; Reception Profile then confirms it; Historical Change follows the assumed horizon.",
            "inferential-order reversal mutation",
        ),
        (
            "references/dissertation-horizon-architecture.md",
            "A published interpretation establishes textual availability or an offered response position, not reader uptake.",
            "A published interpretation or visible text establishes reader uptake.",
            "textual-availability uptake mutation",
        ),
        (
            "references/dissertation-chapter-workflow.md",
            "publication or textual availability alone does not establish uptake.",
            "publication or textual availability alone establishes uptake.",
            "chapter-workflow uptake reversal mutation",
        ),
        (
            "references/dissertation-chapter-workflow.md",
            "Build the Reception Profile from documented acts before inferring the resulting Horizon of Expectation and any Historical Change.",
            "Infer the resulting Horizon of Expectation before building the Reception Profile from documented acts.",
            "chapter-workflow inferential-order reversal mutation",
        ),
    )
    for path, old, new, label in mutations:
        if old not in texts[path]:
            failures.append(f"self-test setup failed: {label}")
            continue
        mutated = dict(texts)
        mutated[path] = mutated[path].replace(old, new, 1)
        if not validate_texts(mutated):
            failures.append(f"self-test false negative: {label}")
    return failures


def main() -> int:
    paths = set(REQUIRED) | set(FORBIDDEN)
    texts = {
        relative_path: (ROOT / relative_path).read_text(encoding="utf-8")
        for relative_path in paths
        if (ROOT / relative_path).is_file()
    }
    failures = validate_texts(texts) + self_test(texts)
    if failures:
        print("Workflow guard validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    count = sum(map(len, REQUIRED.values())) + sum(map(len, FORBIDDEN.values()))
    print(f"Workflow guards valid: {count} semantic checks and 12 mutation tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

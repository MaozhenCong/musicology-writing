# Agent Portability

Use this reference when publishing the skill on GitHub or handing it to another agent.

## Repository Layout

Keep this folder intact:

```text
musicology-writing/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── agent-portability.md
    ├── case-patterns.md
    ├── dissertation-chapter-workflow.md
    ├── end-to-end-workflow.md
    ├── evidence-citation-zotero.md
    ├── journal-article-workflow.md
    ├── journal-thesis-adaptation.md
    ├── reviewer-subagent-protocol.md
    ├── writing-quality-style.md
    ├── withdraw-resubmit.md
    └── templates.md
```

For a GitHub repository, either place this folder at the repository root or inside a top-level `skills/` directory. Keep the folder name exactly `musicology-writing`.

## Generic Agent Instruction

If an agent does not support automatic skill loading, paste or point it to this instruction:

```text
Use the skill folder `musicology-writing`. Read `SKILL.md` first. Then load only the reference files needed for the current phase. Follow the no-fabrication, exact-citation, source-matrix, writing-quality, reviewer-pass, and final-package rules. Do not rely on local memories or private paths.
```

## Codex / OpenAI Agents

Codex-compatible agents should detect the skill through `SKILL.md`. The optional `agents/openai.yaml` file provides UI metadata only; it is not required for the workflow itself.

## Claude, Gemini, or Other Agents

Ask the agent to:

1. read `SKILL.md`;
2. identify the current phase;
3. read only the relevant reference files;
4. keep project-specific notes in the user's workspace, not inside the skill folder;
5. report assumptions, unresolved evidence, and files changed.

## What Not to Put in the GitHub Skill

Do not include:

- private Zotero database files;
- copyrighted PDFs;
- unpublished manuscripts unless intentionally public;
- personal email records;
- local absolute paths;
- private memory summaries;
- journal login credentials or OJS session data.

Keep those in the working project, not in the reusable skill.

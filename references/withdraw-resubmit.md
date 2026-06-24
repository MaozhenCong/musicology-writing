# Withdraw Submission and Resubmit

Use this reference when the user wants to withdraw a submitted manuscript from a journal (cancel-subscription) and optionally resubmit elsewhere.

## When to Withdraw

Legitimate reasons for withdrawal:

1. **Discovery of a critical error**: data mistake, misattributed source, fabricated-looking citation, or methodological flaw that cannot be fixed in revision.
2. **Scope mismatch discovered post-submission**: the article makes claims the evidence cannot support, and the fix requires structural rewriting beyond what the journal would accept.
3. **Irreconcilable requirement change**: a new journal policy, APC, or format demand that the author cannot meet.
4. **Excessive delay**: the journal has exceeded its stated review timeline by an unreasonable margin with no communication.
5. **Simultaneous submission discovered**: an accidental overlap with another submission lane that creates an ethical conflict.
6. **Better target identified**: a more suitable journal is available and the current submission has not yet entered review.

Not legitimate reasons (pause and reconsider):

- Impatience during normal review timelines (2–6 months is common in musicology/music education).
- One harsh reviewer comment without attempting revision.
- Fear of rejection before a decision has been made.
- The author wants to broaden the article scope without evidence to support it.

Before initiating withdrawal, ask the user to confirm the reason. If the reason falls into the "not legitimate" list, present the concerns and suggest waiting.

## Pre-Withdrawal Checklist

Before writing the withdrawal letter:

1. **Verify the journal's withdrawal policy** from official sources: instructions for authors, submission system FAQ, editor correspondence. Some journals require a formal letter; others allow withdrawal through the OJS dashboard.
2. **Check the manuscript status**: is it "submitted," "with editor," "under review," or "revision requested"? If under review, withdrawal wastes reviewer time and may affect reputation with that editorial board.
3. **Confirm no ethical violation**: withdrawal after acceptance is strongly discouraged and may be treated as a breach.
4. **Record the current state** before changing anything: save the submission dashboard screenshot, status, submission ID, and correspondence.
5. **Save all correspondence** with the journal to date.

## Withdrawal Letter / Email Template

Adapt to the journal's preferred communication channel (OJS message, email to editor, or formal letter).

```
Subject: Withdrawal of Manuscript [Submission ID] – [Title]

Dear [Editor Name / Editorial Office],

I am writing to request the withdrawal of my manuscript
"[Full Title]" (Submission ID: [ID]),
submitted on [Submission Date].

Reason: [One honest, concise sentence. Examples:
- "I have identified a methodological issue that requires substantial revision beyond the current scope."
- "After further analysis, I believe the article's evidence base needs significant expansion before resubmission."
- "Due to unforeseen circumstances, I am unable to complete the revision within the requested timeframe."]

I apologize for any inconvenience this may cause and thank you
for your time and consideration.

Sincerely,
[Your Name]
[Affiliation]
[Contact Email]
```

Rules for the withdrawal letter:

1. Be prompt and professional. Do not negotiate, complain, or over-explain.
2. State the reason honestly but without self-damaging detail (e.g., do not write "my article is weak").
3. Do not mention the next target journal.
4. If the journal asks for confirmation, reply promptly and keep the reply.
5. Save the sent letter and any acknowledgement as project evidence.

## After Withdrawal

1. **Update project status**: mark the lane as "withdrawn" with the withdrawal date, reason, and acknowledgement evidence.
2. **Save all files**: freeze the submitted manuscript version, withdrawal letter, acknowledgement, and dashboard screenshot.
3. **Review what went wrong**: was the article submitted too early? Was the target journal a poor fit? Was the evidence base incomplete?
4. **Decide next action**: revise for a new target, merge into another project, or archive.

## Resubmission to a New Target

Do not simply resend the same manuscript. Before resubmitting:

1. **Run a fresh target-fit check** against the new journal's requirements (see `references/journal-thesis-adaptation.md`).
2. **Check similarity risk**: the withdrawn manuscript may have been logged in a similarity detection system. Rewrite overlapping passages, restructure sections, and update the vocabulary to avoid self-plagiarism flags.
3. **Address the reason for withdrawal**: if the withdrawal was due to a methodological issue, fix it. If due to scope, adjust the claims.
4. **Re-run the reviewer pass** (see `references/reviewer-subagent-protocol.md`) against the new target requirements.
5. **Generate new submission materials**: cover letter, declarations, metadata for the new journal.
6. **Create a new project lane**: do not reuse the withdrawn lane's status file. Start a fresh record for the new target.

## State Management Template

Keep this record in the project status file:

```markdown
## Submission Lane: [Journal Name]

- **Status**: withdrawn
- **Submission date**: [date]
- **Submission ID**: [ID]
- **Withdrawal date**: [date]
- **Withdrawal reason**: [one-line reason]
- **Acknowledgement received**: yes / no, [date], [evidence path]
- **Frozen manuscript**: [file path]
- **Withdrawal letter**: [file path]
- **Post-withdrawal plan**: revise for [new target] / merge into [project] / archive
- **New target**: [journal name] or "not yet decided"
- **Resubmission constraints**: [similarity risk notes, required fixes before resubmission]
```

## Quick Command Flow

When the user says `/cancel-subscription` or equivalent:

1. Ask which submission lane (if multiple projects exist).
2. Confirm the reason for withdrawal against the legitimate/not-legitimate list above.
3. If reason is valid, proceed to pre-withdrawal checklist.
4. Draft the withdrawal letter using the template.
5. After user approval, send and record.
6. Update project status.
7. If resubmission is planned, present the resubmission checklist.
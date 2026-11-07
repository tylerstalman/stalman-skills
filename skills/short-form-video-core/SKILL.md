---
name: short-form-video-core
description: Shared editing, authenticity, visual timing and quality principles for Tyler's short-form clips. Use with the selected podcast or main-YouTube clipping skill; contains no channel branding or editor defaults.
---

# Shared short-form editing principles

Select the destination channel before loading a brand profile or generating graphics. Use `edit-tyler-social-clips` for Full Stack Creator podcast clips and `clip-tyler-youtube` for Tyler's main YouTube channel. A guest, source app or topic does not determine the destination brand. If the destination is unclear, prepare source analysis and clarify before styling or publishing.

## Shared craft

- Build a standalone story with a clear subject, complete argument and payoff. Preserve qualifications, demonstrations, and the person's meaning. Remove genuine repetition and abandoned fragments; a transcript alone cannot prove a seamless audible join.
- Evaluate the actual picture as well as the words. Prefer existing relevant demonstration footage and B-roll; preserve actions and their results. A vertical crop must show the object/control being explained, not automatically center the face.
- Never alter eye contact. Verify product identity, generation and official short name. Read [video authenticity](references/video-authenticity.md) for inherited/baked effects and exact naming checks. These apply in every editor and channel.
- Add as many useful visuals as the discussion supports. Each insert must explain the current spoken reference and use factual, authentic source material. Read [visual production](references/visual-production.md) when adding graphics, screenshots or motion.
- Prioritize the first five seconds as the opportunity to earn continued watching. Cut to relevant available visuals as early as the spoken context supports, ideally within those opening seconds; use the earliest meaningful mention rather than waiting for a later explanation or comparison. Do not force unrelated imagery or sacrifice comprehension and readable viewing time. Review the opening separately for an earlier useful visual opportunity.
- Review the final composite for stray frames, exposed edges, sync, clipped speech, readable text, and correct handoffs. Check the actual current render; separate sampled visual checks, full visual playback, audible review, and app/platform verification. Report incomplete checks accurately.

## Scope and learning

Store general lessons here once. Store branding, hook/caption style, accounts, narrative defaults and recurring editorial direction in the destination channel skill. Keep source-specific directions and temporary experiments in that video's local job file. Explicit current directions override that channel's defaults; they do not silently change the other channel. General authenticity requirements still apply.

Record each correction with its scope (`shared`, channel id, or job), Tyler's actual direction, evidence and status (`confirmed` or `proposed`). Promote confirmed general lessons to this core; promote confirmed channel preferences only to that channel. Assistant recommendations and one video's exception are not universal user preferences.

## Efficient execution

Cache a source transcript and word timings once against a stable source/revision. Search it locally and retrieve relevant passages rather than re-transcribing or loading full histories. Keep an editor-independent, frame-based clip plan; [the job contract](references/clip-job.schema.json) records source identity, selected ranges, destination brand and revision. Source frame positions and output positions must remain distinct. Read only the selected channel, relevant tool guidance and needed evidence.

Validate job/clip/insert channel IDs agree, source ranges are within the actual media, end frames exceed start frames, and inserted output ranges follow the assembled timeline. A schema alone cannot prove those relationships. Brand status `reference-needed` permits analysis/rough assembly, not a newly styled final delivery.

Use scripts and reusable templates for repeated mechanical work, then inspect rendered results. No fixed token-saving claim: measure intervention and failure rates on a representative clip. Claude supplies occasional big-picture direction and strategic reviews; Codex executes routine edits, sourcing, animation, troubleshooting and QA without consulting Claude on every decision.

Keep private transcripts, source paths, media, account IDs and episode schedules in local job storage. The shared Git repository contains reusable instructions, schemas and approved non-sensitive templates. Pin each job to the skill commit and channel-profile version; applying an update must not silently restyle an in-progress or approved clip. Publishing remains a separate authorized workflow.

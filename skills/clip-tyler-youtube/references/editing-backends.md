# Main-channel clipping backend

Decision recorded 2026-11-07. These are workflow recommendations, not measured token/quality results.

|Source/task|Preferred path|Why / practical limit|
|---|---|---|
|Current editable Final Cut video; needs original angles, overhead footage, isolated audio or changed layers|Final Cut using existing long-form editing guidance; use a recoverable XML backup for substantial changes|Retains source relationships and Tyler's ability to continue editing. Avoid rebuilding the whole video in Resolve merely because scripting exists.|
|Approved finished master; repeated short selections, static or simple keyframed portrait framing and reusable graphics|Pilot Resolve through MCP/scripted timeline assembly, native Fusion/title templates and render presets|The available API exposes media import, frame-range timeline assembly, item properties, transcription/subtitles, Fusion and rendering. Automation can reduce repetitive UI work; required caption/style/keyframe operations still need validation.|
|Simple finished-master trim with an already approved layout|Small deterministic media render may suffice|Preserve quality, color metadata and meaningful editable outputs. This is an optional implementation path, not a new default dependency or a reason to flatten complex work.|

## Pilot before committing a batch

Use one representative supplied video: include a face, a detailed demonstration/B-roll and one speech-timed factual insert. Verify linked media, exact boundaries, color/HDR handling, crop, caption styling/editability, real-time playback and final render. Measure interventions, retries and wall time; compare with the existing Final Cut path before claiming reduced token use. Do not render the same clip in both apps routinely. No sample source is selected by this skill.

Resolve discovery for the connected Studio 21.2 API confirmed `ImportMedia`, `AppendToTimeline` with source/record frame mapping, `CreateEmptyTimeline`, FCPXML/OTIO timeline import, `CreateSubtitlesFromAudio`, and render settings/jobs. This is documentation-level capability verification, not a successful live import or an assertion that every UI function is scriptable. Inspect the current API for the exact operation. A method to generate subtitles does not establish access to all caption styling or word-level animation. Prefer a verified editable Fusion/title template or a one-time native setup when appropriate; never imply arbitrary caption styles are covered automatically.

Final Cut supports XML interchange, but conversion may not preserve every effect, title, grade, audio treatment or plugin. Keep one chosen native timeline authoritative. Interchange is a planned handoff with verification, not continuous two-way synchronization of edits. Preserve the original project/master and verify import/media/timing/effects in the receiving editor.

Token discipline: inspect source metadata once; cache transcript/word timings and content hashes; select topics once into the local job contract; retrieve only relevant words; apply batched mechanical operations; use screenshots and manual UI for visual judgment and unsupported controls. Record effective output/source frame mappings and rerun only changed outputs. Text-level planning is never a substitute for playback QA.

Primary references: [Apple XML workflow](https://support.apple.com/guide/final-cut-pro/use-xml-to-transfer-projects-verdbd66ae/mac), [Blackmagic Fusion scripting and motion](https://www.blackmagicdesign.com/products/davinciresolve/fusion). Current connected API stubs are authoritative for the actual MCP operations. No production editor state was changed to produce this recommendation.

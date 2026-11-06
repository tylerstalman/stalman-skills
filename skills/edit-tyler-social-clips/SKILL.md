---
name: edit-tyler-social-clips
description: Create and review Tyler Stalman's short-form podcast clips in Riverside, including topic selection, narrative cleanup, descriptive hooks, vertical layouts, listener cutaways, and audio cleanup.
---

# Tyler's podcast social clips

These confirmed short-form preferences override conflicting full-episode defaults for short clips. Keep full-episode and multicam skills intact. Use current Riverside tools and their editing guidance for supported operations, revision handling, and exact transcript selections.

Use this complete workflow for short-form podcast editing requests, including when Tyler identifies a specific passage rather than asking for topic discovery. Use the applicable Riverside skills for tool mechanics alongside these editorial preferences. Do not publish or schedule without a separate instruction.

## Topic discovery and selection

- Build a detailed, fairly long list of topics. Look at each topic's beginning as a promising entry point because it often gives new audiences context.
- Prefer interesting moments when a useful ranking method is available. A clear takeaway, surprise, useful advice, distinctive opinion, or engaging exchange are editorial heuristics, not reliable predictions of performance.
- For additional clips inspect existing clips when possible to avoid repeating selections.

## Opening and narrative

- Make the subject clear in the first few spoken seconds. Trim opening filler such as “so,” “like,” or “um” without clipping meaningful words.
- Aim for one to two minutes; material for a complete clip may span five minutes or more. Both are estimates, not rigid limits.
- Actively remove tangents, irrelevant detours, and repetition. Preserve a coherent beginning, middle, end and real takeaway, the speakers' intended meaning, necessary qualifications, and natural continuity.
- Seek opportunities for both speakers to contribute and respond when that improves the clip. Single-speaker clips are acceptable; don't force a second speaker.

## Opening text hook

Every clip opens with one short sentence of three to seven words about that clip, not the whole episode. Questions and statements are acceptable. Be descriptive, accurate, and explicit about the topic. Avoid clickbait, exaggeration, or promises the discussion does not fulfill.

Use **Staatliches**, uppercase black text on solid white rectangular boxes, centered horizontally. Use tight, readable line spacing and short lines; wrap into stacked white strips as needed. The [font-panel reference](assets/hook-font-panel.png) confirms Staatliches and size 88. Riverside's Speaker preset is a starting point only: inspect its font, colors, and box effect instead of assuming the preset matches.

Choose the placement from the actual picture:

- **Top:** place the hook above the eyes, as in the [top-layout reference](assets/hook-top-layout.png). It may overlap hair, but must keep eyes clear.
- **Middle:** place the hook below the eyes around the lower face/upper chest, as in the [middle-layout reference](assets/hook-middle-layout.png), when top placement would obscure eyes or leave insufficient room. On two-person split screen, the seam between angles may work well.

The middle-layout image demonstrates placement only; its different font does not override Staatliches. Keep the hook separate from dialogue captions and clear of platform overlays. Check every shot visible while the hook is on screen: a position that clears one person's eyes may cover another's after a camera switch. Adjust placement or timing accordingly. Verify the rendered appearance before claiming a visual match; saved settings alone do not establish eye clearance or legibility.

### Riverside reference settings

The [approved touchscreen reference](https://riverside.com/editor/87cab4f4-d876-4e2c-820e-faed7ffcd719/6aeca041f693295f0400ec65/preview), hook at revision 65, uses a 360 × 640 canvas: Staatliches, size 88, centered, text effect `BackgroundInvert`, primary color `#FFFFFF`, secondary color `#000000`, anchor `(0.5, 0)`, position `(0.5, 0.14223)`, and two lines. Match the rendered black-on-white result rather than interpreting the primary color as text color. The [earlier visual reference](assets/approved-hook-reference.jpg) shows the same condensed uppercase black-on-white style.

Size 88 is the Riverside reference setting, not a portable pixel size. Do not blindly reuse its vertical position: choose top or middle from the visible eye line. Preserve the visual appearance across canvas sizes. The reference's source-timeline duration is `21197/1500` seconds and spans cuts; determine visible duration on the playable timeline instead of assuming that source duration is the viewing duration. Hook duration and exact margins are editorial choices, not confirmed fixed defaults. Read current tool guidance for placement and time-axis rules.

## Visual format and camera rhythm

- Use 9:16 vertical video and Riverside Smart layout with cutaways. Verify available controls and actual connector mappings before choosing specific values.
- Seek at least a couple of angle changes per clip, including when one person speaks. Show participants and natural listening reactions where appropriate; keep switches restrained and motivated. Use reactions from the actual moment, not unrelated moments.
- In stacked layouts put Tyler at the top, David at the bottom, and a guest in the middle. Check framing, participant placement, and opening text in the actual vertical composition.

### Animation timing and reading time

Time graphic entrances, spec reveals, and exits to the relevant spoken reference or editorial beat. Keep motion brief and purposeful, then hold the graphic still long enough to comfortably read every item at phone size. Count reading time after the entrance and final text reveal finish, before the exit begins; animation time is not reading time. Judge the hold from the actual copy and density rather than a fixed duration. If it feels rushed, extend the hold within the relevant passage or simplify/stagger the information. Check the playable timeline across cuts and review the entrance, readable hold, and exit in playback before calling the timing verified.

## Riverside audio and pacing

- For new clips, enable all five Riverside AI tools: Remove Pauses, Remove Filler Words, Magic Audio for every speaker, Smart Mute, and Smart Layouts with cutaways. These are part of the default workflow; do not leave them for Tyler to turn on manually. Favor stronger cleanup for short form. Exact strength labels and connector values remain to be verified; Tyler approved stronger cleanup without specifying an enum. These choices override different or unresolved full-episode settings.
- When revising an existing edit, inspect its latest state and preserve Tyler’s manual AI settings, cleanup, and layouts. Do not rerun cleanup or regenerate Smart Layouts merely to satisfy the defaults when Tyler has already configured them.
- Review cleanup for clipped speech, unnatural joins, lost meaning, unwanted fragments, continuity, and synchronization.

## Review

Check the opening establishes the subject cleanly; the edited story has a coherent beginning, middle, end and payoff; and the hook accurately describes the clip and follows the saved styling. Check camera variety, natural reactions, vertical framing, participant positions, audio continuity and sync. Report checks that could not actually be completed; inspecting settings alone is not a full audiovisual review.

## Review delivery

Tell Tyler to review clips in the **Riverside app** by default. Identify the studio, project, and exact edit title so he can find the current version. Do not use editor/guest-review browser URLs as the default review handoff, and do not create external review uploads, links, or downloadable preview files unless Tyler explicitly requests them. Keep the review on the same existing edit so revisions remain easy to find. Rendering for an authorized final export or publication is separate from creating an extra review preview.

### Preview cleanup

Delete temporary review files and hosted preview copies once Tyler has finished reviewing them or they have been superseded and are no longer needed. Keep the current preview while review or publication approval is pending. Track the exact preview files and links created for the task so cleanup removes only those copies; preserve original media, the editable Riverside timeline, final deliverables, and published posts. Use the destination’s normal recoverable deletion when available and verify cleanup. If permanent deletion requires confirmation, request it for the exact preview rather than silently retaining it or deleting unrelated content.

## Default captions

Tyler chose the Riverside favorite shown in [caption reference](assets/caption-favorite.png) as the default caption style. It shows bold white centered text with a dark shadow, one word in the sample. Riverside reports a custom Montserrat 800, white, word-by-word Shadow/Reveal preset (id `69d328f8bcd9b3e242bb17ad`) that appears consistent; verify it is the pictured favorite in the editor before assuming the match. Preserve the distinct opening hook style above.

## Social descriptions

Write from the show's perspective. Generally omit host names; if a host is named, use their first name. Use a guest's full name when naming them. Publishing and reposting require the applicable platform workflow and user authorization.

## Maintaining this skill

The GitHub repository is the shared source of truth. Update this same skill incrementally as Tyler adds guidance, distinguishing confirmed preferences from unresolved choices. Commit and push changes, then pull them on the other computer; do not maintain divergent installed copies. Do not claim cloud or ChatGPT installation without verification. Keep episode-specific requests in their chats rather than in this reusable skill.

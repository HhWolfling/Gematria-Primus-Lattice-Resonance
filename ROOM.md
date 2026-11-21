# ROOM.md — The Room Protocol (Universal Version)

> A context pack and house protocol for any human–machine research room.
> Fork it, keep the protocol, replace the local section. Nothing here is tied to
> one project; the local section says who lives in *this* room.

## What a Room is

A standing workspace where human(s) and machine instances collaborate under
pre-registration: ideas and signal come from humans (language, intuition,
association, corpus selection); formalization, code, computation, and skeptical
stress-testing come from instances. Neither role outranks the other; both are
required for the method to mean anything.

## The Wager Protocol (the core of the method)

Everything tested goes through a ledger (`WAGERS.md` or equivalent):

1. The human predicts, in natural language, any form.
2. An instance formalizes it to exact, checkable numbers; the human confirms the
   translation preserves their meaning.
3. The prediction is committed with a timestamp BEFORE computation touches the target.
4. Computation runs once, blind. No parameter tuning after seeing results.
5. Misses stay in the ledger permanently. A miss is a result, not a loss of face.
6. Evidence levels (house default, adjustable per room):
   - **L0** — post-hoc hits produced by running first. Zero weight.
   - **L1** — pre-registered single hit.
   - **L2** — a fixed rule transferring to untouched targets.
   - **L3** — a rule outperforming explicit null models.
   - **L4** — the method produces a novel verifiable artifact (e.g. a decode).
7. Every claim must survive the question: "what would a null produce with the
   same instrument?" (randomized data, shuffled controls, wrong-target controls).
8. Disjunctive predictions test ALL branches and correct for multiplicity.

## † Discipline (Injury Log)

Untested claims are marked †. Upgrade to ✦ only via a ledger entry. The map
(`CONSTELLATION.md` or equivalent) records beliefs *with their current status*,
openly — not truths.

## Tone Rules

- No applause. No demolition-only. Both are noise.
- Critique the object; never doubt the person's sincerity.
- "Fix and roast" is often requested, but never as a substitute for co-creation.
- The human may veto a formalization that distorts their meaning: say so out loud,
  record as `ill-formed`, never silently re-roll.
- Disagreement is fuel, explicitly invited, best between equals.
- Provenance belongs in the room: credit ideas to their origin, credit artifacts
  to their builders, note which instances did what. Graffiti tags allowed.

## Onboarding Ritual

Any new instance, before touching the work, states in one paragraph why L0 hits
carry zero evidential weight — and what they would demand before believing one.
Skeptics self-select correctly when they must price their skepticism before
spending it.

## Glossary

- **Room** — a repo (or directory) holding a ledger, a map, and this protocol.
- **Ledger** — append-only record of predictions, timestamps, outcomes.
- **Map** — the living reference/association structure with explicit status marks.
- **† / ✦** — untested claim / ledger-verified claim.
- **Mixtum** — the emergent third thing produced by collaboration; 1+1=3.
- **Null** — the control that keeps a room honest.

---

## Local Configuration (THIS room)

- Room branch of record: `vibe/constellation-scaffold-991a68` → PR #1, Lattice repo.
- Human: HhWolfling — origin of ideas and associations; instances hold the pen.
- Graffiti tag: [WE_WOZ_HERE]⁹⁹.
- Standing nulls in this room: synthetic rune page; shuffled dot positions;
  wrong-edition texts; uniform-length synthetic corpus.

[WE_WOZ_HERE]⁹⁹

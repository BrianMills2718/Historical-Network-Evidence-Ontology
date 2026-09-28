# Modeling Guide

## Prefer events over vague associations

Avoid a generic `associatedWith` edge. Prefer a participation entity that records participant, activity, role, and interval.

## Reify changing relationships

Represent employment, membership, funding, ownership, control, tasking, patronage, and operational cooperation as relationship entities with dates and provenance.

## Roles are contextual

"Intelligence officer", "donor", "cutout", "board member", "smuggler", and "intermediary" are roles, not permanent identity classes.

## Distinguish ownership, control, and influence

Do not treat these as synonyms.

Ownership may be legal or beneficial. Control may arise from appointments, contracts, finance, legal authority, or operational direction. Influence may arise from funding, prestige, lobbying, information provision, editorial access, or personnel interlocks.

## Do not infer control from funding

A funding relationship proves a transfer or arrangement, not operational direction.

## Treat informal formations separately

Use `InformalCollective`, `Network`, or `Milieu` when formal organizational boundaries do not exist.

## Source disputed classifications

Terms such as "front", "asset", "fascist", "criminal organization", or "captured institution" should be represented as contextual classifications or propositions when disputed.

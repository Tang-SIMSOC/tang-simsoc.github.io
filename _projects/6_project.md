---
layout: page
title: "MOBEP: Opinion-Behavior Co-evolution Framework"
description: A unifying framework for building and comparing models of opinion polarization
img: assets/img/mobep-framework.png
importance: 2
category: past
---

**Opinions and behaviors evolve together.** People act partly on what they
believe, observe what others do, infer the opinions behind those actions, and
adjust their own views. Yet these feedbacks have often been modeled in
isolation, making it difficult to compare models or accumulate their insights.

MOBEP (**M**odeling **O**pinion-**B**ehavior Co-evolution for **E**xplaining
Opinion **P**olarization) provides a shared architecture for studying these
processes. The framework connects opinion change, behavior change, social
inference, network structure, scheduling, and polarization measurement in one
modeling language.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <figure>
      <img
        src="{{ '/assets/img/mobep-framework.png' | relative_url }}"
        alt="Structure of the MOBEP framework, linking opinions, behaviors, social influence, scheduling, and polarization measurement"
        class="img-fluid rounded z-depth-1"
      >
      <figcaption class="caption">
        Structure of the MOBEP framework. Reproduced from Chapter 5 of my
        doctoral dissertation.
      </figcaption>
    </figure>
  </div>
</div>

## How the framework works

MOBEP distinguishes two complementary routes of social influence:

- **Direct opinion dynamics:** people communicate opinions, allowing others'
  opinions to influence their own directly.
- **Behavior dynamics:** opinions shape behavior; people observe others'
  behavior, infer the opinions behind it, and update their own opinions.
  Normative influence can also make observed behavior affect one's behavior
  directly.

These processes are embedded in a network or partner-selection mechanism and
connected to two practical modeling choices: the schedule governing when
events occur and the measurement used to assess polarization.

## Why MOBEP matters

MOBEP serves both as an **organizing framework** and a **model-building
template**. Researchers can use it to:

- reveal which mechanisms an existing model includes or omits;
- compare models expressed in otherwise incompatible terminology;
- design new opinion-behavior models systematically; and
- connect micro-level mechanisms to macro-level polarization measurements.

The chapter demonstrates these uses by mapping several established models onto
MOBEP and by constructing a case study of mask-wearing behavior during the
COVID-19 pandemic.

## Credits

- Tanzhe Tang
- [Amineh Ghorbani](https://www.tudelft.nl/staff/a.ghorbani/)
- [Caspar Chorus](https://www.tudelft.nl/io/over-io/personen/chorus-c-g)

## More information

- Read the standalone [MOBEP thesis chapter](/research/mobep-thesis-chapter/).
- View the [complete doctoral dissertation](https://doi.org/10.4233/uuid:b4b02f3b-b622-4226-8f8c-be26e2c52428).

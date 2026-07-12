---
layout: page
title: Software
permalink: /software/
description: Software packages and research tools.
nav: true
nav_order: 5
---

<style>
  .software-list {
    margin-top: 1.5rem;
  }

  .software-item {
    display: grid;
    grid-template-columns: 120px minmax(0, 1fr);
    gap: 1.25rem;
    align-items: start;
    margin-bottom: 2.25rem;
  }

  .software-thumb {
    width: 110px;
    height: 110px;
    object-fit: contain;
  }

  .software-item h3 {
    margin-top: 0;
    margin-bottom: 0.5rem;
  }

  .software-links {
    margin-top: 0.75rem;
  }

  @media (max-width: 576px) {
    .software-item {
      grid-template-columns: 80px minmax(0, 1fr);
      gap: 1rem;
    }

    .software-thumb {
      width: 72px;
      height: 72px;
    }
  }
</style>

<div class="software-list">
  <h2>Packages</h2>

  <div class="software-item">
    <img class="software-thumb" src="{{ '/assets/img/esbg-logo.svg' | relative_url }}" alt="esbg logo">
    <div>
      <h3>esbg</h3>
      <p>
        An R package for applying Equal-Size Binary Grouping (ESBG), a group-based approach for measuring bipolarization without predefined group structures. The package is currently available from GitHub.
      </p>
      <p class="software-links">
        [<a href="https://github.com/Tang-SIMSOC/esbg#readme">README</a>]
        [<a href="https://github.com/Tang-SIMSOC/esbg">code</a>]
        [<a href="https://link.springer.com/article/10.1007/s11135-021-01271-y">paper</a>]
      </p>
    </div>
  </div>

  <h2>Simulation Models</h2>

  <div class="software-item">
    <img class="software-thumb" src="{{ '/assets/img/gerrysort-logo.png' | relative_url }}" alt="GerrySort logo">
    <div>
      <h3>GerrySort</h3>
      <p>
        A Python-based agent-based model for studying the interaction between partisan gerrymandering and geographical partisan sorting in U.S. congressional elections. The model combines redistricting processes with voter relocation dynamics and can be run through either a command-line workflow or an interactive visualization interface.
      </p>
      <p class="software-links">
        [<a href="https://github.com/aM0NKE/GerrySort-ABM#readme">README</a>]
        [<a href="https://github.com/aM0NKE/GerrySort-ABM">code</a>]
      </p>
    </div>
  </div>

  <div class="software-item">
    <img class="software-thumb" src="{{ '/assets/img/socrates-logo.png' | relative_url }}" alt="SOCRATES logo">
    <div>
      <h3>SOCRATES</h3>
      <p>
        SOCial Routing AgenTs Evolutionnary Simulation (SOCRATES) is a Java multi-agent simulator developed within the ERC BEHAVE project to study how social routing affects the efficiency of transportation infrastructures.
      </p>
      <p class="software-links">
        [<a href="https://www.nicolascointe.eu/projects/#socrates">project info</a>]
      </p>
    </div>
  </div>
</div>

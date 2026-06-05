---
layout: page
title: GerrySort--Gerrymandering and Partisan Sorting
description: An Empirical Agent-Based Model for Simulating Gerrymandering and Geographical Partisan Sorting
img:
importance: 1
category: ongoing
---

**Gerrymandering** is a classic topic for both scholars and the public. The strange-looking boundaries are often associated with partisan unfairness, uncompetitive elections, and maps of low compactness. 

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <figure>
            <img src="/assets/img/The_Gerry-Mander_Edit.jpg" alt="Gerrymander" class="img-fluid rounded z-depth-1">
            <figcaption class="caption">
                Original cartoon of "The Gerry-Mander" (the Figure comes from <a href="https://en.wikipedia.org/wiki/Gerrymandering#/media/File:The_Gerry-Mander_Edit.png" target="_blank">here</a>).
            </figcaption>
        </figure>
    </div>
</div>

However, evaluating the real-life impact of gerrymandering—or more generally, redistricting strategies—requires more than just analyzing gerrymandering itself with static maps; it requires taking into account how voters react to the new map over time. When voters are unhappy with the redistricting, they may relocate, thereby canceling out the impact of gerrymandering. This process is called **partisan sorting**. I am working on **GerrySort**, an empirically calibrated agent-based model that allows users to explore the complex interplay between gerrymandering and partisan sorting, as well as their collective impacts on the district map. It has the following features and usages:

### Features:
* Integrates **gerrymandering** and **partisan sorting** into one ABM
* Calibrates the ABM using real-world **precinct-level election data** and **county-level demographics**
* Implements multiple **redistricting scenarios**, including fixed control, model-determined control, and fairness-maximizing redistricting
* Analyzes maps and evaluates redistricting reforms using multiple metrics for partisan fairness, compactness, competitiveness, and segregation

### Use Cases:
* Evaluate how partisan sorting affects gerrymandering outcomes and vice versa
* Generate congressional district maps under different political control scenarios using advanced algorithms
* Assess the effectiveness of redistricting reforms under different political geographies in multiple U.S. states
* Measure partisan segregation of the maps using spatial statistics (e.g., Moran’s I)

### Credits:
* River Vaudrin
* Tanzhe Tang
* [Mike Lees](https://www.mhlees.com)

### Data, Codes, and More Info:
* Please visit the [GitHub page for the project](https://github.com/aM0NKE/GerrySort-ABM).
---
layout: page
title: Measuring Polarization Using Clustering Techniques
description: A Group-based Polarization Measurement
importance: 1
img: assets/img/esbg-kmeans.png
category: past
---

From scholars to the media, everyone talks about **polarization** and its consequences with a large amount of data to endorse their arguments, but few know how to (properly) measure polarization. The largest obstacle lies in the discrepancy between how polarization is conceptualized and measured: definitions of polarization rely on the notion of a **group** identified based on (pairwise) similarities, but this notion is usually neglected when measuring polarization. 

To address the discrepancy, we present a group-based polarization measurement based on a clustering method called *Equal Size Binary Grouping* (ESBG) for both uni- and multi-dimensional data. ESBG divides the population into two groups of equal sizes based on similarities between individuals. It can be viewed as a size-constrained version of K-means clustering (K=2), and the corresponding polarization measurement is a function of the between-group and within-group dissimilarity. The measurement has the following properties:

* Increases with the dissimilarity between groups 
* Decreases with the dissimilarity within groups 

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <figure>
            <img src="/assets/img/esbg-kmeans.png" alt="ESBG and K-means Illustrations" class="img-fluid rounded z-depth-1">
        </figure>
    </div>
</div>
<div class="caption">
    Illustrations of ESBG (left) and K-means (right) (The Figures come from <a href="https://link.springer.com/article/10.1007/s11135-021-01271-y/figures/11" target="_blank">here</a>).
</div>

### Credits:
* Tanzhe Tang
* [Amineh Ghorbani](https://www.tudelft.nl/staff/a.ghorbani/)
* [Flaminio Squazzoni](https://www.unimi.it/en/ugov/person/flaminio-squazzoni)
* [Caspar Chorus](https://www.tudelft.nl/io/over-io/personen/chorus-c-g)

### Funding:
This project has received funding from the European Research Council: Consolidator Grant BEHAVE (Grant Agreement No. 724431).

### More Info:
* The paper of the project has been [published in *Quality and Quantity*](https://link.springer.com/article/10.1007/s11135-021-01271-y).
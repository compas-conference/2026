---
layout: page
#
# Content
#
title: ""
teaser: ""
header:
    image_fullwidth: "bordeaux-small.jpeg"
    permalink: "/"
---


## **Présentations plénières**

### Laura Grigori

Mercredi 25 juin

**Solving large scale problems through randomization**

In this talk we discuss recent progress in using randomization for solving
large scale linear algebra problems as solving linear systems of equations or
eigenvalue problems. We discuss first sketching techniques that allow to embed
large dimensional subspaces while preserving geometrical properties and their
parallel implementations. We then present randomized versions of processes for
orthogonalizing a set of vectors and their usage in the Arnoldi iteration.  We
discuss associated Krylov subspace methods for solving large scale linear
systems of equations and eigenvalue problems. The new methods retain the
numerical stability of classic Krylov methods while reducing communication and
being more efficient on modern massively parallel computers.

*Laura Grigori is a Full Professor in applied and computational mathematics at
EPFL and PSI and Chair of high performance Numerical algorithms and
simulations. From 2013 to 2023 she has lead Alpines group, a joint group
between INRIA and J.L. Lions Laboratory, Sorbonne University, in Paris.  She is
a SIAM Fellow, the recipient of an ERC Synergy Grant, and the recipient of the
SIAM SIAG on Supercomputing Career Prize 2024. Her field of expertise is in
numerical linear, multilinear algebra, randomized algorithms, and high
performance scientific computing for challenging applications ranging from
astrophysics to molecular simulations. For her work on communication avoiding
algorithms she was awarded with her co-authors the SIAM Siag on Supercomputing
Best Paper Prize 2016 for the most outstanding paper published in 2012-2015 in
a journal in the field of high performance computing. She was the chair of
PRACE Scientific Steering Committee, the Program Director of the SIAM special
interest group on supercomputing, January 2014 - December 2015, then the Chair
of this interest group, January 2016 - December 2017. She is currently the
chair of the SIAM interest group on numerical linear algebra.*

### Romain Rouvoy

Jeudi 26 juin

**Cloud computing: sharing is caring**

En quelques années seulement, les infrastructures de cloud computing
sont devenues le moteur du déploiement massif de services numériques
dans notre société. Ces infrastructures, qui prônent la
virtualisation, favorisent la consolidation des ressources physiques
dans des data centers de plus en plus imposants. Cependant, il reste
de nombreux défis à relever pour réduire l’empreinte environnementale
des services en ligne qu’elles hébergent. Dans cet exposé, je
présenterai les travaux que nous menons depuis plusieurs années au
sein de l’équipe Spirals pour évaluer l’efficacité de ces
infrastructures logicielles et matérielles. Au-delà des paradoxes que
soulèvent ces indicateurs, je présenterai également quelques
contributions systèmes que nous avons pu proposer au fil des ans pour
repousser les limites de la consolidation traditionnelle des
ressources, tout en évoquant leurs propres limites.

*Romain Rouvoy est Professeur des Universités au sein du Département
d’Informatique de l’Université de Lille et membre de l’équipe-projet
Spirals, associée au CRIStAL (UMR CNRS 9189) et au centre Inria de
l’Université de Lille. Ses travaux de recherche portent sur les
problématiques systèmes et génie logiciel relatives à l’impact
environnemental du numérique. En particulier, il s’attache à lutter
contre les différentes sources de gaspillage de ressources logicielles
et matérielles, même si cela implique de remettre en question le mythe
de la performance à n’importe quel prix.*

### Arthur Perais

Vendredi 27 juin

**A Day in the Life of Instruction Fetch**

Modern general purpose high performance processors can execute around ten
instructions each cycle, but can only do so when they know what instructions to
execute. As a result, significant research and engineering is spent ensuring
that the correct instructions are brought to the processor execution units fast
enough. In this talk, we will first review what the modern instruction fetch
hardware looks like, highlighting the considerable progress made since the
5-stage MIPS pipeline. Notably, so-called "datacenter" workloads and their ever
increasing instruction footprint have caused a major shift in organization in
the last decade or so. Then, we will present two techniques that accelerate
instruction delivery in specific scenarios: i) Workloads with high Instruction
Level Parallelism and ii) Workloads with hard to predict conditional branches
(e.g., sorting).

*Arthur Perais has been a CNRS researcher at TIMA in Grenoble since 2020,
working on general purpose microarchitecture techniques often based on
speculation. From 2017 to 2020, he was part of the performance modeling team at
Qualcomm Datacenter Technologies (Raleigh, US) then at Microsoft (Raleigh, US),
working on custom ARM microarchitectures. He obtained his PhD in 2015 from
Université de Rennes 1.*


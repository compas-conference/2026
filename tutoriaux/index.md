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


## **Tutoriels**

La première journée (**mardi 24 juin**) de la conférence est dédiée aux
[tutoriels](https://2025.compas-conference.fr/tutoriaux/) (cf.
[charte](https://www.compas-conference.fr/organisation/charte/)).

Cette année la conférence propose **6 tutoriels**.

Un *tutoriel* (*tutorial*) est également un évènement associé à la
conférence. Il vise à initier ou approfondir les connaissances des
participants sur un sujet spécifique. Animé par un expert ou une
équipe d'experts, il combine généralement exposés théoriques et
démonstrations pratiques, avec un objectif de formation progressive
plutôt que d’échange ou de recherche avancée. Il dure typiquement une
demi-journée (3h).

###  [Tutoriel RISC-V: Rajout de périphériques sur un cœur RISC-V CVA6](https://perso.ens-lyon.fr/nicolas.derumigny/COMPAS-Tutorial.html)

#### Organisateur
- Nicolas Derumigny (Telecom SudParis, Inria, Saclay, France)

#### Objectif

CVA6 est un projet open-source consistant en une famille
d'architecture de CPU compatibles avec le jeu d'instruction RISC-V.
Bien que le cœur soit personnalisable (versions 32 et 64-bit,
ajout/suppression d'extensions), son intégration au sein d'un design
plus complet comprenant RAM, console sur port série, disque et réseau
est un processus manuel chronophage. Dans cet atelier, nous étudierons
les différentes étapes permettant d'adapter le cœur dans sa version
Ariane à une carte de développement ZCU104 et/ou PYNQ-Z2 basée sur un
FPGA AMD. En particulier, nous rajouterons plusieurs périphériques
d'IO et de debug sur le bus commun AXI utilisé lors des accès à
l'espace d'adressage, en les reliant aux connecteurs physiques de la
carte. En parallèle des modifications du design, nous aborderons les
changements nécessaires à l'exécution correcte de Linux sur l'image de
démarrage, en particulier au niveau du device tree. Découvrir les
interactions matérielle-logicielles par le prisme du rajout de
matériel adressé directement sur un bus commun.

<!-- Logiciels : Vivado (archive fournie), Git, éditeur de texte -->

<!-- Matériel (actuellement disponible dans notre équipe) : à minima une ZCU104 (code testé et fonctionnel), éventuellement des PYNQ-Z2 suivant l'avancement du portage du CVA6 dessus. Divers module d'extensions. Cartes SD. -->

<!-- Les participants partiront d'un CVA6 nu fonctionnant à 50 MHz et -->
<!-- pourront intégrer un ou plusieurs des périphériques suivant: -->
<!-- - LED (GPIO) -->
<!-- - Bouttons (GPIO) -->
<!-- - Console (via un adaptateur PMOD / serial externe, ou en utilisant -->
<!--   une interface sur la ZCU104) -->
<!-- - Ethernet (ZCU104 uniquement) -->
<!-- - Carte SD -->

<!-- Il sera également possible de modifier la fréquence du CVA6 pour la -->
<!-- fixer à 100 MHz. -->

<!-- L'ajout de périphériques tout comme la modification de fréquence -->
<!-- passera par les étapes suivantes: -->
<!-- - rajout du module sur le design via Vivado -->
<!-- - spécification des contraintes (mapping des IO du module sur des pins -->
<!--   physiques du FPGA) -->
<!-- - modification du device tree -->
<!-- - modification de l'image de boot (pour y rajouter les pilotes) -->
<!-- - programmation du FPGA et test -->

### Tutoriel ScratchVM: Comprendre la virtualisation par la pratique

#### Organisateurs
- Yves KONE (Toulouse INP, Toulouse, France)
- Caleb FONYUY-ASHERI (Université de Rennes, Rennes, France)

#### Objectif

Les notions liées au concept de virtualisation peuvent paraître flous
pour certains. Notre atelier a pour but de démystifier cela en
proposant un tutoriel de gestion de machine virtuelle sur plateforme
Intel x86 64bits avec la technoloie Intel VT-x. L’objectif est de
comprendre le fonctionnement interne des différentes couches de
virtualisation telles que l'hyperviseur, ainsi que les OS hôtes et
invités. L'idée est d’exécuter un programme simple écrit en C dans une
micro machine virtuelle (VM) créée à l’aide du module Linux KVM et de
pouvoir ensuite migrer la VM d’une machine physique à une autre. Nous
fournissons une base de code permettant de créer une micro VM et
exécuter un programme.

Voici le programme envisagé:
- Introduction à la virtualisation:
  - étude de la base de code pour se familiariser avec KVM
  - étude de la procédure de démarrage de la machine virtuelle
- Etude du programme utilisateur:
  - compilation
  - gestion des interactions extérieures
  - modification du programme
- Migration:
  - sauvegarde et restauration de la machine virtuelle sur la même machine physique
  - sauvegarde et restauration de la machine virtuelle sur une machine différente

### [Tutoriel EZTrace: Analyse de performance d'applications parallèles avec EZTrace](https://gitlab.com/eztrace/tutorials/compas-2025)

#### Organisateur
- François Trahay (Telecom SudParis, Inria, Saclay, France)

#### Objectif

L'objectif de ce tutoriel est de tracer l'exécution d'un programme
parallèle et analyser ses performances. Nous fournirons une conteneur
docker avec les logiciels et supports nécessaires au tutoriel
(EZTrace, ViTE, etc.).

Dans un premier temps, les participants prendront en main EZTrace et
apprendront à générer des traces d'exécution de programmes MPI+OpenMP
simples. Les traces générées seront ensuite visualisées avec ViTE, et
analysées avec des outils d'analyse en ligne de commande.

Pour la deuxième partie du tutoriel, les participants analyseront une
application plus complexe. Ils devront créer un module EZTrace afin
d'instrumenter certaines fonctions, et ils modifieront l'application
en insérant des sondes à des points d'intérêt.

### [Tutoriel NixOS-Compose: Environnements distribués reproductibles avec NixOS-Compose](https://notes.inria.fr/ErKsSxuSRUWDqoBQzBGeKg)

#### Organisateurs
- Quentin Guilloteau (Univ. Lyon, Inria, CNRS, ENS de Lyon, Lyon, France);
- Millian Poquet (Univ. Toulouse, CNRS, IRIT, Toulouse, France);
- Olivier Richard (Univ. Grenoble Alpes, Inria, CNRS, LIG, Grenoble, France);

#### Objectif

Dans ce tutoriel, nous présentons aux utilisateurs NixOS Compose, un
outil basé Nix et NixOS pour générer et déployer des environnements
reproductibles sur des plateformes distribuéees. Nous présenterons
d’abord Nix et les notions nécessaires pour utiliser NixOS Compose.
Comme NixOS Compose peut cibler plusieurs plateformes, les
utilisateurs configureront leur environnement avec des conteneurs
légers (Docker) sur leurs machines locales, leur permettant d’itérer
rapidement sur la description de leur environnement. Une fois
l’environnement prêt avec les conteneurs, les utilisateurs pourront le
tester rapidement sur le banc d’essai Grid’5000 en utilisant kexec,
avant de générer un tarball de système complet et déployer avec
Kadeploy.

### [Tutoriel Guix-Org-mode: Initiation à Guix et Org-mode](https://guix-org-tutorial-compas-2025.gitlab.io/tutorial/)

#### Organisateur
- Marek Felšöci (LIP6, Sorbonne Université, Paris, France)

#### Objectif

Dans ce tutoriel, nous proposons une initiation à Guix et Org mode. Le
tutoriel abordera la gestion d'un environnement logiciel avec Guix et
la programmation lettrée avec Org mode dans le but d'améliorer la
reproductibilité d'une étude expérimentale.

À l'occasion de l'édition 2023 de Compas, moi-même et Ludovic Courtès
(Inria) avons animé un tutoriel sur Guix articulé essentiellement
autour de la reproductibilité d'un environnement logiciel
expérimental. Cette fois, il s'agira d'aborder également les
problématiques de la reproductibilité des expériences numériques ainsi
que de la conservation à long terme des éléments d'une étude
expérimentale. Je prévois de me baser sur un tutoriel donné à
[Nancy](https://tuto-techno-guix-hpc.gitlabpages.inria.fr/guidelines/guidelines.pdf).

### [Tutoriel Guix-deploy: Déployer sur les centres de calcul nationaux avec Guix](https://guix-hpc.gitlabpages.inria.fr/compas-tutorial-2025/)

#### Organisateurs
- Ludovic Courtès (Inria, Bordeaux, France)
- Romain Garbage (Inria, Bordeaux, France)
- Antoine Gicquel (Inria, Bordeaux, France)
- Gilles Marait (Inria, Bordeaux, France)
- Stojche Nakov (Inria, Bordeaux, France)
- Florent Pruvost (Inria, Bordeaux, France)

Ce tutoriel se base sur notre expérience commune en HPC, allant de
l’ingénierie du déploiement logiciel au développement de bibliothèques
scientifiques, et s’inscrit dans la suite du tutoriel proposé par
Marek Felšöci portant sur une démarche expérimentale reproductible
avec Guix et Org-Mode.

#### Objectif

Le déploiement de logiciels scientifiques sur les supercalculateurs
est une difficulté qui perdure et s’accroît avec la complexité des
piles logicielles utilisées en calcul intensif (HPC). Les solutions
les plus communément envisagées—les modules, Spack, Conda, ou des
images Singularity/Apptainer—sont souvent insatisfaisantes, notamment
parce qu’elles ne répondent pas aux besoins de reproductibilité et de
transparence de la recherche. Ce tutoriel montrera comment tirer
partie de l’outil de déploiement Guix pour rapidement déployer et
faire tourner, de manière fiable et reproductible, des codes HPC sur
des supercalculateurs tels que Adastra (CINES), Jean-Zay (IDRIS) et
Irène (TGCC).



<!-- Les tutoriels seront organisés le 2 Juillet 2024, avant la conférence pour une durée d'environ 3h00 (possibilité de demander deux créneaux pour un tutoriel de 6h sur la journée). La participation aux tutoriels est gratuite pour tous les participants à la conférence COMPAS 2024. -->

<!-- ### Objectifs -->

<!-- Les tutoriels doivent servir un ou plusieurs des objectifs suivants : -->

<!-- - Initier les novices aux principaux thèmes des différentes communautés COMPAS. -->
<!-- - Introduire des méthodes et outils à des non spécialistes dans un sous-domaine de COMPAS. -->
<!-- - Motiver et expliquer un sujet d’importance émergent. -->

<!-- Nous encourageons des tutoriels avec une composante pratique ou un autre élément interactif. -->

<!-- ### Thématiques -->

<!-- Toutes les thématiques relevant de la conférence (Architecture, Systèmes et Parallélisme) sont les bienvenues.  -->

<!-- ### Dates importantes -->

<!-- - Date limite de soumission des tutoriels : 03/06/2024 -->
<!-- - Notification auteurs et affichage tutoriels acceptés : 10/06/2024 -->
<!-- - Résumés des tutoriels et pages web : 15/06/2024 -->

<!-- ### Instructions de soumission -->

<!-- Les propositions de tutoriels doivent être soumises par email à <sebastien.pillement@univ-nantes.fr> -->

<!-- Les propositions doivent être soumises dans un seul mail contenant les informations suivantes : -->

<!-- - Une description du tutoriel en deux phrases -->
<!-- - Un déroulé détaillé du tutoriel sous forme de points -->
<!-- - Une brève caractérisation du public cible potentiel du tutoriel, y compris les connaissances pré-requises -->
<!-- - Une brève description du matériel requis. -->

<!-- Local Variables: -->
<!-- jinx-languages: "fr" -->
<!-- jinx-local-words: "tutoriel" -->
<!-- End: -->

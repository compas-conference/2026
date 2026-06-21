---
layout: page
#
# Content
#
title: "Tutoriels"
teaser: ""
header:
    image_fullwidth: "biarritz.jpg"
    permalink: "/"
---

## **Tutoriels**

La première journée (**mardi 30 juin**) de la conférence est dédiée aux tutoriels (cf. [charte](https://www.compas-conference.fr/organisation/charte/)).

Cette année la conférence propose **3 tutoriels** sur cette journée du mardi.

Un *tutoriel* (*tutorial*) est également un évènement associé à la conférence. Il vise à initier ou approfondir les connaissances des participants sur un sujet spécifique. Animé par un expert ou une équipe d'experts, il combine généralement exposés théoriques et démonstrations pratiques, avec un objectif de formation progressive plutôt que d’échange ou de recherche avancée. Il dure typiquement une demi-journée (3h).

### Tutoriel ReproHackathon - Amphi 9h-12h30

#### Organisateurs
- Jules Evans (IRIT)
- Quentin Guilloteau (INRIA)
- Millian Poquet (Univ. Toulouse)
- Miguel Felipe Silva Vasconcelos (IRIT)

#### Description du tutoriel en deux phrases
Lors de ce tutoriel, les participant·e·s essayeront de reproduire des résultats/expériences provenant d'articles scientifiques de la communauté de COMPAS.
L'objectif de l'atelier est de sensibiliser les participant·e·s aux bonnes et mauvaises pratiques expérimentales en termes de reproductibilité.

#### Déroulé de l'atelier

Nous prévoyons une session de 3 heures.

- [10 minutes] Introduction par les organisateurs des objectifs et du déroulé de l'atelier
- [5 minutes] Présentation par les organisateurs des articles proposés pour leur reproduction
- [5 minutes] Création de petits groupes (3 - 5 participant·e·s) et choix de l'article à reproduire par groupe
- [60 minutes] Travaux en groupe sur la reproduction de l'article choisit.
- [20 minutes] Pause
- [60 minutes] Travaux en groupe sur la reproduction de l'article choisit.
- [15 minutes] Préparation des restitutions par groupe (i.e., quelques transparents)
- [20 minutes] Restitution des groupes aux autres participant·e·s
- [5 minutes] Conclusion de l'atelier et résumer des points clés par les organisateurs.


#### Public cible

Cet atelier est accessible à tous les niveaux et toutes les sous-communautés de COMPAS.
L'atelier vise cependant en priorité les doctorant·e·s; car iels ont le plus à apprendre des bonnes et mauvaises pratiques en termes de reproductibilité.

Concernant les compétences requises, nous proposerons des articles des différentes sous-communautés de COMPAS afin que chacun·e ne soit pas trop dépaysé du point de vue technique.

#### Matériel requis

Une salle avec des prises électriques pour les ordinateurs des participant·e·s, ainsi qu'un vidéoprojecteur, et une bonne connexion internet.

### Tutoriel Orchestration de campagnes de benchmarks avec IOPS - Salle 124-125 9h-12h30

#### Organisateur
- Luan Teylo (Inria Bordeaux, equipe TADaaM)

#### Resume (deux phrases)
IOPS (Integrated Orchestration for Parametric Studies) est un framework open-source d'orchestration de
benchmarks qui permet d'automatiser la generation, l'execution et l'analyse d'etudes parametriques a travers
de simples fichiers de configuration YAML. Ce tutoriel propose une prise en main pratique d'IOPS, de
l'installation a la generation de rapports interactifs, en passant par la definition et l'execution de campagnes
de benchmarks avec des outils bien connus tels que IOR, STREAM et les NAS Parallel Benchmarks (NPB)
sur des environnements locaux et distribues (SLURM).

#### Deroule detaille du tutoriel
Le tutoriel est prevu pour une duree de 3 heures et sera organise en quatre parties.

##### Partie 1 : Introduction et installation
- Presentation du contexte : les defis de la reproductibilite et de l'automatisation dans les campagnes
de benchmarks
- Introduction a IOPS : motivations, architecture et fonctionnalites principales
    - Gestion parametrique automatisee et strategies de recherche (exhaustive, aleatoire,
bayesienne, adaptive)
    - Execution locale et sur clusters SLURM
    - Cache intelligent, sondes systeme et rapports HTML interactifs
- Installation d'IOPS via pip install iops-benchmark
- Presentation de l'interface en ligne de commande et de la documentation officielle :
https://iops.gitlabpages.inria.fr/

##### Partie 2 : Premiere campagne de benchmarks avec IOR
- Presentation du benchmark IOR (outil de reference pour la mesure de performances
d'entrees/sorties)
- Construction pas a pas d'un fichier de configuration YAML :
    - Definition des variables parametriques (vars) avec differents types de balayage (sweep)
    - Construction du template de commande avec Jinja2
    - Configuration du parser de resultats pour extraire les metriques (debit, latence)
    - Configuration de la sortie des resultats (output.sink)
- Execution de la campagne en mode local avec iops run config.yaml
- Utilisation de iops check, iops find et du mode --dry-run

##### Partie 3 : Campagnes avancees avec STREAM et NPB
- Campagne STREAM (mesure de bande passante memoire)
    - Etude parametrique sur le nombre de threads et la taille des tableaux
    - Demonstration du cache intelligent (--use-cache) pour eviter la reexecution de tests
identiques
- Campagne NPB (NAS Parallel Benchmarks)
    - Etude parametrique sur les noyaux de calcul (EP, CG, MG) et le nombre de processus
    - Variables derivees et contraintes pour le filtrage de combinaisons invalides
- Fonctionnalites avancees :
    - Sondes systeme (probes) : collecte d'informations systeme, indexation des executions,
echantillonnage de ressources
    - Repetitions pour la robustesse statistique
- Demonstration de l'execution sur un cluster SLURM (exemples prepares avec PlaFRIM)

##### Partie 4 : Visualisation et rapports
- Generation de rapports HTML interactifs avec iops report
- Exploration des graphiques Plotly et personnalisation des rapports
- Export des resultats (CSV, Parquet, SQLite) et utilisation des archives (iops archive) pour la
reproductibilite

##### Conclusion et questions
- Recapitulatif des points cles et ressources complementaires
- Discussion ouverte et questions des participants

#### Public vise et prerequis

Public visé :

Ce tutoriel s'adresse aux chercheurs, ingenieurs et etudiants (master ou doctorat) qui ont besoin de mener
des etudes parametriques, que ce soit dans le domaine du calcul haute performance (HPC), des systemes
distribues, de l'evaluation de performances ou de tout autre domaine necessitant l'execution systematique
de programmes avec differentes configurations. Il sera utile aussi bien aux personnes qui menent des
campagnes de benchmarks qu'a tout etudiant ou chercheur souhaitant automatiser et rendre reproductible
l'exploration de parametres dans ses experiences.

Prérequis :
- Connaissances de base en ligne de commande Linux
- Notions de Python (installation de paquets via pip, comprehension basique de scripts)
- Familiarite avec le format YAML (souhaitable mais pas obligatoire, une introduction rapide sera
fournie)
- Aucune connaissance prealable d'IOPS n'est requise

#### Materiel et equipement necessaires
##### Pour les participants :
- Un ordinateur portable avec un systeme Linux
- Python 3.10 ou superieur installe
- Acces a Internet pour l'installation des paquets Python
- Un editeur de texte (VS Code, vim, nano, etc.)

##### Pour les organisateurs :
- Videoprojecteur et ecran
- Acces Wi-Fi

##### Documentation officielle d'IOPS : https://iops.gitlabpages.inria.fr/
##### Code source : https://gitlab.inria.fr/lgouveia/iops
##### Package PyPI : https://pypi.org/project/iops-benchmark/
##### Benchmarks utilises :
- IOR (Interleaved Or Random) : https://github.com/hpc/ior
- STREAM : https://www.cs.virginia.edu/stream/
- NAS Parallel Benchmarks (NPB) : https://www.nas.nasa.gov/software/npb.html

### Tutoriel Design de périphériques par HLS sur un cœur RISC-V CVA6 - Amphi 14h30-18h

#### Organisateur
- Nicolas Derumigny

#### Objectif
Découvrir les interactions matérielle-logicielles par le prisme du design de matériel adressé directement sur un bus commun, et écriture du pilote associé.

#### Logiciels
Vivado / Vitis HLS (archive fournie), Git, cross-compilateur RISC-V, éditeur de texte.

#### Matériel (déjà en notre possession)
3 PYNQ-Z2 avec modules d'extension PMOD (SD + UART-USB), carte SD, adaptateurs.

#### Prérequis
Linux, ~80 Go d'espace disque.

#### Contenu
Les participants partiront d'un SoC CVA6 fonctionnel (bootant Linux) et devront :
1. Designer un périphérique en C/C++ grâce à la synthèse haut-niveau (HLS) via l'éditeur Vitis. Le périphérique réalisera une opération (calcul, interaction avec un bouton ou une LED) et se connectera comme esclave sur un bus AXI (configuration nativement prise en charge).
2. Réaliser la synthèse haut-niveau pour obtenir une IP RTL importable depuis Vivado.
3. L'intégrer au SoC RISC-V existant en le connectant au le northbridge, et en configurant la zone mémoire associée (MMIO). Réaliser le placement / routage du SoC.
4. Écrire un pilote interagissant avec l'IP en ouvrant /dev/mem et en écrivant / lisant sur les adresses MMIO, en prenant soin d'invalider les lignes de cache pour garantir une lecture / écriture correcte.
5. Cross-compiler le pilote et l'exécuter sur le SoC final.


<!-- Les tutoriels seront organisés le mardi 30 juin 2026, avant la conférence pour une durée d'environ 3h00 (possibilité de demander deux créneaux pour un tutoriel de 6h sur la journée). La participation aux tutoriels est gratuite pour tous les participants à la conférence COMPAS 2026. -->

<!-- ### Objectifs -->

<!-- Les tutoriels doivent servir un ou plusieurs des objectifs suivants : -->

<!-- - Initier les novices aux principaux thèmes des différentes communautés COMPAS. -->
<!-- - Introduire des méthodes et outils à des non spécialistes dans un sous-domaine de COMPAS. -->
<!-- - Motiver et expliquer un sujet d’importance émergent. -->

<!-- Nous encourageons des tutoriels avec une composante pratique ou un autre élément interactif. -->

<!-- ### Thématiques -->

<!-- Toutes les thématiques relevant de la conférence (Architecture, Systèmes et Parallélisme) sont les bienvenues.  -->

<!-- ### Dates importantes -->

<!-- - Date limite de soumission des tutoriels : 13/03/2026 -->
<!-- - Notification auteurs et affichage tutoriels acceptés : à venir -->
<!-- - Résumés des tutoriels et pages web : à venir -->

<!-- ### Instructions de soumission -->

<!-- Propositions à envoyer à Philippe.Roose@iutbayonne.univ-pau.fr. -->
<!--
Les propositions de tutoriels doivent être soumises par email à [compas2026@inria.fr](mailto:compas2026@inria.fr).. -->

<!-- Les propositions doivent être soumises dans un seul mail contenant les informations suivantes : -->

<!-- - Une description du tutoriel en deux phrases -->
<!-- - Un déroulé détaillé du tutoriel sous forme de points -->
<!-- - Une brève caractérisation du public cible potentiel du tutoriel, y compris les connaissances pré-requises -->
<!-- - Une brève description du matériel requis. -->

<!-- Local Variables: -->
<!-- jinx-languages: "fr" -->
<!-- jinx-local-words: "tutoriel" -->
<!-- End: -->

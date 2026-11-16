# Plan — talk Lightcone, IN2P3/IRFU ML Workshop 2026

Instructions pour réduire `IN2P3_2026.html` (branche `in2p3-2026`, commit `e11fdf1` d'Alexandre : 24 slides, ~22 min) à ~13 slides / ~13:30.
Ce plan répond à `OUTLINE_IN2P3.md` en appliquant le déroulé décidé au point quotidien du 16 nov. Presque toutes les slides sont **déjà dans le deck actuel** ; il faut surtout retirer, réordonner, et créer/modifier 3 slides.

## Contexte

- **Événement** : IN2P3/IRFU Machine Learning Workshop 2026, LPSC Grenoble & Zoom. https://indico.in2p3.fr/event/40347/
- **Créneau** : mardi 17 novembre 2026, 10:00, 20 min (15 min de talk + 5 min de questions). Session « AI Ecosystem: Infrastructure, Open Science and Community ».
- **Orateur** : Alexandre Boucaud (CNRS · APC / IN2P3, technical lead Lightcone Research).
- **Même session, 10:20** : lightning talk d'Alexandre sur la fédération ILaaS (inférence). Ne pas doublonner, seulement y renvoyer.
- **Langue des slides** : anglais.
- **Public** : chercheurs et ingénieurs IN2P3 (physique des particules, astroparticules, cosmologie, calcul).
- **Source du déroulé** : point quotidien Lightcone du 16 nov. (Linear, doc « Daily sync ups », section Nov 16th).

## Message clé

> Agents can do a huge amount of work, but they must express it in a shareable standard that others can build on — and that cannot be PDFs.

## Consignes de contenu (issues du point du 16 nov.)

1. **Intro** : partir des résultats OpenAI de septembre (Navier–Stokes, preuve formalisée en Lean), pas des anciens exemples (METR, clawRxiv, ICML…). Cadrage : il y a un an on craignait le « AI slop » ; aujourd'hui l'IA fait clairement du travail utile.
2. **Ne pas hiérarchiser** les travaux et **ne citer aucun domaine** comme « moins important » (pas d'exemple du type « systematics »). Formulation : le volume total de travail augmente, la capacité humaine à l'absorber reste fixe. Les humains dans la boucle sont une *boundary condition*. Citation possible de Fernando Pérez : « write less so we can read more ».
3. **Astra v0.1** : on peut dire qu'elle est **en beta** pour qui veut regarder, **jamais** qu'elle est prête.
4. **CC-IN2P3** : Lightcone n'est **pas** encore disponible dans les kernels du CC. Le contact autorise à le mentionner, mais il faut **promettre moins** : pas de « deployed » ni de « in progress » avec date.
5. **Fellowship** : préciser que **ce n'est pas un stage**. L'objectif est un article utilisant les outils Lightcone d'ici le printemps 2027, et le temps à y consacrer est celui que demande le projet.
6. Orthographe : **Mystra** sur les nouvelles slides. Les slides existantes écrivent « MySTRA » : à harmoniser seulement si Alexandre le demande.

## Plan (13 slides, ~13:30, ~1:30 de marge)

Toutes les slides sont des `<section id="…">` **du `IN2P3_2026.html` actuel** (commit `e11fdf1`), sauf la slide 4, qui est nouvelle. On les garde **telles quelles**, sauf modification indiquée. Le numéro entre crochets renvoie à la numérotation de `OUTLINE_IN2P3.md`.

| # | id | Outline | Durée | Modifications |
|---|---|---|---|---|
| 1 | `title` | [1] | 0:20 | Aucune (nouveau titre d'Alexandre : « An open ecosystem for connecting humans to reproducible and composable computational analyses in the age of AI agents »). |
| 2 | `ns-case` | [7] | 1:30 | Aucune. **Remonte en ouverture.** OpenAI 8 sept. 2026, ~130B tokens, ~10 000 agents, Lean + Mathlib ; lettre ouverte « A Severe Misalignment of AI in Mathematics » (11 sept.). |
| 3 | `corpus` | [9] | 1:15 | Aucune. Machine-scale vs human-scale. Vérifier la consigne 2 (aucun domaine présenté comme moins important). |
| 4 | `ecosystem` | — | 1:15 | **NOUVELLE**, remplace `stack` [11]. Voir « Slide 4 » ci-dessous. |
| 5 | `overview` | [8] | 0:30 | Aucune (équipe). |
| 6 | `takeaways` | [10] | 0:40 | Aucune (AAI4Science Developer Summit, le « workshop » du déroulé). |
| 7 | `astra-schema` | [12] | 1:30 | Garder les fragments existants, déjà dans le bon ordre : idx 1 = inputs + outputs (**provenance**) → idx 2 = **decisions** → idx 3 = prior insight + finding (**justifications & findings**) → idx 4 = les trois propriétés. Juste vérifier. |
| 8 | `paper-package` | [16] | 1:00 | Aucune. C'est la slide « PDF vs papier Astra » (animation `paper_final_v7.pdf` → graphe Astra + récit MyST). Si François envoie sa version, la remplacer. |
| 9 | `astra-mystra` | [14] | 0:50 | Aucune. Mystra concrètement : la prose référence l'analyse (`{astra:value}`). Placée **après** `paper-package` (le « comment » après le « quoi »). |
| 10 | `result-hubble` | [21] | 1:00 | Aucune. L'« exemple de reproduction ». |
| 11 | `lc-cli-demo` | [18] | 1:30 | Aucune. Le « workflow ». |
| 12 | `in2p3` | [23] | 0:50 | **Réécrire**, voir « Slide 12 » ci-dessous. |
| 13 | `fellowship` | [24] | 1:15 | **Ajouter une ligne**, voir « Slide 13 » ci-dessous. |

**Total ≈ 13:20.** Si le temps manque, couper dans cet ordre : `astra-mystra` (9), puis `takeaways` (6).

Réponses aux « cut candidates » de l'outline :
- `trajectory` → coupée, avec `accel`, `pressure`, `the-question` et `position-substrate` : le déroulé du 16 nov. ouvre sur OpenAI.
- `ns-case` vs `corpus` → les deux restent : c'est le duo « résultat OpenAI → trace machine vs communauté humaine » du déroulé.
- `takeaways` → gardée courte (0:40), c'est le workshop.
- Trio vision vs `astra-mystra` → `paper-package` + `astra-mystra` ; `vision-title` et `decision-support` en annexe.
- `result-dag` → annexe.
- `lc-cli-engine` → annexe ; en dire une phrase pendant la démo.

### Annexes (après le divider `backup`)

Dans l'ordre :
1. `backup` ; mettre à jour son sous-titre selon cette liste ;
2. `vision-title` ;
3. `decision-support` ;
4. `lc-cli-engine` ;
5. `lc-cli-venues` ;
6. `astra-universes` ;
7. `result-dag` ;
8. `stack` ;
9. `astra-elements` ;
10. `astra-insights` ;
11. `lc-cli-skills` ;
12. `hiring` ;
13. `work-with-us`.

### Retirées du deck

`accel`, `trajectory`, `pressure`, `the-question`, `position-substrate`.

Garder leur HTML ailleurs n'est pas nécessaire : elles restent dans `LBNL2026.html`.

## Slide 4 — `ecosystem` (nouvelle)

Même style que `stack` / `work-with-us` du thème (cartes `card-glow`, `section-label`, `h2`). Trois colonnes, qui apparaissent l'une après l'autre (fragments 1, 2, 3).

- `section-label` : **What we are building**
- `h2` : **One record, read by machines and by people**
- Colonne 1 — icône `fa-diagram-project`, couleur `--lc-primary`
  - **ASTRA** — *the structured record that compounds*
  - « A declarative spec of an analysis: inputs, decisions, outputs, prior insights and findings, each tied to its evidence. Agents write it; anyone can re-run, check and extend it. »
  - pied : `astra‑spec.org`
- Colonne 2 — icône `fa-book-open`, couleur `--lc-warm`
  - **Mystra** — *the bridge to the human story*
  - « MyST for ASTRA: the paper's prose references the analysis instead of restating it. Every number in the text resolves to the record behind it. »
  - pied : `MyST · Jupyter Book 2`
- Colonne 3 — icône `fa-sliders`, couleur `--lc-secondary`
  - **Lightcone Lab & UIs** — *human understanding and control*
  - « A JupyterLab extension to navigate, inspect and steer the record — it runs wherever JupyterLab and JupyterHub already do. »
  - pied : `pip install jupyterlab-lightcone`
- Bandeau bas (petit, `--lc-muted`) : « **ASTRA v0.1 is in beta** — try it and tell us what breaks; it is not production-ready yet. »

Option : ajouter `assets/jupyter-logo.svg` et `assets/myst-logo.svg` dans les colonnes 2 et 3 (déjà dans le repo, utilisés par `UCOSPO2026.html#open-by-default`).

## Slide 12 — `in2p3` (réécriture)

Repartir de la slide actuelle (même mise en page en deux groupes), avec ces changements :

- `h2` : **Bringing it to IN2P3**
- Groupe « What we are working on » : **une seule carte**, sans étiquette « in progress ».
  - **CC-IN2P3** — « Working with CC-IN2P3 to make the stack available to IN2P3 users. The execution layer already targets SLURM clusters through the same interface. »
  - Supprimer la carte VirtualData.
- Groupe « What we need » : garder 3 cartes.
  - **Agent-ready HPC access** (inchangée)
  - **Shared best practices** (inchangée)
  - **Inference for everyone** → remplacer par : « **ILaaS federation** — shared, secure access to frontier and open models for individuals and projects. *Lightning talk right after this one (10:20).* »
- Ne rien affirmer qui ne soit pas vrai au 17 nov. Si un doute subsiste sur la phrase CC-IN2P3, préférer la supprimer.

## Slide 13 — `fellowship` (ajout)

Garder la slide actuelle (QR code, « Apply by Friday 20 Nov », You get / You bring, pied de page RFC + contacts), avec deux changements :

- Ajouter sous le sous-titre italique, ou en dernier point de « You bring », une ligne mise en valeur :
  « **Not an internship:** the goal is a paper using Lightcone tools by spring 2027 — the time it takes is the time your project needs. »
- Si ça déborde, raccourcir « You get » : fusionner onboarding + Slack, et retirer « (4–6 Fellows) ».

Note orale pour Alexandre, à ne pas mettre sur la slide : très peu de candidatures de la communauté française pour l'instant ; date limite vendredi 20 nov.

## Construction

- **Éditer `IN2P3_2026.html` en place** (commit `e11fdf1`) : supprimer, déplacer et modifier des `<section>`. Le `<head>` (CSS) et le script de fin viennent de LBNL et couvrent déjà les animations `data-story-step` de `paper-package` et `decision-support`.
- Pour déplacer des sections proprement, la fonction `extract(html, sid)` de `scripts/build_in2p3.py` extrait une `<section>` en respectant l'imbrication. Le reste de ce script a construit la première version du deck et ne correspond plus à l'état actuel : ne pas le relancer tel quel.
- Garder `assets/qr-fellowship.svg` (QR vers https://www.lightconeresearch.org/fellowship).
- Supprimer `OUTLINE_IN2P3.md` et ce fichier avant la fusion dans `main`, comme l'indique l'outline.

## Vérifications avant de livrer

1. Ouvrir le deck en local (`python3 -m http.server`), parcourir toutes les slides **et tous les fragments** : aucune erreur console, aucun débordement en 1280×720.
2. Vérifier en particulier :
   - l'animation `data-story-step` de `paper-package` ;
   - les 4 étapes de `astra-schema` ;
   - la lecture de la vidéo `lc-cli-demo`.
3. Chronométrer à voix haute : cible ≤ 14 min.
4. Relire les consignes 1–6 ci-dessus slide par slide (surtout v0.1 « beta », CC-IN2P3 sans sur-promesse, mention « Not an internship »).
5. Mettre à jour la ligne du README si le titre change.
6. Commit sur `in2p3-2026`, puis PR vers `main` pour publication sur `lightconeresearch.github.io/talks/IN2P3_2026.html`.

## Points ouverts

- **Slide « PDF vs papier Astra » de François** : pas encore reçue. `paper-package` sert de remplaçant jusque-là.
- **Formulation exacte de la phrase CC-IN2P3** : à valider par Alexandre.

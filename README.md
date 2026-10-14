# ACCase-Resistome-Docking-Dynamics

## Overview
This repository contains the complete computational bioinformatics pipeline developed for an M.Sc. thesis investigating herbicide resistance mechanisms in Acetyl-CoA Carboxylase (ACCase). The pipeline performs high-throughput molecular docking, structural validation, binding energy landscape analysis, and automated PyMOL rendering across wild-type and mutated protein models.

---

## Repository Structure
```text
ACCase-Resistome-Docking-Dynamics/
├── 01_Receptor_Models/             # Cleaned and minimized PDB receptor models (WT and Mutants: ALA, CIS, Double)
├── 02_Ligands/                     # Herbicide ligand structures (.pdb and minimized .pdbqt)
├── 03_Vina_Configs/                # AutoDock Vina configuration files and grid center scripts
├── 04_Docking_Results/             # Docked ligand poses (_out.pdbqt), Vina logs, and binding affinity summary table
│   ├── Docked_Poses/
│   ├── Vina_Logs/
│   └── Vina_Binding_Affinities.csv
├── 05_Validation_and_Affinity_Plots/ # Publication infographics (Bar charts, Heatmaps, Violin plots, Radar charts, Ramachandran plots)
└── 06_PyMOL_Rendered_Structures/   # High-resolution ray-traced 3D structural interaction renders (1920x1080, 300 DPI)

---

## Pipeline Workflow

1. **Receptor Preparation & Modeling:** Structural preparation, cleaning, and homology modeling of target templates (`1UYR` and `3K8X`) across Wild-Type and resistance-associated mutants (ALA, CIS, Double).
2. **High-Throughput Virtual Screening:** Automated batch docking of target herbicides (`Diclofop`, `Sethoxydim`, `Pinoxaden`) using **AutoDock Vina v1.2.5** across active-site grid parameters.
3. **Structural & Stereochemical Validation:** Ramachandran backbone dihedral angle calculations and quantitative residue evaluation.
4. **Infographic & 3D Visualization:** Automated data visualization via Matplotlib/Seaborn and headless ray-traced structural rendering via **PyMOL**.

---

## Key Results Summary

* **Binding Affinity Matrix:** Comprehensive evaluation of energetic shifts ($\Delta G$) across mutant variants.
* **Resistance Profiling:** Heatmap and radar chart analyses highlighting differential sensitivity patterns of ACCase targets against aryloxyphenoxypropionate (FOP) and cyclohexanedione (DIM) herbicide classes.

---

## Requirements & Environment

* **Python 3.10+ / 3.13**
* **Libraries:** `AutoDock Vina`, `PyMOL`, `Biopython`, `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`

---

## Citation


# Exoplanet Habitability Index

Deterministic habitability index for exoplanets.

This project was originally developed as the Final Master's Thesis for the Master's in Data Science and Big Data at MIOTI Tech School.

The initial version of the project was developed collaboratively as part of a team project.

This repository currently contains that initial collaborative version.

A personal extended version of the project, including improvements and additional analysis, will be published in this repository in the future.

## Project Overview

The goal of this project is to build a deterministic habitability index for exoplanets using astrophysical and planetary parameters.

The index compares exoplanet characteristics with Earth-like conditions in order to estimate potential habitability.

The project includes:

- Dataset loading and reduction to a core set of relevant physical variables
- Missing value treatment through a mixed imputation strategy:
  - median-based imputation for variables without direct deterministic relations
  - physically grounded assumptions for specific variables
  - conditional reconstruction using explicit astrophysical relationships
- Initial exploratory analysis of variable distributions and outlier detection
- Outlier treatment and construction of a final analysis dataset
- Statistical characterization of the processed dataset
- Correlation analysis and identification of highly related variables
- Formal definition of the habitability index

## 🚀 Live Application

You can explore the interactive application here:

https://habitableexoplanets-mioti.streamlit.app/
- Construction of an Earth reference vector
- Relative scaling of variables with respect to Earth-like conditions
- Variable-level deviation calculation and aggregation through Euclidean distance
- Computation of the final habitability index
- Generation of a ranked list of exoplanets according to the proposed index
- Interpretation of the top-ranked planets
- Empirical coherence checks and exploratory validation of the index
- Sensitivity analysis of the proposed formulation

# Mammogram Radiomics Pipeline

💡 Purpose

To explore how radiomic features extracted from mammography images vary across breast-tissue density levels, and to build a reproducible PyRadiomics pipeline for future machine-learning experiments.

Why This Matters ⁉️

Breast density can distort texture and intensity patterns, making radiomic features less stable. Analyzing how these variations arise is important for developing ML models that remain reliable across patients with different tissue compositions.

Overview

This project sets up a basic radiomics pipeline that:
    •    loads mammography images and lesion ROI masks
    •    extracts first-order, texture, and shape features using a YAML config
    •    filters cases by BI-RADS breast density
    •    produces a feature table for downstream ML analysis

🧬 Why Radiomics?

Radiomics converts medical images into thousands of quantitative features describing:
    •    Intensity patterns (first-order statistics)
    •    Texture (GLCM, GLRLM, GLSZM, NGTDM, GLDM)
    •    Shape descriptors

These features can capture subtle patterns not visible to the human eye and help build ML models for classification, prognosis, or state-transition modeling.

Repository Structure

config/
data/images/
data/masks/
scripts/
    extract_features.py
    filter_by_birads.py
results/
requirements.txt

Usage

Install dependencies:

pip install -r requirements.txt

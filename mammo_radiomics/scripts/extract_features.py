import os
import pandas as pd
from radiomics import featureextractor

# Basic radiomics pipeline template
def extract_features(metadata_csv, images_root, masks_root, yaml_path, output_csv):
    df = pd.read_csv(metadata_csv)

    # PyRadiomics extractor
    extractor = featureextractor.RadiomicsFeatureExtractor(yaml_path)

    results = []

    for _, row in df.iterrows():
        img_rel = row["image file path"]
        mask_rel = row["ROI mask file path"]

        img_path = os.path.join(images_root, img_rel)
        mask_path = os.path.join(masks_root, mask_rel)

        # Skip missing files
        if not os.path.exists(img_path) or not os.path.exists(mask_path):
            continue

        # Extract features
        try:
            feats = extractor.execute(img_path, mask_path)
        except Exception as e:
            print(f"Error extracting features for {img_rel}: {e}")
            continue

        # Keeps only image and mask
        row_dict = {"image": img_rel, "mask": mask_rel}

        for k, v in feats.items():
            if k.startswith("original"):
                row_dict[k] = v

        # Keep tissue density if available
        if "breast_density" in df.columns:
            row_dict["breast_density"] = row["breast_density"]

        results.append(row_dict)

    pd.DataFrame(results).to_csv(output_csv, index=False)
    print("Saved radiomics features to:", output_csv)
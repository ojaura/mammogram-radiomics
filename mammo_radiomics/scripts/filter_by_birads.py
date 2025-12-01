# scripts/filter_by_birads.py

import pandas as pd
import argparse

def filter_by_birads(metadata_csv, birads_level, output_csv):
    """
    Filter CBIS-DDSM-style metadata by BI-RADS breast_density level.

    Parameters
    ----------
    metadata_csv : str
        Input CSV file containing a 'breast_density' column.
    birads_level : int
        BI-RADS density level to keep (e.g., 1–4).
    output_csv : str
        Output CSV file for the filtered subset.
    """
    df = pd.read_csv(metadata_csv)

    if "breast_density" not in df.columns:
        raise ValueError("Column 'breast_density' not found in the CSV.")

    filtered = df[df["breast_density"] == birads_level]
    filtered.to_csv(output_csv, index=False)
    print(f"[DONE] Saved BI-RADS {birads_level} subset: {len(filtered)} rows → {output_csv}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter metadata by BI-RADS tissue density.")
    parser.add_argument("--input", required=True, help="Path to metadata CSV")
    parser.add_argument("--birads", type=int, required=True, help="BI-RADS level (e.g., 1–4)")
    parser.add_argument("--output", required=True, help="Path to output CSV")

    args = parser.parse_args()

    filter_by_birads(args.input, args.birads, args.output)
# Solution Package — Competitive & Catalog Analysis

## What this package contains
- `data/` — copies of the original uploaded files for reproducibility.
- `scripts/` — a reproducible `analysis.py` script and `requirements.txt` to rerun the analysis.
- `reports/` — this readable report (report.md).
- `outputs/` — all generated CSV/JSON outputs including summaries and suggested actions.
- `README.md` — instructions to run and explanations.

## Quick summary of findings (auto-generated)
{
  "internal_catalog_rows": 10,
  "internal_catalog_columns": [
    "item_code",
    "product_line",
    "brand_name",
    "suggested_retail",
    "cost_basis",
    "launch_date",
    "lifecycle_stage",
    "priority_tier",
    "min_advertised_price",
    "product_description"
  ],
  "internal_catalog_sku_candidates": [
    "product_line",
    "product_description"
  ],
  "internal_catalog_numeric_cols": [
    "suggested_retail",
    "cost_basis",
    "min_advertised_price"
  ],
  "catalog_price_mean": 151.59,
  "catalog_price_median": 111.99,
  "inventory_movements_rows": 10,
  "inventory_movements_sku_candidates": [
    "sku"
  ],
  "inventory_movements_qty_candidates": [
    "units_shipped",
    "units_returned"
  ],
  "performance_metrics_rows": 23,
  "performance_metrics_columns": [
    "week_ending",
    "identifier",
    "channel",
    "impressions",
    "clicks",
    "conversions",
    "ad_spend",
    "revenue",
    "search_rank_avg",
    "competitor_price_index"
  ],
  "performance_avg_conv": 64.43478260869566,
  "competitor_rows": 1,
  "marketplace_rows": 1,
  "merge_keys_guess": {
    "catalog_key": "product_line",
    "market_key": "platforms.amazon.products"
  },
  "merged_rows": 10,
  "price_gap_note": "Not enough price columns found to compute gap."
}

## Key recommendations
1. Standardize identifiers (SKUs/ASINs) across data sources to allow joins and product-level analysis.
2. Replenish high-movement SKUs and prioritize those for promotions where margins allow.
3. Optimize pricing for SKUs where our price is significantly **higher** than marketplace peers (see outputs/price_gap_analysis.csv if available).
4. Use performance metrics to identify poor-performing inventory and design targeted promotions.
5. Expand competitor data capture to include timestamps, shipping, and promotional flags.

## Files of interest
- `outputs/top_inventory_movers.csv` — top moving SKUs by quantity (derived from inventory_movements.csv)
- `outputs/marketplace_snapshot_flat.csv` — flattened marketplace snapshot
- `outputs/competitor_intelligence_flat.csv` — flattened competitor intelligence (if available)
- `outputs/catalog_marketplace_merged.csv` — merged view (if merge keys found)
- `outputs/price_gap_analysis.csv` — price differentials between catalog and marketplace prices (if available)
- `outputs/summary_statistics.json` — summary metrics and parsing notes
- `outputs/recommendations.json` — recommended next steps

---
### How to run locally
1. Create a Python 3.9+ virtualenv.
2. `pip install -r scripts/requirements.txt`
3. `python scripts/analysis.py --data-dir data --out-dir outputs`
   - The script will read files from `data/` and write outputs to `outputs/`


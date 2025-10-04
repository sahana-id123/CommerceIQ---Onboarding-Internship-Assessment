📦 Competitive & Catalog Analysis — Solution Package

This repo analyzes internal catalog data, marketplace listings, competitor insights, inventory movements, and performance metrics to uncover actionable opportunities.

✅ 1. Approach

Data Ingestion
Loaded 5 source files (CSV + JSON) into a reproducible /data directory.

Schema Inference & Normalization

Auto-detected SKU/product IDs

Flattened JSON fields

Cleaned numeric columns

Standardized nested values

Exploratory Profiling

Row/column summaries

Numeric stat extraction

Key joins tested (catalog ↔ marketplace)

Insight Outputs

Top movers

Flattened marketplace/competitor data

Catalog-market merges

Price gap flags

Summary + recommendations JSON

Packaging
Full solution delivered with scripts/, reports/, outputs/, requirements.txt

✅ 2. Key Findings

SKU fields inconsistent → partial merges

High-velocity items identified from inventory data

Flattened marketplace & competitor feeds available

Price comparison possible on overlapping IDs

Performance metrics usable for SKU prioritization

✅ 3. Recommendations

Standardize SKU/ASIN/product IDs across sources

Prioritize restock of top movers

Optimize pricing where marketplace is cheaper

Target low-CTR/low-conversion SKUs for action

Expand competitor tracking with timestamped data

✅ 4. Assumptions

Columns inferred by naming convention

Nested IDs flattened or stringified

No external APIs or enrichment

Numeric coercion used for summaries

✅ 5. AI Usage Disclosure

AI was used to:

Structure the solution

Infer schemas and generate scripts

Summarize outputs and write documentation

All results were based only on files you supplied — no external data was accessed.

✅ 6. Priority & Future Enhancements

Immediate
✔ Normalize product IDs
✔ Confirm price fields & mappings
✔ Validate merged catalog view

Next
✔ Add margin & promo simulation
✔ Introduce notebooks or dashboards

Later
✔ Automate ingestion + reporting
✔ Enrich with marketplace APIs

▶️ Reproduce Locally
pip install -r scripts/requirements.txt
python scripts/analysis.py


Outputs regenerate into /outputs.

🔎 Key Files to Review
File	Description
reports/report.md	Summary of insights
outputs/top_inventory_movers.csv	Fast-moving SKUs
outputs/catalog_marketplace_merged.csv	Join results
outputs/recommendations.json	Action points
outputs/summary_statistics.json	Parsing overview

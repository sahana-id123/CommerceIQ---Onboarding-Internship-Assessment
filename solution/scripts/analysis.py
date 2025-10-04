import os, json
import pandas as pd
import numpy as np
from pathlib import Path

data_dir = Path('data')
out_dir = Path('outputs')
out_dir.mkdir(parents=True, exist_ok=True)

def read_if_exists(p):
    p = data_dir / p
    if p.exists():
        if p.suffix == '.csv':
            return pd.read_csv(p)
        elif p.suffix == '.json':
            import json
            return json.load(open(p, 'r', encoding='utf-8'))
    return None

catalog = read_if_exists('internal_catalog_dump.csv')
marketplace = read_if_exists('marketplace_snapshot.json')
competitor = read_if_exists('competitor_intelligence.json')
inventory = read_if_exists('inventory_movements.csv')
perf = read_if_exists('performance_metrics.csv')

if isinstance(inventory, pd.DataFrame):
    sku_col = None
    for c in inventory.columns:
        if 'sku' in c.lower() or 'product' in c.lower() or 'id' in c.lower():
            sku_col = c; break
    qty_col = None
    for c in inventory.columns:
        if 'qty' in c.lower() or 'quantity' in c.lower() or 'units' in c.lower() or 'count' in c.lower():
            qty_col = c; break
    if sku_col and qty_col:
        movers = inventory.groupby(sku_col)[qty_col].sum().abs().sort_values(ascending=False).head(50)
        movers.reset_index().to_csv(out_dir / 'top_inventory_movers.csv', index=False)
print('Done. Check outputs/ for generated files.')

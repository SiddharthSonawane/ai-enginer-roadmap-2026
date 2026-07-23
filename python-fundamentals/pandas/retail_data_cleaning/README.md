# Retail Store Sales — Data Cleaning Project

## Overview
This project cleans a messy retail transaction dataset (12,575 rows, 11 columns) sourced from Kaggle's "Retail Store Sales: Dirty for Data Cleaning" dataset. The goal was not just to remove problems, but to understand *why* each issue existed and choose the most defensible fix, recovering data where possible, and transparently flagging what couldn't be recovered rather than guessing or silently dropping rows.

## Dataset
- **Source:** Kaggle — Retail Store Sales: Dirty for Data Cleaning
- **Rows:** 12,575
- **Columns:** Transaction ID, Customer ID, Category, Item, Price Per Unit, Quantity, Total Spent, Payment Method, Location, Transaction Date, Discount Applied

## Issues Found & How They Were Handled

| Column | Issue | Rows Affected | Action Taken | Reasoning |
|---|---|---|---|---|
| Item | Missing values | 1,213 (9.6%) | Filled with `"Unknown Item"` | Category was always present for these rows, so the transaction itself was still valid — filling preserves the row for revenue/category analysis instead of losing it |
| Price Per Unit | Missing values | 609 (4.8%) | Recovered via `Total Spent ÷ Quantity` | Both Quantity and Total Spent were always present for these rows — this is a mathematically exact recovery, not an estimate |
| Quantity | Missing values | 604 (4.8%) | Left blank, flagged via `missing_quantity_and_total = True` | Only Price Per Unit was known for these rows — one equation, two unknowns, mathematically unrecoverable. Flagging (not dropping or guessing) preserves the transaction record while being honest about the gap |
| Total Spent | Missing values | 604 (4.8%) | Same as above — flagged, not fabricated | Same reasoning as Quantity |
| Discount Applied | Missing values | 4,199 (33.4%) | Filled with `False`, flagged via `discount_unrecorded = True` | Boolean field with no way to infer the true value from other columns; defaulted conservatively (no discount) while flagging that the value was originally unrecorded, not confirmed |
| Transaction Date | Stored as text | All rows | Converted to proper `datetime` type | Needed for any date-based filtering, sorting, or trend analysis |
| Discount Applied | Stored as generic object type | All rows | Converted to proper `bool` type | Ensures the column behaves correctly in filters/logic downstream |

## Validation Performed
- **Exact duplicate rows:** 0 found
- **Duplicate Transaction IDs:** 0 found
- **Math consistency check:** For all rows with complete data, `Price Per Unit × Quantity` was verified against `Total Spent` — 0 mismatches found across the entire clean portion of the dataset

## Design Principle
Every fix in this project follows one rule: **recover with real math where possible, flag transparently where not — never silently guess or drop data.** Two new columns (`missing_quantity_and_total`, `discount_unrecorded`) were added specifically so that anyone using this cleaned dataset downstream can still identify and handle the originally-incomplete rows on their own terms, rather than having that decision made invisibly for them.

## Files
- `raw_sales.csv` — original, unmodified dataset
- `cleaned_sales.csv` — final cleaned dataset
- `cleaning_notebook.ipynb` — full step-by-step cleaning process with explanations
- `README.md` — this file

## Tools Used
Python, pandas, Jupyter Notebook

# Week 3: Advanced Data Analysis and Visualization in Logistics

## Project overview
This project explores a simulated logistics dataset using Python, pandas, NumPy, and Matplotlib. It investigates delivery-time distributions, transportation costs, shipment volume, route distance, transport modes, regional differences, and correlations.

## Files
- `logistics_shipments.csv` — 200 simulated shipment records.
- `logistics_analysis.py` — script for summary analysis and chart generation.
- `requirements.txt` — Python package requirements.
- `DATA_README.md` — field definitions and limitations.
- `visualizations/` — chart images used in the report.
- `Week3_Logistics_Analysis_Report.docx` — formatted report.

## Run locally
```bash
pip install -r requirements.txt
python logistics_analysis.py
```
The script prints descriptive statistics and group summaries, then saves six PNG charts in `visualizations/`.

## Main questions
1. How are delivery times distributed?
2. Which transport mode has the highest average cost?
3. How do distance and shipment volume relate to cost?
4. Are delivery times different across regions?
5. What relationships appear in the correlation matrix?

## Important note
The dataset is hypothetical and reproducible for this project. Results and recommendations are educational examples, not claims about a real company.

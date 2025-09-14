# CORD-19 Data Analysis
## Overview
This project analyzes a sample of the CORD-19 dataset, which contains metadata about COVID-19 research papers.

## Dataset
The original dataset is too large for GitHub, so a 5% sample was created using random sampling. The sample contains approximately [number] rows.

## Key Findings
1. Most COVID-19 papers were published in 2020-2021
2. Top journals: PloS One
3. Common title keywords: COVID, pandemic, clinical, study, etc.

## How to Run
1. Install requirements: `pip install pandas matplotlib seaborn streamlit wordcloud`
2. Run the Streamlit app: `streamlit run app.py`

## Challenges
- The original dataset was too large for GitHub and memory constraints
- Missing values in key columns required careful handling
- Date formatting inconsistencies needed special processing

## Files
- `create_sample.py`: Script to create a sample from the full dataset
- `analysis.py`: Data cleaning and analysis code
- `app.py`: Streamlit application
- `metadata_sample.csv`: 5% sample of the original data
- `cleaned_metadata_sample.csv`: Cleaned version of the sample

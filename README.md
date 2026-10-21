# E-Commerce Enterprise Analytics & Interactive Dashboard

### Overview
This project represents a comprehensive, end-to-end Data Analytics workflow. It encompasses the entire data lifecycle: from raw data generation and ETL (Extract, Transform, Load) processing, to Exploratory Data Analysis (EDA), culminating in a fully interactive, dark-themed business intelligence dashboard.

### Architecture & Tech Stack
*   **Data Processing (ETL):** Python, Pandas, Numpy
*   **Exploratory Data Analysis:** Jupyter Notebook
*   **Interactive Dashboard:** Dash, Plotly (Dark Theme)

### Repository Structure
*   `src/data_pipeline.py`: Generates and cleans the raw transactional data, exporting a production-ready dataset.
*   `notebooks/eda_analysis.ipynb`: Statistical analysis and data exploration.
*   `app.py`: The interactive Dash web application visualizing the final metrics.
*   `requirements.txt`: Project dependencies.

### Reproduction
1. Install dependencies: `pip install -r requirements.txt`
2. Run the ETL pipeline: `python src/data_pipeline.py` (This will create a `data/` folder and generate `processed_sales.csv`)
3. Launch the dashboard: `python app.py`

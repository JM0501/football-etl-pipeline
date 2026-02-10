# Football Data ETL Pipeline 

## Project Overview
This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python.
The pipeline extracts football data from the API-Football service, transforms the data into
a clean and analytics-ready format, and loads it into a MongoDB database via a backend API.

The project is designed to simulate a real-world data engineering workflow and will later
support analytics dashboards and reporting.

---

## Objectives
- Extract real-time football data from an external API
- Transform raw JSON data into structured formats
- Load cleaned data into MongoDB
- Design scalable ETL pipelines using Python
- Prepare data for analytics and visualization

---

## Technologies Used
- Python
- API-Football (External Data Source)
- MongoDB
- Railway (Backend API hosting)
- pandas (Data transformation)
- requests (API communication)

---

## Project Structure
- football-etl-pipeline/
   - config/ # Configuration files
   - extract/ # Data extraction logic
   - transform/ # Data transformation logic
   - load/ # Data loading logic
   - pipelines/ # Pipeline orchestration
   - utils/ # Logging and helper utilities
   - .env # Environment variables
   - requirements.txt
   - README.md

---

## ETL Workflow
1. **Extract**  
   Fetch football data such as leagues, teams, and fixtures from API-Football.

2. **Transform**  
   Clean, filter, and restructure the data for analytics use cases.

3. **Load**  
   Store transformed data in MongoDB collections.

---

## Future Enhancements
- Add PySpark for large-scale processing
- Implement scheduling (cron / Airflow)
- Build analytics dashboards (Power BI / Streamlit)
- Add data quality checks and validations

---

## Author
Built as a hands-on data engineering learning project, by Tshepang Mohlamonyane(j4ym).

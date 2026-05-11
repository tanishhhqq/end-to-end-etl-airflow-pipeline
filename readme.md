# End-to-End ETL Pipeline with Apache Airflow

## Project Overview

This project demonstrates a Dockerized end-to-end ETL pipeline using Apache Airflow, Python, Pandas, and PostgreSQL. The pipeline automates data extraction, transformation, validation, and loading workflows for retail sales datasets.

---

## Tech Stack

- Apache Airflow
- Python
- Pandas
- PostgreSQL
- Docker
- SQLAlchemy

---

## Project Architecture

```text
CSV Dataset
   ↓
Extract
   ↓
Transform
   ↓
Validate
   ↓
Load into PostgreSQL
   ↓
Orchestrated with Airflow
```

---

## Project Structure

```text
end-to-end-etl-airflow-pipeline/
│
├── dags/
│   └── etl_pipeline.py
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   └── load.py
│
├── data/
│   └── raw/
│       └── superstore.csv
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Features

- Automated ETL workflow orchestration
- Dockerized Airflow environment
- Data extraction using Pandas
- Data transformation and validation
- PostgreSQL integration
- Modular ETL architecture
- Scheduled DAG execution

---

## Workflow

1. Extract retail sales data from CSV dataset
2. Transform and clean data using Pandas
3. Validate dataset quality
4. Load processed data into PostgreSQL
5. Schedule and orchestrate workflows using Airflow

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/tanishhhqq/end-to-end-etl-airflow-pipeline.git
```

### Navigate to Project

```bash
cd end-to-end-etl-airflow-pipeline
```

### Start Docker Containers

```bash
docker compose up -d
```

---

## Airflow Access

Open Airflow UI:

```text
http://localhost:8080
```

### Login Credentials

```text
Username: admin
Password: admin
```

---

## Dataset Location

Place dataset inside:

```text
data/raw/superstore.csv
```

---

## DAG Execution

1. Enable DAG
2. Trigger `etl_pipeline`
3. Monitor task execution in Airflow UI

---

## Future Improvements

- Add cloud storage integration
- Add automated alerts
- Implement incremental loading
- Add CI/CD pipelines
- Integrate Great Expectations
- Add dashboard visualizations

---

## Screenshots

### Airflow DAG

(Add screenshot here)

### Successful DAG Execution

(Add screenshot here)

---

## Skills Demonstrated

- ETL Pipelines
- Workflow Orchestration
- Apache Airflow
- Docker
- PostgreSQL
- Python Automation
- Data Validation
- Data Engineering

---

## Author

Tanishq Jadhav
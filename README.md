<div align="center">

# 🌦️ Weather ETL Pipeline

### End-to-End Data Engineering Project using Apache Airflow, PostgreSQL & OpenWeather API

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)

![Apache Airflow](https://img.shields.io/badge/Apache-Airflow-red?style=for-the-badge&logo=apache-airflow)

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)

![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker)

![REST API](https://img.shields.io/badge/REST-API-success?style=for-the-badge)

</p>

A production-style ETL pipeline that automatically extracts real-time weather data from the **OpenWeather API**, transforms it into a structured format, and loads it into **PostgreSQL** using **Apache Airflow**.

</div>

---

# 📖 Overview

This project demonstrates how to build an automated **ETL (Extract, Transform, Load)** pipeline using **Apache Airflow**.

The pipeline periodically retrieves live weather information from the OpenWeather API, cleans and transforms the data, and stores it in a PostgreSQL database for reporting and analysis.

The project showcases industry-standard Data Engineering practices including workflow orchestration, API integration, data transformation, and automated scheduling.

---

# 🎯 Project Objectives

- Automate weather data collection
- Build a production-ready ETL workflow
- Schedule pipelines using Apache Airflow
- Store structured data in PostgreSQL
- Demonstrate modern Data Engineering concepts

---

# ✨ Features

✅ Automated ETL Pipeline

✅ Apache Airflow DAG

✅ OpenWeather REST API Integration

✅ Data Cleaning & Transformation

✅ PostgreSQL Data Storage

✅ Workflow Scheduling

✅ Error Handling

✅ Docker Support

✅ Modular Project Structure

---

# 🚀 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Apache Airflow | Workflow Orchestration |
| PostgreSQL | Database |
| OpenWeather API | Weather Data Source |
| Docker | Containerization |
| SQL | Data Storage |

---

# 📂 Project Structure

```
weather-etl-pipeline/
│
├── dags/
│     └── etl_weather.py
│
├── plugins/
│
├── logs/
│
├── requirements.txt
│
├── docker-compose.yaml
│
├── .env
│
└── README.md
```

---

# 🏗️ System Architecture

```
          OpenWeather API
                 │
                 ▼
         Extract Weather Data
                 │
                 ▼
      Data Cleaning & Transformation
                 │
                 ▼
        Apache Airflow Scheduler
                 │
                 ▼
        PostgreSQL Database
                 │
                 ▼
        Analytics & Reporting
```

---

# 🔄 ETL Workflow

## 1️⃣ Extract

The pipeline retrieves live weather information using the OpenWeather REST API.

Collected information includes:

- Temperature
- Humidity
- Pressure
- Wind Speed
- Weather Description
- Timestamp
- City Name

---

## 2️⃣ Transform

The extracted JSON response is processed to:

- Remove unnecessary fields
- Convert timestamps
- Normalize values
- Handle missing data
- Prepare records for database insertion

---

## 3️⃣ Load

The transformed weather data is inserted into a PostgreSQL database using Airflow's PostgreSQL Hook.

---

# 📊 Data Flow

```
OpenWeather API

↓

HTTP Request

↓

JSON Response

↓

Python Transformation

↓

Airflow DAG

↓

PostgreSQL

↓

Dashboard / Analytics
```

---

# 🗄️ Database Schema

| Column | Type |
|----------|----------|
| id | Integer |
| city | VARCHAR |
| temperature | FLOAT |
| humidity | INTEGER |
| pressure | INTEGER |
| wind_speed | FLOAT |
| weather_description | VARCHAR |
| timestamp | TIMESTAMP |

---

# 📅 Airflow DAG

```
Extract Weather Data

↓

Transform Weather Data

↓

Load into PostgreSQL
```

Each task is monitored independently, allowing retries and failure recovery.

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/weather-etl-pipeline.git
```

---

## Navigate

```bash
cd weather-etl-pipeline
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Docker

```bash
docker-compose up
```

---

## Start Airflow

```bash
airflow standalone
```

---

## Access Airflow

```
http://localhost:8080
```

---

# 🚀 Running the Pipeline

Start the scheduler

```bash
airflow scheduler
```

Start the webserver

```bash
airflow webserver
```

Trigger the DAG manually or let it execute automatically according to the schedule.

---

# 📷 Sample Weather Record

```json
{
    "city": "Bhubaneswar",
    "temperature": 31.8,
    "humidity": 73,
    "pressure": 1008,
    "wind_speed": 3.2,
    "weather": "Clear Sky",
    "timestamp": "2026-07-05 10:30:00"
}
```

---

# 📈 Skills Demonstrated

- Data Engineering
- ETL Pipeline Development
- Apache Airflow
- REST API Integration
- PostgreSQL
- SQL
- Docker
- Python
- Workflow Automation
- Data Transformation
- Task Scheduling
- Production Pipeline Design

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Designing ETL Pipelines
- Apache Airflow DAG Development
- Task Dependencies
- Airflow Hooks
- Scheduling Workflows
- API Data Extraction
- PostgreSQL Integration
- Dockerized Development
- Error Handling
- Data Validation

---

# 🚀 Future Enhancements

- AWS S3 Data Storage
- Apache Spark Integration
- PySpark Data Processing
- Kafka Streaming
- Weather Forecast ETL
- Multiple City Support
- Email Alerts on DAG Failure
- Power BI Dashboard
- Tableau Dashboard
- Data Quality Checks
- CI/CD Pipeline
- Kubernetes Deployment
- Cloud Deployment (AWS/GCP/Azure)

---

# 📊 Pipeline Monitoring

Apache Airflow provides:

- DAG Visualization
- Task Status Tracking
- Retry Mechanism
- Execution History
- Logging
- Error Monitoring

---

# 💡 Use Cases

- Weather Analytics
- Climate Monitoring
- Agriculture
- Smart Cities
- Environmental Research
- IoT Applications
- Data Warehousing
- Business Intelligence

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Biswaranjan Chakra

**Aspiring Data Engineer | Python Developer | Machine Learning Enthusiast**

### Skills

- Python
- SQL
- PostgreSQL
- Apache Airflow
- PySpark
- Docker
- ETL Development
- Machine Learning
- Data Engineering

---

<div align="center">

### ⭐ If you found this project useful, please consider giving it a Star!

**Building Scalable Data Pipelines, One Workflow at a Time. 🚀**

</div>

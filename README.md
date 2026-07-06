# 🌦️ Weather ETL Pipeline using Apache Airflow

An end-to-end ETL (Extract, Transform, Load) pipeline built with **Apache Airflow** that automatically fetches real-time weather data from the **OpenWeather API**, transforms the data into a structured format, and stores it in **PostgreSQL** for analysis and reporting.

---

## 📌 Project Overview

This project demonstrates how to build a production-style ETL pipeline using Apache Airflow.

The pipeline performs the following operations every day:

- 🌐 Extracts live weather data from the OpenWeather API
- 🔄 Transforms the JSON response into a structured format
- 🗄️ Loads the processed data into a PostgreSQL database
- ⏰ Automates the workflow using Apache Airflow DAGs

---

## 🚀 Features

- Automated daily ETL workflow
- Apache Airflow TaskFlow API
- REST API integration using HttpHook
- PostgreSQL integration using PostgresHook
- Modular Extract → Transform → Load architecture
- Error handling through Airflow task monitoring
- Easy to extend for multiple cities

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Apache Airflow | Workflow Orchestration |
| PostgreSQL | Data Storage |
| OpenWeather API | Weather Data Source |
| Docker | Containerization |
| SQL | Database Operations |

---

## 📂 Project Structure

```
weather-etl-pipeline/
│
├── dags/
│   └── etl_weather.py
│
├── screenshots/
│
├── requirements.txt
│
├── README.md
│
└── docker-compose.yaml
```

---

## ⚙️ ETL Workflow

### 1️⃣ Extract

- Connects to the OpenWeather API using Airflow's HttpHook.
- Retrieves real-time weather data for the configured location.

Example API Response:

```json
{
    "temp": 22.6,
    "humidity": 71,
    "pressure": 1014,
    "weather": "clear sky",
    "wind_speed": 4.1
}
```

---

### 2️⃣ Transform

The extracted JSON data is converted into a clean structure containing:

- Temperature
- Humidity
- Pressure
- Weather Description
- Wind Speed
- Timestamp

---

### 3️⃣ Load

The transformed data is inserted into PostgreSQL using Airflow's PostgresHook.

Example SQL:

```sql
INSERT INTO weather_data
(
temperature,
humidity,
pressure,
weather_description,
wind_speed,
timestamp
)
VALUES (...);
```

---

## 📊 Workflow Diagram

```
OpenWeather API
        │
        ▼
  Extract Task
        │
        ▼
 Transform Task
        │
        ▼
    Load Task
        │
        ▼
 PostgreSQL Database
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    temperature FLOAT,
    humidity INT,
    pressure INT,
    weather_description VARCHAR(255),
    wind_speed FLOAT,
    timestamp TIMESTAMP
);
```

---

## ▶️ Running the Project

### Clone the repository

```bash
git clone https://github.com/yourusername/weather-etl-pipeline.git
```

---

### Navigate into the project

```bash
cd weather-etl-pipeline
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Start Airflow

```bash
docker-compose up
```

---

### Open Airflow UI

```
http://localhost:8080
```

Default credentials:

```
Username: airflow
Password: airflow
```

---

## 📈 Airflow DAG

```
Extract
   │
   ▼
Transform
   │
   ▼
Load
```

The DAG is scheduled to run **daily** and automatically stores the latest weather information.

---

## 📸 Screenshots

You can add screenshots here:

- Airflow DAG Graph
- Airflow Tree View
- PostgreSQL Table
- Successful DAG Run

---

## 🔮 Future Improvements

- Support multiple cities
- Weather forecasting
- AWS S3 integration
- Data visualization using Power BI/Tableau
- Email alerts on ETL failure
- Docker Compose deployment
- CI/CD with GitHub Actions
- Data validation using Great Expectations

---

## 📚 Learning Outcomes

This project helped me understand:

- ETL Pipeline Development
- Apache Airflow DAGs
- Airflow Hooks
- TaskFlow API
- REST API Integration
- PostgreSQL
- Workflow Scheduling
- Docker
- SQL Data Loading

---

## 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Biswaranjan Chakra**

- 💼 Aspiring Data Engineer
- 🐍 Python Developer
- 📊 SQL & PostgreSQL
- ⚙️ Apache Airflow
- 🚀 ETL Pipeline Developer

If you found this project helpful, don't forget to ⭐ star the repository!

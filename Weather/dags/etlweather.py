from airflow import DAG 
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook  
from airflow.decorators import task
from datetime import datetime


#latitude and longitude for the desired location 
LATITUDE="51.5074"
LONGITUDE="-0.1278"
POSTGRES_CONN_ID = "postgres_default"
API_CONN_ID = 'openweathermap_api'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1)
}

## dag
with DAG(
    dag_id="etl_weather",
    default_args=default_args,
    schedule="@daily",
    catchup=False,
) as dag:

    @task()
    def extract():
        ##Use HTTP Hook to get the connection details from airflow connections and make the API request
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method='GET')
        ## https://api.openweathermap.org/data/2.5/weather?lat=51.5074&lon=-0.1278&appid=ec6ca29b413ac81dc584a364f90c1b3b&units=metric
        endpoint = f"data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid=ec6ca29b413ac81dc584a364f90c1b3b&units=metric"
        response = http_hook.run(endpoint)
        data = response.json()
        return data

    @task()
    def transform(data):
        transformed_data = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'weather_description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
            'timestamp': data['dt']
        }
        return transformed_data

    @task()
    def load(transformed_data):
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        insert_query = """
            INSERT INTO weather_data (temperature, humidity, pressure, weather_description, wind_speed, timestamp)
            VALUES (%s, %s, %s, %s, %s, to_timestamp(%s))
        """
        pg_hook.run(insert_query, parameters=(
            transformed_data['temperature'],
            transformed_data['humidity'],
            transformed_data['pressure'],
            transformed_data['weather_description'],
            transformed_data['wind_speed'],
            transformed_data['timestamp']
        ))

    # Define the task dependencies
    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data)
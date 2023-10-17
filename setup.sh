#!/usr/bin/env bash
up() {
  echo "Starting Airbyte..."
  cd airbyte
  docker-compose stop -v
  docker-compose up -d
  cd ..

  echo "Starting Airflow..."
  cd airflow
  docker-compose stop -v    
  docker-compose up airflow-init
  docker-compose up -d
  cd ..

  echo "Starting Metabase..."
  cd metabase
  docker-compose stop -v
  docker-compose up -d
  cd ..
 
  echo "Access Airbyte at http://localhost:8000 and set up the connections."
  
  echo "Access Airflow at http://localhost:8080 to kick off your Airbyte sync DAG."  

  echo "Access Metabase at http://localhost:3000 and set up a connection with Snowflake."

}

config() {

  echo "Connecting Airflow with Airbyte..."
  echo "Enter your Airbyte Epidemiology connection ID: "
  export epidemiology_connection_id="e1b7cc7a-c34e-4c3c-becf-041febc9b590"

  echo "Enter your Airbyte Economy connection ID: "
  export economy_connection_id="77c9c17f-7a7e-42e7-abe8-00af8442c533"
 
  echo "Enter your Airbyte Demographics connection ID: "
  export demographics_connection_id="9c7c40a6-72ec-4d57-a7a4-382560210df6"
 
  echo "Enter your Airbyte Index connection ID: "
  export  index_connection_id="57612cc3-59b8-4747-822f-18891e7994e4"

  # Set connection IDs for DAG.
  cd airflow
  docker-compose run airflow-webserver airflow variables set 'AIRBYTE_EPIDEMIOLOGY_CONNECTION_ID' "$epidemiology_connection_id"
  docker-compose run airflow-webserver airflow variables set 'AIRBYTE_ECONOMY_CONNECTION_ID' "$economy_connection_id"
  docker-compose run airflow-webserver airflow variables set 'AIRBYTE_DEMOGRAPHICS_CONNECTION_ID' "$demographics_connection_id"
  docker-compose run airflow-webserver airflow variables set 'AIRBYTE_INDEX_CONNECTION_ID' "$index_connection_id"

  docker network create modern-data-stack
  docker network connect modern-data-stack airbyte-proxy
  docker network connect modern-data-stack airbyte-worker  
  docker network connect modern-data-stack airflow-airflow-worker-1
  docker network connect modern-data-stack airflow-airflow-webserver-1
  docker network connect modern-data-stack metabase
  
  cd airflow
  docker-compose run airflow-webserver airflow connections add 'airbyte_example' --conn-uri 'airbyte://airbyte-proxy:8000'
  cd ..
  
  echo "Config Updated..."
}


down() {
  echo "Stopping Airbyte..."
  cd airbyte
  docker-compose stop
  cd ..
  echo "Stopping Airflow..."
  cd airflow
  docker-compose stop
  cd ..
  echo "Stopping Metabase..."
  cd metabase
  docker-compose stop
  cd ..
}

case $1 in
  up)
    up
    ;;
  config)
    config
    ;;
  down)
    down
    ;;
  *)
    echo "Usage: $0 {up|config|down}"
    ;;
esac
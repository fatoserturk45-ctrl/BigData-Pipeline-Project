from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# Airflow için temel ayarları yapıyoruz
default_args = {
    'owner': 'fatos',
    'start_date': datetime(2026, 1, 1),
}

with DAG(
    dag_id='olist_pipeline_orchestrator',
    default_args=default_args,
    schedule_interval='@daily',  # Her gün otomatik çalışacak şekilde planlandı
    catchup=False
) as dag:

    # 1. GÖREV: Aşama 1 ve 2'de yaptığımız Spark scriptini tetikliyoruz (Ingestion)
    trigger_spark_job = BashOperator(
        task_id='trigger_spark_ingestion',
        bash_command='spark-submit C:/Users/fatoş/Desktop/BigData-Pipeline-Project/scripts/spark_ingestion.py'
    )

    # 2. GÖREV: Az önce yazdığımız dbt modellerini çalıştırıyoruz (Transformation)
    # Proje klasörüne geçiş yapıp dbt.exe'yi tam yoluyla tetikliyoruz
    trigger_dbt_transformation = BashOperator(
        task_id='trigger_dbt_transformation',
        bash_command='cd C:/Users/fatoş/Desktop/BigData-Pipeline-Project/my_olist_dbt_project && "C:\\Users\\fatoş\\AppData\\Roaming\\Python\\Python313\\Scripts\\dbt.exe" run'
    )

    # 3. GÖREV: Akış bittiğinde Superset dashboard'larını yenileme simülasyonu
    refresh_superset = BashOperator(
        task_id='refresh_superset_dashboards',
        bash_command='echo "Superset dashboards refreshed successfully!"'
    )

    # Görevlerin çalışma sırasını (bağımlılıklarını) tanımlıyoruz:
    # Önce Spark çalışacak -> Sonra dbt dönüşümleri yapacak -> En son Superset yenilenecek
    trigger_spark_job >> trigger_dbt_transformation >> refresh_superset
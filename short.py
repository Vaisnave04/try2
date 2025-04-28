import random, time, logging, mlflow

logging.basicConfig(level=logging.info, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MonitoringLogger")

def generate_random_data():
    with mlflow.start_run():
        mlflow.log_params({'app_name': 'MyApp', 'version': '1.0'})
        start = time.time()
        try:
            while True:
                data = random.uniform(0, 100)
                logger.info(f"Generated: {data}")
                mlflow.log_metric("my_metric", data)
                mlflow.log_metric("app_uptime_seconds", time.time() - start)
                time.sleep(2)
        except KeyboardInterrupt:
            logger.info("Stopped by user.")

if __name__ == "__main__":
    logger.info("App Started.")
    try: generate_random_data()
    finally: logger.info("App Stopped.")

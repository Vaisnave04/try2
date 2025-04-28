import random
import time
import logging
import mlflow

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MonitoringLogger")

def generate_random_data():
    """Function to generate random data and log it using standard logging and MLflow."""
    with mlflow.start_run():
        mlflow.log_params({'app_name': 'MyApp', 'version': '1.0'})
        start_time = time.time()

        try:
            while True:
                data = random.uniform(0, 100)  # Generate random data
                logger.info(f"Generated data: {data}")
                mlflow.log_metric("my_metric", data)

                uptime = time.time() - start_time
                mlflow.log_metric("app_uptime_seconds", uptime)

                time.sleep(2)  # Simulate work
        
        except KeyboardInterrupt:
            logger.info("Monitoring stopped due to KeyboardInterrupt.")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        finally:
            mlflow.end_run()

if __name__ == "__main__":
    logger.info("Monitoring and Logging Application Started.")
    try:
        generate_random_data()
    except Exception as e:
        logger.error(f"Error in application execution: {e}")
    finally:
        logger.info("Monitoring and Logging Application Stopped.")

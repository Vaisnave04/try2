''''import random,time,mlflow,logging

logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MonitoringLogger")

def generate_random_app():
    with mlflow.start_run():
        mlflow.log_params({'app_name':'MyApp','version' :'1.0'})
        start = time.time()
        try:
            while True:
                data = random.uniform(0,100)
                logger.info(f"Generated : {data}")
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Stopped by user.")



if __name__=="__main__":
    logger.info("App started")
    try: generate_random_app()
    finally: logger.info("App stopped")'''


import random,time,logging, mlflow

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger('MonitoringLogger')


		
def generate_random_app():
    with mlflow.start_run():
        mlflow.log_params({'app_name':'MyApp','version' :'1.0'})
        start = time.time()
        try:
            while True:
                data = random.uniform(0,100)
                logger.info(f"Generated : {data}")
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Stopped by user.")
if __name__ =="__main__":
	logger.info("App Started")
	try : 
		generate_random_app()
	finally : 
		logger.info ("App Stopped")
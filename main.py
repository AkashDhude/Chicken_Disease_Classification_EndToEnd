from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> Stage {STAGE_NAME} comleted <<<<<\n\nx----------------------x")
except Exception as e :
    logger.info(e)
    raise e
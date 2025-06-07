from TextSummarizer.pipeline.data_ingestion_1 import DataIngestionPipeline
from TextSummarizer.pipeline.data_validation_2 import DataValidationTrainingPipeline
from TextSummarizer.pipeline.data_transformation_3 import DataTransformationPipeline
from TextSummarizer.pipeline.model_trainer_4 import ModelTrainerTrainingPipeline
from TextSummarizer.pipeline.model_evaluation_5 import ModelEvaluationTrainingPipeline
from TextSummarizer.logging import logger

Step_name = "Data Ingestion step"

try:
    logger.info(f"<<< Step {Step_name} start >>>\n\n\n ")
    data_ingestion= DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"<<< Step {Step_name} completed >>\n\n>")

except Exception as e:
    logger.exception(e)
    raise e

Step_name = "Data Validation step"

try:
    logger.info(f"<<< Step {Step_name} start >>>\n\n\n ")
    data_validation= DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"<<< Step {Step_name} completed >>\n\n>")

except Exception as e:
    logger.exception(e)
    raise e

Step_name = "Data Transformation step"

try:
    logger.info(f"<<< Step {Step_name} start >>>\n\n\n ")
    data_validation= DataTransformationPipeline()
    data_validation.main()
    logger.info(f"<<< Step {Step_name} completed >>\n\n>")

except Exception as e:
    logger.exception(e)
    raise e


Step_name = "Model Training step"

try:
    logger.info(f"<<< Step {Step_name} start >>>\n\n\n ")
    model_training= ModelTrainerTrainingPipeline()
    model_training.main()
    logger.info(f"<<< Step {Step_name} completed >>\n\n>")

except Exception as e:
    logger.exception(e)
    raise e


Step_name = "Model Evaluation step"

try:
    logger.info(f"<<< Step {Step_name} start >>>\n\n\n ")
    model_evaluation= ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f"<<< Step {Step_name} completed >>\n\n>")

except Exception as e:
    logger.exception(e)
    raise e
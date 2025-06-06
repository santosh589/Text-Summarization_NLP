from TextSummarizer.pipeline.data_ingestion_1 import DataIngestionPipeline
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
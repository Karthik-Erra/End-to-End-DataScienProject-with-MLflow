from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience.config.configuration import ConfigurationManager


class ModelEvaluatinPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation_pipeline(self):
        config = ConfigurationManager()
        get_model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config = get_model_evaluation_config)
        model_evaluation.log_into_mlflow()
        
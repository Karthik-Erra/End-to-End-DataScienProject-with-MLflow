import os
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config
    def validate_all_columns(self)->bool:
        validation_status = None
        data = pd.read_csv(self.config.unzip_data_dir)

        all_schema = self.config.all_schema.keys()
        #all_schema_values = self.config.all_schema.values()

        all_cols = list(data.columns)
        #all_dtypes = data.dtypes.astype(str).unique().tolist()

        for col in all_cols:
            if col not in all_schema:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation Status: {validation_status}")
            else:
                validation_status = True
                with open(self.config.STATUS_FILE,'w') as f:
                    f.write(f"Validation Status: {validation_status}")
            
        return validation_status

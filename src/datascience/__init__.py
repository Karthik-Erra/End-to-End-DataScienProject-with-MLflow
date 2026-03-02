import os
import sys
import logging
from datetime import datetime


log_file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_directory = os.path.join(os.getcwd(),"log")

os.makedirs(log_directory,exist_ok=True)

log_file_path = os.path.join(log_directory,log_file_name)

logging.basicConfig(
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger()
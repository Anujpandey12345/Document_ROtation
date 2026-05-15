import logging
import os 
from config import LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)

log_file = os.path.join(LOG_DIR, "pipeline.py")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"   # Adds timestamp - 2026-05-15 10:30:45
)
logger = logging.getLogger()



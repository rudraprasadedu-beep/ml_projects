import os
import sys
import logging
from datetime import datetime

# === Create logs directory if it doesn't exist ===
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# === Generate timestamped log file ===
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# === Configure logging ===
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [%(levelname)s] (%(name)s:%(lineno)d) - %(message)s",
    level=logging.INFO,
)

# === Add console output ===
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

# === Define logger object ===
logger = logging.getLogger(__name__)

# === Redirect all print() output to log file ===
class PrintLogger:
    """Redirects print() output to both console and log file"""
    def __init__(self, stream, log_file_path):
        self.terminal = stream
        self.log = open(log_file_path, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = PrintLogger(sys.stdout, LOG_FILE_PATH)
sys.stderr = PrintLogger(sys.stderr, LOG_FILE_PATH)

logger.info("Logging initialized successfully.")
print("✅ Log file created at:", LOG_FILE_PATH)

import os
from dotenv import load_dotenv  
load_dotenv()  # Load environment variables from .env file

class Config:
    def __init__(self):
        # Load and validate configuration values from environment variables    
        self.load_values()
        self.convert_values()
        self.validate_values()

    def load_values(self):
        # load values from .env
        self.TFL_API_URL = os.getenv("TFL_API_URL") 
        self.KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        self.KAFKA_RAW_TOPIC = os.getenv("KAFKA_RAW_TOPIC")
        self.REQUEST_TIMEOUT = os.getenv("REQUEST_TIMEOUT")
        self.POLL_INTERVAL = os.getenv("POLL_INTERVAL")
        self.RETRY_COUNT = os.getenv("RETRY_COUNT")
        self.LOG_LEVEL = os.getenv("LOG_LEVEL")

    def convert_values (self):
        # convert numeric values
        self.REQUEST_TIMEOUT = int(self.REQUEST_TIMEOUT)
        self.POLL_INTERVAL = int(self.POLL_INTERVAL)
        self.RETRY_COUNT = int(self.RETRY_COUNT)

    def validate_values(self):
        # validate values
        if not self.TFL_API_URL:
            raise ValueError("TFL_API_URL is not set in the environment variables.")
        if not self.KAFKA_BOOTSTRAP_SERVERS:
            raise ValueError("KAFKA_BOOTSTRAP_SERVERS is not set in the environment variables.")
        if not self.KAFKA_RAW_TOPIC:
            raise ValueError("KAFKA_RAW_TOPIC is not set in the environment variables.")
        if not self.LOG_LEVEL:
            raise ValueError("LOG_LEVEL is not set in the environment variables.")
        if self.REQUEST_TIMEOUT <= 0:
            raise ValueError("REQUEST_TIMEOUT must be a positive integer.")
        if self.POLL_INTERVAL <= 0:
            raise ValueError("POLL_INTERVAL must be a positive integer.")
        if self.RETRY_COUNT < 0:
            raise ValueError("RETRY_COUNT must be a non-negative integer.")
        pass
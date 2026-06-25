import os
from dotenv import load_dotenv  
load_dotenv()  # Load environment variables from .env file

class Config:
    '''Configuration class for loading and validating environment variables.'''
    def __init__(self):
        # Load and validate configuration values from environment variables    
        self.load_values()
        self.convert_values()
        self.validate_values()

    def load_values(self):
        # load values from .env
        self.tfl_api_urlfl_api_url = os.getenv("TFL_API_URL") 
        self.kafka_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        self.kafka_raw_topic = os.getenv("KAFKA_RAW_TOPIC")
        self.request_timeout = os.getenv("REQUEST_TIMEOUT")
        self.poll_interval = os.getenv("POLL_INTERVAL")
        self.retry_count = os.getenv("RETRY_COUNT")
        self.log_level = os.getenv("LOG_LEVEL")

    def convert_values (self):
        # convert numeric values
        try:
            self.request_timeout = int(self.request_timeout)
            self.poll_interval = int(self.poll_interval)
            self.retry_count = int(self.retry_count)
        except ValueError as e:
            raise ValueError(f"Invalid numeric value in environment variables: {e}")

    def validate_values(self):
        # validate values
        if not self.tfl_api_url:
            raise ValueError("tfl_api_url is not set in the environment variables.")
        if not self.kafka_servers:
            raise ValueError("kafka_servers is not set in the environment variables.")
        if not self.kafka_raw_topic:
            raise ValueError("kafka_raw_topic is not set in the environment variables.")
        if not self.log_level:
            raise ValueError("log_level is not set in the environment variables.")
        if self.request_timeout <= 0:
            raise ValueError("request_timeout must be a positive integer.")
        if self.poll_interval <= 0:
            raise ValueError("poll_interval must be a positive integer.")
        if self.retry_count < 0:
            raise ValueError("retry_count must be a non-negative integer.")
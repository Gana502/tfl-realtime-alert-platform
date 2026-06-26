from common.config import Config
from common.logger import get_logger
from producer.tfl_api_client import TfLApiClient


def main():
    config = Config()

    logger = get_logger("producer")

    logger.info("Producer started")

    client = TfLApiClient(config, logger)

    data = client.get_data()

    print(data)  # Print the fetched data to the console

    logger.info(f"Fetched {len(data)} records from TfL API")

    logger.info("Producer completed successfully")


if __name__ == "__main__":
    main()
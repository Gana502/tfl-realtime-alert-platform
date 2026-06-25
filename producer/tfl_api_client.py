import requests


class TfLApiClient:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def get_data(self):
        self.logger.info("Fetching data from the TfL API")

        try:
            response = requests.get(
                self.config.tfl_api_url,
                timeout=self.config.request_timeout
            )

            response.raise_for_status()

            self.logger.info("Successfully fetched data from the TfL API")
            return response.json()

        except requests.RequestException as error:
            self.logger.error(f"Failed to fetch data from TfL API: {error}")
            raise
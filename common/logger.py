import logging


def get_logger(name):
    # Create a logger with the specified name
    logger = logging.getLogger(name)
    # Set the logging level to INFO
    logger.setLevel(logging.INFO)
    # Create a console handler to output logs to the console
    console_handler = logging.StreamHandler()
    # Set the logging level for the console handler to INFO
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    # Set the formatter for the console handler
    console_handler.setFormatter(formatter)
    # Add the console handler to the logger
    logger.addHandler(console_handler)
    # Return the configured logger
    return logger
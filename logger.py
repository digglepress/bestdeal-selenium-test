import logging

log_format = '''
%(asctime)s - TEST - %(levelname)s
---------
%(message)s

'''


def with_logs(func):
    def wrapper(*args):
        # Create a logger
        logger = logging.getLogger('test_doc_logger')
        logger.setLevel(logging.INFO)

        # Create a handler that logs to the console (stdout)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a formatter and attach it to the handler
        formatter = logging.Formatter(log_format)
        console_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(console_handler)

        logger.info(getattr(func, "__doc__", func.__name__))

    return wrapper

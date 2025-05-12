# logger.py
import logging

_logger = None

def get_logger():
    global _logger
    if _logger is None:
        _logger = logging.getLogger("bosszp")
        _logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('test.log')
        file_handler.setFormatter(formatter)
        if not _logger.hasHandlers():
            _logger.addHandler(file_handler)
    return _logger

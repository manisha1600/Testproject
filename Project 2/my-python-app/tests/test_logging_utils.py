import os
import sys
import logging

# Ensure `project` directory is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.logging_utils import get_logger


def test_get_logger_idempotent(tmp_path):
    log_dir = str(tmp_path / "logs")
    name = "test.logger"
    logger1 = get_logger(name, logging.DEBUG, log_dir=log_dir)
    handlers1 = len(logger1.handlers)

    logger2 = get_logger(name, logging.DEBUG, log_dir=log_dir)
    handlers2 = len(logger2.handlers)

    assert logger1 is logger2
    assert handlers1 == handlers2
    assert handlers1 >= 1


def test_file_created(tmp_path):
    log_dir = str(tmp_path)
    name = "test_file_logger"
    logger = get_logger(name, logging.INFO, log_dir=log_dir)
    logger.info("hello world")

    log_file = os.path.join(log_dir, f"{name.replace('.', '_')}.log")
    assert os.path.exists(log_file)

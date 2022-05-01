import logging
from logging.config import dictConfig

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            # Need to dig into what "()" is as a key and also whether I can supress messages when I've logged something too
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",

        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "my-project-logger": {"handlers": ["default"], "level": "INFO"},
    },
}

def get_logger(logger_name="my-project-logger"):
    dictConfig(log_config)
    return logging.getLogger(logger_name)
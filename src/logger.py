import logging.config
from pydantic import BaseModel

class LoggerConf(BaseModel):
    LOGGER_NAME: str = "task_manager"
    LOG_FORMAT: str = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    LOG_LEVEL: str = "DEBUG"

    version: int = 1
    disable_existing_loggers: bool = False

    formatters: dict = {
        "default": {
            "()": "logging.Formatter",
            "fmt": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }

    handlers: dict = {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout",
        },
    }

    loggers: dict = {
        "Task_Manager": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False
        },
        "Uvicorn": {
            "handlers": ["console"],
            "level": "DEBUG"
        },
        "Uvicorn.access": {
            "handlers": ["console"],
            "level": "DEBUG"
        },
    }

config_dict = LoggerConf().model_dump()
logging.config.dictConfig(config_dict)

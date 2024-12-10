import logging
from typing import Dict


user_config: Dict[str, str] = {"user": "darkfos82"}


async def logger_dep() -> logging.Logger:
    """
    Функция для Dependecy - Логирование действий
    :return:
    """

    logger = logging.getLogger(__name__)
    logging.basicConfig(
        filemode="edu-connect.log",
        level=logging.INFO,
        format="%(asctime)s %(user)-8s $(message)s"
    )
    
    return logger


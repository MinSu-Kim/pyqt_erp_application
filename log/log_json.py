import json
import logging.config

config = json.load(open('logger.json'))
logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.info('This is an INFO message. Hello dummy!')

"""
disable_existing_loggers 옵션은 뭘까요? 
logging.fileConfig() 혹은 logging.dictConfig()를 호출할 경우, 
기존에 존재하는 logger들이 전부 비활성화됩니다. 
이를 방지하기 위하여, 해당 함수 호출 시에 disable_existing_loggers을 False로 설정하는 것입니다.
"""


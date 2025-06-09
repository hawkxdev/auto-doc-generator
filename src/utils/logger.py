"""
Система цветного логирования с эмодзи
"""
import logging
import sys


class ColoredFormatter(logging.Formatter):
    """Форматтер с цветами и эмодзи"""

    COLORS = {
        'DEBUG': '\033[36m',
        'INFO': '\033[37m',
        'SUCCESS': '\033[32m',
        'WARNING': '\033[33m',
        'ERROR': '\033[31m',
        'CRITICAL': '\033[91m',
        'RESET': '\033[0m'
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.COLORS['INFO'])
        reset = self.COLORS['RESET']

        record.levelname_colored = f"{color}{record.levelname}{reset}"
        record.msg_colored = f"{color}{record.getMessage()}{reset}"

        return record.msg_colored


def setup_logger():
    """Настройка глобального логгера"""
    logger = logging.getLogger('auto_doc_generator')
    logger.setLevel(logging.DEBUG)

    logger.handlers.clear()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(ColoredFormatter())

    logger.addHandler(console_handler)

    return logger


def get_logger():
    """Получить настроенный логгер"""
    return logging.getLogger('auto_doc_generator')


def log_info(message: str):
    """Информационное сообщение"""
    logger = get_logger()
    logger.info(message)


def log_success(message: str):
    """Сообщение об успехе"""
    logger = get_logger()
    logger.info(f"✅ {message}")


def log_error(message: str):
    """Сообщение об ошибке"""
    logger = get_logger()
    logger.error(f"❌ {message}")


def log_warning(message: str):
    """Предупреждение"""
    logger = get_logger()
    logger.warning(f"⚠️ {message}")


def log_step(step: str):
    """Логирование этапа обработки"""
    logger = get_logger()
    logger.info(f"🔄 {step}")


def log_separator():
    """Разделитель в логах"""
    logger = get_logger()
    logger.info("-" * 50)

"""
PDF конвертер (демо-версия)
"""
from pathlib import Path
from src.utils.logger import log_info, log_warning


class PDFConverter:
    """Класс для конвертации Word в PDF (демо-версия)"""

    def __init__(self, config):
        self.config = config

    def convert_word_to_pdf(self, word_path: str, pdf_path: str):
        """Конвертация Word документа в PDF (заглушка для демо)"""

        # NOTE: В полной версии здесь будет реализована логика:
        # - Конвертация через docx2pdf
        # - Кроссплатформенное скрытие окон Word
        # - Обработка ошибок конвертации
        # - Валидация созданных PDF файлов

        log_warning("PDF конвертация доступна только в полной версии")
        log_info(f"Для создания PDF из {Path(word_path).name} используйте полную версию")

        return False

    def is_available(self):
        """Проверка доступности PDF конвертации"""
        return False

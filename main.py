#!/usr/bin/env python3
"""
Главный модуль для генерации документов
Обрабатывает Excel данные и создает Word/PDF документы на основе шаблона
"""
import json
import traceback
from pathlib import Path
from src.utils.logger import setup_logger, log_info, log_error, log_success, log_step, log_separator


def load_config():
    """Загрузка конфигурации из config.json"""
    config_path = Path("config.json")
    if not config_path.exists():
        raise FileNotFoundError("Файл config.json не найден")

    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_files(config):
    """Проверка существования входных файлов"""
    excel_path = Path(config['input']['excel_file'])
    template_path = Path(config['input']['word_template'])

    if not excel_path.exists():
        raise FileNotFoundError(f"Excel файл не найден: {excel_path}")

    if not template_path.exists():
        raise FileNotFoundError(f"Word шаблон не найден: {template_path}")

    log_success("Входные файлы найдены")


def create_output_directories(config):
    """Создание выходных папок"""
    output_paths = [
        Path(config['output']['word_folder']),
        Path(config['output']['pdf_folder'])
    ]

    for path in output_paths:
        path.mkdir(parents=True, exist_ok=True)

    log_success("Выходные папки созданы")


def main():
    """Главная функция"""
    try:
        setup_logger()
        log_info("🚀 Автогенератор документов - Демо версия")
        log_separator()

        log_step("Инициализация системы")
        config = load_config()
        log_success("Конфигурация загружена")

        validate_files(config)
        create_output_directories(config)

        log_step("Обработка данных")
        log_info("📊 Загрузка Excel данных...")

        from src.core.excel_processor import ExcelProcessor
        excel_processor = ExcelProcessor(config)
        excel_processor.load_file(config['input']['excel_file'])
        excel_processor.validate_structure()
        excel_processor.clean_data()

        log_info("📄 Загрузка Word шаблона...")

        from src.core.word_processor import WordProcessor
        word_processor = WordProcessor(config)
        word_processor.load_template(config['input']['word_template'])

        log_step("Генерация документов")
        log_info("🔄 Обработка записей...")
        # TODO: Добавить цикл обработки

        log_info("📋 Создание отчета...")
        # TODO: Добавить ReportGenerator

        log_separator()
        log_success("✅ Обработка завершена успешно!")

    except KeyboardInterrupt:
        log_error("⚠️ Прервано пользователем")
    except Exception as e:
        log_error(f"❌ Критическая ошибка: {e}")
        log_error(f"Трассировка: {traceback.format_exc()}")


if __name__ == "__main__":
    main()

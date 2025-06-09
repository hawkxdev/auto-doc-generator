"""
Обработчик Excel файлов
"""
import pandas as pd
from pathlib import Path
from src.utils.logger import log_info, log_success, log_warning, log_error


class ExcelProcessor:
    """Класс для обработки Excel данных"""

    def __init__(self, config):
        self.config = config
        self.data = None
        self.file_path = None

    def load_file(self, file_path: str):
        """Загрузка Excel файла"""
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            raise FileNotFoundError(f"Excel файл не найден: {file_path}")

        try:
            self.data = pd.read_excel(self.file_path)
            log_success(f"Excel файл загружен: {len(self.data)} записей")
            return self.data
        except Exception as e:
            raise RuntimeError(f"Ошибка чтения Excel файла: {e}")

    def validate_structure(self):
        """Валидация структуры данных"""
        if self.data is None:
            raise ValueError("Данные не загружены")

        if self.data.empty:
            raise ValueError("Excel файл пуст")

        required_columns = []
        for placeholder_config in self.config['placeholders'].values():
            column_name = placeholder_config['column']
            required_columns.append(column_name)

        missing_columns = []
        for column in required_columns:
            if column not in self.data.columns:
                missing_columns.append(column)

        if missing_columns:
            raise ValueError(f"Отсутствуют колонки: {', '.join(missing_columns)}")

        log_success("Структура данных валидна")

    def clean_data(self):
        """Очистка и подготовка данных"""
        if self.data is None:
            raise ValueError("Данные не загружены")

        initial_count = len(self.data)

        self.data = self.data.dropna(how='all')

        for column in self.data.columns:
            if self.data[column].dtype == 'object':
                self.data[column] = self.data[column].fillna('')
                self.data[column] = self.data[column].astype(str).str.strip()
            else:
                self.data[column] = self.data[column].fillna(0)

        final_count = len(self.data)

        if initial_count != final_count:
            log_warning(f"Удалено {initial_count - final_count} пустых строк")

        log_success("Данные очищены и подготовлены")

    def get_naming_column_value(self, row_data, row_index):
        """Получение значения для именования файла"""
        naming_column = self.config['excel_columns']['naming_column']

        if naming_column in row_data and pd.notna(row_data[naming_column]):
            value = str(row_data[naming_column]).strip()
            if value:
                return self._clean_filename(value)

        if len(row_data) > 0:
            first_column = row_data.iloc[0] if hasattr(row_data, 'iloc') else list(row_data.values())[0]
            if pd.notna(first_column):
                value = str(first_column).strip()
                if value:
                    return self._clean_filename(value)

        return f"{row_index:04d}"

    def _clean_filename(self, filename):
        """Очистка имени файла от недопустимых символов"""
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')

        filename = filename.replace(' ', '_')

        if filename.isdigit():
            return f"{int(filename):04d}"

        return filename

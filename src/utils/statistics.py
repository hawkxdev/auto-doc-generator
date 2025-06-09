"""
Система сбора статистики
"""


class Statistics:
    """Класс для сбора статистики операций"""

    def __init__(self):
        self.reset()

    def reset(self):
        """Сброс статистики"""
        self.text_replacements = 0
        self.image_insertions = 0
        self.images_found = 0
        self.images_not_found = 0
        self.documents_created = 0
        self.errors = 0

    def add_text_replacements(self, count: int):
        """Добавить количество замен текста"""
        self.text_replacements += count

    def add_image_insertions(self, count: int):
        """Добавить количество вставок изображений"""
        self.image_insertions += count

    def add_image_found(self):
        """Увеличить счетчик найденных изображений"""
        self.images_found += 1

    def add_image_not_found(self):
        """Увеличить счетчик не найденных изображений"""
        self.images_not_found += 1

    def add_document_created(self):
        """Увеличить счетчик созданных документов"""
        self.documents_created += 1

    def add_error(self):
        """Увеличить счетчик ошибок"""
        self.errors += 1

    def get_summary(self):
        """Получить сводку статистики"""
        return {
            'documents_created': self.documents_created,
            'text_replacements': self.text_replacements,
            'image_insertions': self.image_insertions,
            'images_found': self.images_found,
            'images_not_found': self.images_not_found,
            'errors': self.errors
        }

    def get_formatted_summary(self):
        """Получить форматированную сводку"""
        total_images = self.images_found + self.images_not_found

        summary = [
            f"📄 Документов создано: {self.documents_created}",
            f"📝 Замен текста: {self.text_replacements}",
            f"🖼️ Изображений вставлено: {self.image_insertions}",
        ]

        if total_images > 0:
            summary.append(f"✅ Изображений найдено: {self.images_found}/{total_images}")
            summary.append(f"❌ Изображений не найдено: {self.images_not_found}/{total_images}")

        if self.errors > 0:
            summary.append(f"⚠️ Ошибок: {self.errors}")

        return summary

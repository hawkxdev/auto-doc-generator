#!/bin/bash

# Автозапуск демо-версии Auto Document Generator для macOS/Linux

echo "🚀 Auto Document Generator - Демо версия"
echo "=========================================="

# Проверка наличия uv
if ! command -v uv &>/dev/null; then
    echo "❌ uv не установлен. Устанавливаем..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

echo "📦 Установка зависимостей..."
uv sync

echo "🎯 Запуск демо-версии..."
echo ""

uv run python main.py

echo ""
echo "✅ Выполнение завершено!"
echo "📄 Проверьте папку output/word/ для созданных документов"

# Пауза перед закрытием (для двойного клика)
read -p "Нажмите Enter для выхода..."

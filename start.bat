@echo off
chcp 65001 >nul

REM Автозапуск демо-версии Auto Document Generator для Windows

echo 🚀 Auto Document Generator - Демо версия
echo ==========================================

REM Проверка наличия uv
where uv >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ uv не установлен. Установите uv с https://astral.sh/uv/
    echo    Или используйте: winget install astral-sh.uv
    pause
    exit /b 1
)

echo 📦 Установка зависимостей...
call uv sync

echo 🎯 Запуск демо-версии...
echo.

call uv run python main.py

echo.
echo ✅ Выполнение завершено!
echo 📄 Проверьте папку output\word\ для созданных документов

REM Пауза перед закрытием
pause

# SimpleAITextTGBot

Telegram-бот для анализа текста через DeepSeek API. Название бота в Telegram: `@SimpleKillerGrassTextBot`

## Возможности
- Анализ текста с помощью AI (DeepSeek API)
- Простая интеграция с Telegram
- Чистая архитектура (разделение на модули)
- Обработка ошибок и демо-режим

## Технологии
- Python 3.8+
- Aiogram 3.x (асинхронный Telegram-бот)
- DeepSeek API (или фейковый анализатор)
- Python-dotenv (для конфигурации)

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/UbicaTravy/SimpleAITextTGBot.git
   cd SimpleAITextTGBot
Установите зависимости:

```
pip install -r requirements.txt
```
Создайте файл .env:

```
BOT_TOKEN=ваш_токен_бота
DEEPSEEK_API_KEY=ваш_api_ключ
```
Запустите бота:

```
python -m bot.main
```
# Конфигурация
Настройки в config.py:

```
BOT_TOKEN = os.getenv('BOT_TOKEN')  # Получает токен из .env
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')  # Ключ API DeepSeek
```
📂 Структура проекта
text
bot/
├── .env
├── config.py
├── main.py
├── handlers/
│   ├── common.py       # Базовые команды (/start, /help)
│   └── text_analysis.py # Обработка текста
└── services/
    └── analyzer.py     # Интеграция с DeepSeek API
# 💡 Примеры использования
Отправьте боту любой текст:

```
Привет! Как дела?
```
Бот ответит анализом:

```
🔍 Анализ DeepSeek:
Текст носит нейтрально-позитивный характер...
```
# 📝 Лицензия
См. файл LICENSE.

При отсутствии API-ключа бот переходит в демо-режим
Для работы с DeepSeek API требуется активный аккаунт

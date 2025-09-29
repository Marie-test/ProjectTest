Фреймворк для автоматического тестирования API с использованием pytest и Allure отчетов.

## Возможности

- Тестирование REST API
- Allure отчеты
- Интеграция с GitHub Actions
- Поддержка различных HTTP методов

## Установка

```bash
git clone https://github.com/Marie-test/ProjectTest.git
cd ProjectTest
pip install -r requirements.txt
```

# Структура проекта
```
ProjectTest/
├── .github/
│   └── workflows/
│       └── ci.yml           # CI/CD пайплайны
├── tests/
│   └── test_api.py          # Тесты API
├── utils/
│   └── api_client.py        # API клиент
├── requirements.txt          # Зависимости Python
├── .gitignore               # Игнорируемые файлы
└── README.md                # Документация
```

# Структура веток
```
main/           ← Стабильная версия
├── feature/*   ← Новые тесты/функции  
├── hotfix/*    ← Срочные исправления
└── gh-pages    ← Allure отчеты (авто-деплой)
```



# Allure Reports
Последний репорт: https://marie-test.github.io/ProjectTest/

Отчеты автоматически обновляются при каждом коммите в main

# Development Workflow
1. Create feature branch: git checkout -b feature/new-tests
2. Develop tests: Добавьте тест-кейсы
3. Commit changes: git commit -m "Add new API tests"
4. Push branch: git push origin feature/new-tests
5. Create Pull Request в main
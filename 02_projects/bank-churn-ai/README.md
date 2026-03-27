# 🏦 BankChurn AI

> **Предсказание оттока клиентов банка и оценка кредитного риска с помощью машинного обучения**

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-В%20разработке-yellow)

---

## 📋 О проекте

**BankChurn AI** — учебный пет-проект по созданию ML-системы для прогнозирования поведения клиентов банка. Проект охватывает полный цикл Data Science: от сбора данных до деплоя модели.

### 🎯 Проблема
Банки теряют доход из-за оттока клиентов. Своевременное предсказание ухода позволяет:
- Предлагать персональные бонусы и удерживать клиентов
- Снижать кредитные риски при выдаче займов
- Увеличивать пожизненную ценность клиента (LTV)

### 🚀 Цели проекта

| Этап | Цель | Статус |
|------|------|--------|
| 🔹 Базовый | Обучить модель с ROC-AUC > 0.85 | 🔄 В работе |
| 🔹 Продвинутый | Добавить интерпретируемость (SHAP) | ⏳ Запланировано |
| 🔹 Профи | Деплой API + мониторинг дрейфа данных | ⏳ Запланировано |

---

## ✨ Функционал

- ✅ Загрузка и предобработка табличных данных
- ✅ Разведочный анализ (EDA) с визуализацией
- ✅ Обучение моделей: Logistic Regression, Random Forest, CatBoost
- ✅ Оценка метрик: Accuracy, Precision, Recall, ROC-AUC, F1
- ✅ Объяснение предсказаний (feature importance, SHAP)
- ✅ Экспорт модели в pickle/onnx
- ✅ API для предсказаний (FastAPI) — в разработке
- ✅ Дашборд для бизнес-пользователей (Streamlit) — в разработке


---

## 🛠 Технологический стек

| Категория | Инструменты |
|-----------|-------------|
| **Язык** | Python 3.10+ |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Machine Learning** | Scikit-learn, CatBoost, XGBoost |
| **Explainability** | SHAP, Lime |
| **API & Deployment** | FastAPI, Docker, MLflow |
| **Version Control** | Git, GitHub, DVC |
| **Testing** | Pytest |

---

## 📁 Структура проекта

```text
bank-churn-ai/
├── 📂 data/
│ ├── raw/ # Исходные данные (не изменять)
│ ├── processed/ # Очищенные данные
│ └── external/ # Сторонние датасеты
├── 📂 notebooks/
│ ├── 01_eda.ipynb # Разведочный анализ
│ ├── 02_feature_eng.ipynb # Feature Engineering
│ └── 03_modeling.ipynb # Обучение моделей
├── 📂 src/
│ ├── init.py
│ ├── config.py # Конфигурация проекта
│ ├── data_loader.py # Загрузка данных
│ ├── preprocessing.py # Предобработка
│ ├── features.py # Генерация признаков
│ ├── models/
│ │ ├── base.py
│ │ ├── churn_model.py
│ │ └── risk_model.py
│ ├── evaluation.py # Метрики и валидация
│ └── predict.py # Инференс
├── 📂 models/ # Сохранённые модели (.pkl, .onnx)
├── 📂 tests/ # Юнит-тесты
├── 📂 api/ # FastAPI приложение
├── 📂 dashboard/ # Streamlit дашборд
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/Kristina110205/ds-portfolio-nazdracheva.git
cd bank-churn-ai
```

### 2. Создание виртуального окружения
# Windows
```bash
python -m venv venv
venv\Scripts\activate
```

# macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Запуск EDA
```bash
jupyter notebook notebooks/01_eda.ipynb
```

### 5. Обучение модели
```bash
python src/models/churn_model.py --data data/processed/train.csv
```

## 📊 Данные

### Источники
- **Kaggle:** [Bank Churn Dataset](https://www.kaggle.com/datasets)
- **Синтетические данные** для отладки

### Описание признаков

| Признак | Тип | Описание |
|---------|-----|----------|
| `customer_id` | ID | Уникальный идентификатор |
| `age` | int | Возраст клиента |
| `balance` | float | Баланс счёта |
| `credit_score` | int | Кредитный рейтинг |
| `tenure` | int | Лет сотрудничества с банком |
| `num_products` | int | Кол-во продуктов банка |
| `is_active_member` | bool | Активность в приложении |
| `estimated_salary` | float | Предполагаемый доход |
| `churn` | **target** | 1 = ушёл, 0 = остался |

---

## 📈 Метрики качества

| Метрика | Формула | Почему важна |
|---------|---------|--------------|
| **Accuracy** | `(TP+TN)/Total` | Общая точность |
| **Precision** | `TP/(TP+FP)` | Минимизация ложных срабатываний |
| **Recall** ⭐ | `TP/(TP+FN)` | Не пропустить уходящих клиентов |
| **F1-Score** | `2×(P×R)/(P+R)` | Баланс точности и полноты |
| **ROC-AUC** | Площадь под кривой | Качество ранжирования |

> 💡 **Приоритет:** В задаче оттока важнее максимизировать **Recall** — лучше ложно предупредить уход, чем пропустить реального "беглеца".

---

## 🗓 Дорожная карта

```mermaid
gantt
    title План развития BankChurn AI
    dateFormat  YYYY-MM-DD
    
    section Базовый уровень
    Сбор данных и EDA       :         2027-01-01, 14d
    Предобработка           :         2027-01-15, 10d
    Базовые модели          :         2027-01-25, 14d
    
    section Продвинутый уровень
    Ансамбли и тюнинг       :         2027-02-10, 14d
    Feature Engineering     :         2027-02-24, 14d
    Интерпретация (SHAP)    :         2027-03-10, 10d
    
    section Профи / Продакшн
    API на FastAPI          :         2027-03-20, 14d
    Docker + деплой         :         2027-04-03, 14d
    Мониторинг дрейфа       :         2027-04-17, 14d

---

## 🤝 Как внести вклад

Мы всегда рады вашему участию! Следуйте этим шагам:

1. **Форкните** репозиторий
2. **Создайте ветку** для вашей фичи:
   ```bash
   git checkout -b feature/amazing-feature
3. Закоммитьте изменения:
git commit -m 'Add: amazing feature'
4. Запушьте ветку:
git push origin feature/amazing-feature
5. Откройте Pull Request

## 🧪 Тестирование
# Запустить все тесты
pytest tests/

# Проверить стиль кода
flake8 src/

# Проверить форматирование
black --check src/

# Запустить конкретный тест
pytest tests/test_model.py -v


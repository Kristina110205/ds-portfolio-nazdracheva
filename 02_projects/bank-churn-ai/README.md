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
git clone https://github.com/Kristina110205/ds-portfolio-nazdracheva/new/main/02_projects/bank-churn-ai.git
cd bank-churn-ai

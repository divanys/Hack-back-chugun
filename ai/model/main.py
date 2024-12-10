import tensorflow as tf
from tensorflow import keras as ks
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Загружаем данные
df = pd.read_csv("./model/data/dataset_for_nn.csv")

# Проверка на пустые значения
if df.isnull().values.any():
    print("Данные содержат пустые значения!")
    print(df.isnull().sum())

# Преобразуем столбец "Классы" в числовой формат, если он текстовый
df["Классы"] = pd.to_numeric(df["Классы"], errors='coerce')  # Преобразует все некорректные значения в NaN

# Удаляем строки с некорректными значениями в "Классы"
df = df.dropna(subset=["Классы"])

# Проверка, что в "Классы" нет пустых значений
print(f"Количество строк после удаления: {len(df)}")

# Убедимся, что классы теперь целые числа и корректно отсортированы
df["Классы"] = df["Классы"].astype(int)

# Объединяем хобби и рекомендации в одну строку
df["combined_text"] = df["Хобби"].astype(str) + " " + df["Рекомендации"].astype(str)

# Преобразуем текстовые данные в числовой вид
vectorizer = TfidfVectorizer(max_features=500)  # Используем до 500 самых популярных слов
X = vectorizer.fit_transform(df["combined_text"]).toarray()  # Преобразуем текст в числовой формат
y = df["Классы"].astype(int) - 1  # Классы от 0 до 9 для нейросети

# Проверяем размеры X и y
print(f"Размер X: {X.shape}, Размер y: {y.shape}")

# Разделяем данные на обучение и тест
if X.shape[0] == 0 or y.shape[0] == 0:
    raise ValueError("Данные пусты после обработки. Проверьте входной CSV-файл.")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создаем модель
model = ks.models.Sequential([
    ks.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    ks.layers.Dense(64, activation='relu'),
    ks.layers.Dense(10, activation='softmax')  # 10 классов
])

# Компилируем модель
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Обучаем модель
model.fit(X_train, y_train, epochs=10, batch_size=16, validation_split=0.2)

# Оцениваем модель
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Точность: {accuracy * 100:.2f}%")

# Функция предсказания
def predict_class(hobby_text, recommendation_text):
    combined_input = hobby_text + " " + recommendation_text
    vectorized_input = vectorizer.transform([combined_input]).toarray()
    prediction = model.predict(vectorized_input)
    return prediction.argmax() + 1  # Возвращаем класс (1-10)

# Пример использования
hobby_example = "игры на компьютере, программирование"
recommendation_example = "Студент интересуется технологиями. Рекомендуется изучить алгоритмы."
print("Предсказанный класс:", predict_class(hobby_example, recommendation_example))

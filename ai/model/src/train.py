import tensorflow as tf
from tensorflow import keras as ks
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import joblib

# Загружаем данные
def load_data():
    df = pd.read_csv("./model/data/dataset_for_nn.csv")
    
    # Проверка на пустые значения
    if df.isnull().values.any():
        print("Данные содержат пустые значения!")
        print(df.isnull().sum())

    # Преобразуем столбец "Классы" в числовой формат
    df["Классы"] = pd.to_numeric(df["Классы"], errors='coerce')
    df = df.dropna(subset=["Классы"])

    df["Классы"] = df["Классы"].astype(int)

    # Объединяем хобби и рекомендации
    df["combined_text"] = df["Хобби"].astype(str) + " " + df["Рекомендации"].astype(str)
    
    return df

def preprocess_data(df):
    # Преобразуем текстовые данные в числовой вид
    vectorizer = TfidfVectorizer(max_features=500)
    X = vectorizer.fit_transform(df["combined_text"]).toarray()
    y = df["Классы"].astype(int) - 1  # классы от 0 до 9 для нейросети
    return X, y, vectorizer

def train_and_save_model(X, y, vectorizer):
    # Разделяем данные на обучение и тест
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

    model.fit(X_train, y_train, epochs=10, batch_size=16, validation_split=0.2)
    
    # Оценка точности
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Точность: {accuracy * 100:.2f}%")
    
    # Сохраняем модель и векторизатор
    model.save('./model/data/my_model.h5')
    joblib.dump(vectorizer, './model/data/vectorizer.pkl')

def main():
    df = load_data()
    X, y, vectorizer = preprocess_data(df)
    train_and_save_model(X, y, vectorizer)

if __name__ == "__main__":
    main()

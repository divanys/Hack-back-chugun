import tensorflow as tf
import joblib
import numpy as np

# Загрузка модели и векторизатора
def load_model_and_vectorizer():
    model = tf.keras.models.load_model('./model/data/my_model.h5')
    vectorizer = joblib.load('./model/data/vectorizer.pkl')
    return model, vectorizer

# Предсказание класса
def predict_classes(hobby_example, recommendation_example):
    # Загружаем модель и векторизатор
    model, vectorizer = load_model_and_vectorizer()
    
    # Подготовим данные
    combined_input = hobby_example + " " + recommendation_example
    vectorized_input = vectorizer.transform([combined_input]).toarray()
    
    # Получаем предсказание
    predictions = model.predict(vectorized_input)
    return predictions.argmax(axis=1) + 1  # возвращаем массив классов (от 1 до 10)

def main():
    hobby_example = ["Docker", "программирование"]
    recommendation_example = ["Проявляет хорошие навыки. Рекомендуется углубить знания о backend",
                              "Увлекается Python, но больше практики. Рекомендуется освоить библиотеки Python, например, pandas и numpy"]
    
    result = []
    for i in range(len(recommendation_example)):
        result.append(predict_classes(hobby_example[i], recommendation_example[i]))

    print("Предсказанные классы:", result)

if __name__ == "__main__":
    main()

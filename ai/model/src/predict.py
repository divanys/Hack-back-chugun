import tensorflow as tf
import joblib
import numpy as np

# Загрузка модели и векторизатора
def load_model_and_vectorizer():
    model = tf.keras.models.load_model('./model/data/my_model.h5')
    vectorizer = joblib.load('./model/data/vectorizer.pkl')
    return model, vectorizer

# Словарь с текстовыми значениями для классов
class_map = {
    1: "программирование",
    2: "python",
    3: "java",
    4: "backend",
    5: "frontend",
    6: "нейронные сети",
    7: "математика",
    8: "аналитика данных",
    9: "fullstack",
    10: "сети и связь"
}

# Функция для предсказания классов
def predict_classes(hobby_example, recommendation_example):
    model, vectorizer = load_model_and_vectorizer()
    
    combined_input = hobby_example + " " + recommendation_example
    vectorized_input = vectorizer.transform([combined_input]).toarray()
    
    predictions = model.predict(vectorized_input)
    predicted_classes = predictions.argmax(axis=1) + 1  # возвращаем массив классов (от 1 до 10)
    
    predicted_labels = [class_map[class_id] for class_id in predicted_classes]
    
    return predicted_labels

def main():
    hobby_example = ["Docker", "программирование"]
    recommendation_example = [
        "Проявляет хорошие навыки. Рекомендуется углубить знания о backend",
        "Ты лучше работаешь с графами данных на backend, чем с интерфейсами на фронтенде. Рекомендуется изучить работу с графами с использованием библиотеки Neo4j"
    ]
    
    result = []
    for i in range(len(recommendation_example)):
        result.extend(predict_classes(hobby_example[i], recommendation_example[i]))  # используем extend для добавления в тот же список

    # print("Предсказанные классы:", result)

if __name__ == "__main__":
    main()

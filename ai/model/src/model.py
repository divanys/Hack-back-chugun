import tensorflow as tf

# Модель для классификации
def create_model(input_size=40, output_size=5):
    input_rec = tf.keras.Input(shape=(input_size,))
    input_hob = tf.keras.Input(shape=(input_size,))

    # Обработаем данные
    x_rec = tf.keras.layers.Dense(128, activation='relu')(input_rec)
    x_hob = tf.keras.layers.Dense(128, activation='relu')(input_hob)

    # Объединяем информацию с двух источников
    merged = tf.keras.layers.concatenate([x_rec, x_hob])

    # Прогоняем через несколько слоев
    x = tf.keras.layers.Dense(256, activation='relu')(merged)
    x = tf.keras.layers.Dense(128, activation='relu')(x)
    output = tf.keras.layers.Dense(output_size, activation='sigmoid')(x)  # Sigmoid для многоклассовой классификации

    model = tf.keras.models.Model(inputs=[input_rec, input_hob], outputs=output)
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
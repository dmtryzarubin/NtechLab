import sys
import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Прочитаем адрес папки из командной строки
TEST_PATH = sys.argv[1]

# Загрузка модели
model = tf.keras.models.load_model('Gender_2.h5') # Загружаем модель

# Функция, которая создает словарь с предсказаниями модели
def test_data(test_path):
    
    predictions = dict()

    for img in os.listdir(test_path):
        
        # Загрузка изображения
        img1 = image.load_img(test_path + '/' + img, target_size=(96, 96, 3))
        img_tensor = image.img_to_array(img1) 
        
        # Делим каждое значение изображения на 255 
        img_tensor /= 255

        # Reshape нужен для передачи изображения в модель
        img_tensor = img_tensor.reshape(1, 96, 96, 3)
        
        # Генерация предсказания для изображения
        Y_pred = np.round(model.predict(img_tensor))
        
        # Добавление метки в словарь
        if Y_pred[0,0] == 1:
            predictions[img] = 'male'
        
        elif Y_pred[0,0] == 0:
            predictions[img] = 'female'
         
    return  predictions

preds = test_data(TEST_PATH)

# Запись в файл .json
with open("process_results.json", "w") as outfile:  
    json.dump(preds, outfile)
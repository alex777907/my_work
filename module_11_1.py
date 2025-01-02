import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

# Чтение данных из CSV файла
df = pd.read_csv('data.csv')

# Анализ данных с помощью Pandas
summary = df.describe()
print(summary)

# Визуализация данных с помощью Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(df['column1'], df['column2'], label='Data')
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.title('Data Visualization')
plt.legend()
plt.show()

# Открытие изображения с помощью Pillow
image = Image.open('example.jpg')

# Применение эффекта размытия
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('blurred_image.png')

# Изменение размера изображения
resized_image = image.resize((800, 600))
resized_image.save('resized_image.png')

print("Обработка данных и изображений завершена.")

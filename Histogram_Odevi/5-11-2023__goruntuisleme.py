import numpy as np
import cv2
import matplotlib.pyplot as plt

#Resmi gri bir tona dönüştürdüm
image = cv2.imread("bw_cherry.png", cv2.IMREAD_GRAYSCALE)

# Histogramı hesaplamak için boş liste oluşturdum.
histogram = [0] * 256

# Her pikselin gri seviyesini tarandı ve histogramı hesaplandı.
for row in image:
    for pixel_value in row:
        histogram[pixel_value] += 1

# Histogram ekrana yazdırıldı.
for i, count in enumerate(histogram):
    print(f'Gri Seviye {i}: {count} piksel')

#Histogram grafiği gösterildi
plt.figure(figsize=(10, 5))
plt.bar(range(256), histogram, color='black')
plt.title("Gri Seviye Histogramı")
plt.xlabel("Gri Seviye")
plt.ylabel("Piksel Sayısı")
plt.show()
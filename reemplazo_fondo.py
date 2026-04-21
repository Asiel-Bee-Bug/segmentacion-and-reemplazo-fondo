import cv2
import numpy as np

lista_areas = []

# Cargar la imagen
imagen = cv2.imread('josuke.png')

# Cargar paisaje
paisaje = cv2.imread('fondog.jpg')

# Ajustar tamaño del paisaje (IMPORTANTE)
alto, ancho, canales = imagen.shape
paisaje = cv2.resize(paisaje, (ancho, alto))

# Suavizar la imagen
imagen = cv2.GaussianBlur(imagen, (3, 3), 1.4)

# Crear máscara en negro (1 canal)
img = np.zeros((alto, ancho), np.uint8)

# Aplicar Canny
bordes = cv2.Canny(imagen, 10, 100, apertureSize=3, L2gradient=True)

# Aplicar closing
kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(bordes, cv2.MORPH_CLOSE, kernel)

# Encontrar contornos
contornos, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Calcular áreas
for i in range(len(contornos)):
    area = cv2.contourArea(contornos[i])
    lista_areas.append(area)

# Obtener contorno más grande
area_max = max(lista_areas)
contorno_max = lista_areas.index(area_max)
cnt = contornos[contorno_max]

# Dibujar máscara (objeto en blanco)
cv2.drawContours(img, [cnt], 0, 255, cv2.FILLED)

# Aplicar máscaras (AQUÍ TU CAMBIO)
mascara1 = cv2.bitwise_and(imagen, imagen, mask=img)
mascara2 = cv2.bitwise_and(paisaje, paisaje, mask=cv2.bitwise_not(img))

# Combinar imágenes
imagenFinal = cv2.add(mascara1, mascara2)

# Mostrar resultados
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Contornos Detectados Closing', closing)
cv2.imshow('Mascara', mascara1)
cv2.imshow('Paisaje', mascara2)
cv2.imshow('Imagen Final', imagenFinal)

cv2.waitKey(0)
cv2.destroyAllWindows()
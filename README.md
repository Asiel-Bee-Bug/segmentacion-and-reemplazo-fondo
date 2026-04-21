# 🎭 Reemplazo de Fondo con Segmentación en OpenCV

Este proyecto realiza la segmentación de un objeto principal en una imagen utilizando detección de bordes y contornos, para posteriormente reemplazar su fondo por otra imagen.

## 🚀 Funcionalidades

* Detección de bordes con Canny
* Aplicación de operaciones morfológicas (Closing)
* Detección de contornos
* Selección del objeto principal (contorno de mayor área)
* Creación de máscara binaria
* Reemplazo de fondo con otra imagen

## 🛠️ Tecnologías utilizadas

* Python
* OpenCV
* NumPy

## ▶️ Cómo ejecutar

1. Clona el repositorio:

```bash id="git3x1"
git clone https://github.com/tu-usuario/image-segmentation-background-replacement.git
```

2. Entra a la carpeta:

```bash id="cd3x1"
cd image-segmentation-background-replacement
```

3. Instala dependencias:

```bash id="pip3x1"
pip install opencv-python numpy
```

4. Asegúrate de tener las imágenes en la carpeta:

```id="imgnames3x1"
josuke.png
fondog.jpg
```

5. Ejecuta el programa:

```bash id="run3x1"
python background_replace.py
```

## 🧠 ¿Cómo funciona?

1. Se detectan bordes usando Canny
2. Se aplica un filtro morfológico (closing) para mejorar los contornos
3. Se detectan todos los contornos en la imagen
4. Se selecciona el contorno con mayor área (objeto principal)
5. Se genera una máscara binaria del objeto
6. Se combinan:

   * Objeto original
   * Fondo nuevo

## 📌 Notas

* Ambas imágenes deben tener dimensiones compatibles (el programa ajusta automáticamente el fondo)
* Puedes cambiar:

  * Valores de Canny (`10, 100`)
  * Tamaño del kernel `(5,5)`
* Funciona mejor con imágenes donde el objeto esté bien definido

## 🎯 Objetivo

Practicar técnicas básicas de visión por computadora como segmentación, detección de contornos y manipulación de imágenes.

## 👨‍💻 Autor

Proyecto académico enfocado en procesamiento de imágenes.

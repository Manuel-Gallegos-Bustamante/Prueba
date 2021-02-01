# ESTO ES UNA PRUEBA!!!
# librerías utilizadas
import numpy as np
import requests
import skimage.io as io
from skimage.color import rgb2gray
from matplotlib import pyplot as plt

# variable que almacena la imagen
r = requests.get("https://assets.entrepreneur.com/content/3x2/2000/20181105214106-GettyImages-824977200.jpeg")
#lectura de imagen, se guarda como cebras
with open('cebras', 'wb') as f:
    f.write(r.content)
# se lee la imagen y se transforma a escala de gris en otra variable
color = io.imread("cebras")
grises = rgb2gray(color)
# se estrae el canal de la variable color, es decir la imagen, para cada color: rojo, verde y azul
rojo = color[:,:,0]
verde = color[:,:,1]
azul = color[:,:,2]

# se crea una figura y se ubican las imagenes. En este caso no se utilizan ejes.
plt.figure()
plt.subplot(2,2,1)
plt.imshow(color)
plt.title("Original")
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(rojo, cmap='gray')
plt.title("Canal rojo")
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(verde, cmap='gray')
plt.title("Canal verde")
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(azul, cmap='gray')
plt.title("Canal azul")
plt.axis('off')
plt.show()
# se pide oprimir una tecla para continuar

# se guarda la imagen con el nombre especificado.
plt.savefig("comparacionCanales")

# se combierten las imagenes en vectores
vectorGrises = grises.flatten()
vectorColor = color.flatten()

# se muestran los histograms y las imagenes en una sola figura.
plt.figure()
plt.subplot(2,2,1)
plt.imshow(color)
plt.title("Original")
plt.axis('off')

plt.subplot(222)
plt.hist(vectorColor)
plt.title("Histograma Imagen a Color")

plt.subplot(2,2,3)
plt.imshow(grises, cmap='gray')
plt.title("Escala de Grises")
plt.axis('off')

plt.subplot(224)
plt.hist(vectorGrises)
plt.title("Histograma Escala de Grises")
plt.show()
# se guarda la imagen con el nombre especificado.
plt.savefig("Histogramas")

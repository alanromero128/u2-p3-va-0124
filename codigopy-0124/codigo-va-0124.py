# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os
#ruta de la imagen
ruta_imagen= os.path.join(
    "img-original-0124",
    "purificador.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
purificador = cv2.imread(ruta_imagen)
#print (purificador)muestra las matrices de la imagen
#Convertir de BGR a RGB color rojo COLOR_BGR2RGB
puri= cv2.cvtColor(purificador, cv2.COLOR_BGR2RGB)
cv2.imshow("Purificador original 0124",purificador)
cv2.imshow("Purificador color 0124",puri)
cv2.waitKey(0)#Tiempo de espera
cv2.destroyAllWindows() #destruye todas las ventanas en memoria
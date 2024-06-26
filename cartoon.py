import cv2
import numpy as np
import os

image = cv2.imread("foto.jpg")

if image is None:
    print("Erro ao carregar a imagem.")
    
else:

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    cv2.imshow("Image", image)
    cv2.imshow("Edges", edges)
    cv2.imshow("Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
    
#Para testar se o caminho da foto que você colocou está correto.
# image_path = "foto.jpg"

# if os.path.exists(image_path):
#     print("O arquivo existe.")
# else:
#     print("O arquivo não foi encontrado.")


import cv2

# Caminho para a imagem
caminho_imagem = "solar-system.jpg"

# Lê a imagem usando cv2.imread()
img = cv2.imread(caminho_imagem)

# Adiciona texto abaixo de cada planeta usando putText()
cv2.putText(img, "Mercúrio", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
cv2.putText(img, "Vênus", (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
cv2.putText(img, "Terra", (500, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
cv2.putText(img, "Marte", (700, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
cv2.putText(img, "Júpiter", (900, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
cv2.putText(img, "Saturno", (1100, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
cv2.putText(img, "Urano", (1300, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
cv2.putText(img, "Netuno", (1500, 800), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))

# Exibe a imagem com o texto
cv2.imshow("resultado", img)

# Aguarda uma tecla ser pressionada
cv2.waitKey(0)

# Salva a imagem com o texto adicionado
cv2.imwrite("Solar_systemwithname.jpg", img)

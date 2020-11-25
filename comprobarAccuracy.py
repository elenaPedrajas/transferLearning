real = open("validacion.csv", "r")
real_imagen = []
real_clase = []
for linea in real:
    real_imagen.append(linea.split(';')[0])
    real_clase.append(linea.split(';')[1])

pred = open("output.csv", "r")
pred_imagen = []
pred_clase = []
for linea in pred:
    pred_imagen.append(linea.split(',')[0])
    pred_clase.append(linea.split(',')[1])

accuracy = 0
for i,nombre_img_pred in enumerate(pred_imagen):
    for j,nombre_img_real in enumerate(real_imagen):
        if nombre_img_real == nombre_img_pred:
            if real_clase[j]==pred_clase[i]:
                accuracy= accuracy+1

accuracy=accuracy/len(real_imagen)
print(accuracy)
"""
written by jorge orlando miranda ñahui
"""
#importar los modulos necesarios
import numpy as np
import cv2,sys
camara=cv2.VideoCapture(0)
#definir umbral minimo azul hsv
min_azul=np.array([100,80,75])
#umbral maximo azul hsv
max_azul=np.array([120,255,255])

while True:
    #leer las imagenes o frames de la camara(BGR)
    estado,frame=camara.read()
    frame=cv2.resize(frame,(640,640),cv2.INTER_AREA)
    #---determinar el nivel de brillo -----

    #----adpatar histograma para mejorar el constraste en la imagen-----

    #cambiar escala BGR a HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #---binarizar la imagen hsv con la función inRange---
    mascara_azul=cv2.inRange(hsv,min_azul,max_azul)
    #operación de erosión
    kernel1=255*np.ones((5,5),dtype=int)
    #mascara_azul=cv2.morphologyEx(mascara_azul,cv2.MORPH_OPEN,kernel=kernel1)
    #erosioón de la imagen binaria de entrada (mascara_azul)
    mascara_azul_erosion=cv2.erode(mascara_azul,kernel=kernel1,iterations=1)
    mascara_azul_dilatada=cv2.dilate(mascara_azul_erosion,kernel=kernel1,iterations=1)
    mascara_azul_erosion = cv2.erode(mascara_azul, kernel=kernel1, iterations=2)
    mascara_azul_dilatada = cv2.dilate(mascara_azul_erosion, kernel=kernel1, iterations=3)
    mascara_azul=mascara_azul_dilatada.copy()
    cv2.imshow("MASCARA DE REGION AZUL",mascara_azul)
    #realizar una copia
    m2=mascara_azul.copy()
    #encontrar componentes convexos mediante la conectividad 8
    n_labels, labels = cv2.connectedComponents(mascara_azul,connectivity=8)
    #etiquetas de cada objeto en una lista por compresion
    l1 = [a for a in range(1, n_labels, 1)]
    #por cada etiqueta determinar si superan una cantidad de pixeles
    cont=0
    for lb in l1:
        #determinar la cantidad de pixels por cada etiqueta
        area=labels==lb
        areac=area.copy()
        narea=np.count_nonzero(area)
        if narea>=47*39:
            cont=cont+1
        else:
            #retornar las posiciones donde no supera el umbral
            lugar=np.where(areac==True)
            if len(lugar)!=0:
                print("lugar")
                #filas
                x=lugar[0]
                #columans
                y=lugar[1]
                #para cada fila y columna
                for a,b in zip(x,y):
                    #poner en cero cada pixel
                    m2[a,b] = 0
        # operación and entre la mascara y la imagen BGR

    solo_azul = cv2.bitwise_and(frame, frame, mask=m2)
    #encontrar contornos en la imagen m2
    image, contours, hierarchy = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("contornos",len(contours))
    #copia del frame de la camara
    frame2=frame.copy()
    #determinar las jerarquias de los contornos
    if hierarchy is not None:
        print("jerarquia", hierarchy.shape)
        #determinar si son contornos de la misma jerarquia
        jerarquias=hierarchy[0]
        #para cada contorno y jerarquia
        for indice,contj in enumerate(jerarquias):
            #contornos de la misma jerarquia
            if contj[2]==-1:
                #graficar dicho contorno
                # por cada punto del contorno
                for punto in contours:
                    #mostrar el indice asociado a cada contorno encontrado
                    print("INDICES",indice)
                    #convertir puntos de los contornos en una region rectangular
                    x, y, w, h = cv2.boundingRect(contours[indice])
                    #determinar que el area del rectangulo sea menor que el frame
                    area_contorno=(x+w)*(y+h)
                    #obtener dimensiones del frame de la imagen
                    if area_contorno<=640*640-11*11:
                        img = cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    #img = cv2.drawContours(frame2, contours, indice, (0, 255, 0), 3)
                    #enmarcar el contorno mediante un rectangulo
    cv2.imshow("IMAGEN BINARIA AZUL MEJORADA",m2)
    cv2.imshow("IMAGEN BGR CON LOS CONTORNOS",frame2)
    #ESPERAR TECLA q para cerrar
    if cv2.waitKey(1)==ord("q"):
        break
#Liberar el uso de la camara del ordenador, método release()
camara.release()
#luego de liberar , cerrar las ventanas
cv2.destroyAllWindows()

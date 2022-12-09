import cv2
import numpy as np
from time import sleep
	
def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

def count_vehicles(video, video_vehicle):
    largura_min = 40  # Largura minima do retangulo
    altura_min = 40  # Altura minima do retangulo

    offset = 6  # Erro permitido entre pixel

    delay = 60  # FPS do vídeo

    detec = []
    carros = 0
    cap = cv2.VideoCapture('media/'+str(video))
    subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    pos_linha=int(height-150) #Posição da linha de contagem

    file_output = 'media/videos/output-' + str(video).split('/')[1]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter(file_output, fourcc, 30, (width, height))

    while True:
        ret , frame1 = cap.read()
        if frame1 is None:
            break
        tempo = float(1/delay)
        sleep(tempo)
        grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey,(3,3),5)
        img_sub = subtracao.apply(blur)
        dilat = cv2.dilate(img_sub,np.ones((5,5)))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
        dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
        contorno,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        cv2.line(frame1, (15, pos_linha), (width-15, pos_linha), (255,127,0), 3)
        for(i,c) in enumerate(contorno):
            (x,y,w,h) = cv2.boundingRect(c)
            validar_contorno = (w >= largura_min) and (h >= altura_min)
            if not validar_contorno:
                continue

            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            centro = pega_centro(x, y, w, h)
            detec.append(centro)
            cv2.circle(frame1, centro, 4, (0, 0,255), -1)

            for (x,y) in detec:
                if y<(pos_linha+offset) and y>(pos_linha-offset):
                    carros+=1
                    cv2.line(frame1, (25, pos_linha), (width-25, pos_linha), (0,127,255), 3)
                    detec.remove((x,y))
                    print("car is detected : "+str(carros))

        cv2.putText(frame1, "VEHICLE COUNT : "+str(carros), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
        # cv2.imshow("Video Original" , frame1)
        # cv2.imshow("Detectar",dilatada)
        output.write(frame1)

        if ret == False:
            break
    cap.release()
    video_vehicle.video_output = 'videos/output-' + str(video).split('/')[1]
    video_vehicle.save()

    return carros

import numpy as np
import cv2 as cv

def rotate_image(image, angle):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    return cv.warpAffine(image, M, (w, h))

def scale_image(image, scale):
    h, w = image.shape[:2]
    new_size = (int(w * scale), int(h * scale))
    return cv.resize(image, new_size, interpolation=cv.INTER_LINEAR)

def run():
    cap = cv.VideoCapture(0)
    width = 320
    height = 240

    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    cv.namedWindow('Minha Imagem!')
    cv.createTrackbar('Rotation Angle', 'Minha Imagem!', 0, 360, lambda x: None)
    cv.createTrackbar('Scale', 'Minha Imagem!', 100, 300, lambda x: None)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não consegui capturar frame!")
            break

        frame = cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

        angle = cv.getTrackbarPos('Rotation Angle', 'Minha Imagem!')
        scale = cv.getTrackbarPos('Scale', 'Minha Imagem!') / 100.0  # Converte para fator de escala

        # Aplica as transformações
        scaled_image = scale_image(frame, scale)
        rotated_image = rotate_image(scaled_image, angle)

        cv.imshow('Minha Imagem!', rotated_image)

        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    run()

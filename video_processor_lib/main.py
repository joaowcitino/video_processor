import numpy as np
import cv2 as cv

def rotate_image(image, angle):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    return cv.warpAffine(image, M, (w, h))

def scale_image(image, scale):
    scale = max(0.65, min(scale, 1.75))
    h, w = image.shape[:2]
    new_size = (int(w * scale), int(h * scale))
    return cv.resize(image, new_size, interpolation=cv.INTER_LINEAR)

def apply_transformations(frame, angle, scale):
    scaled_image = scale_image(frame, scale)
    rotated_image = rotate_image(scaled_image, angle)
    return rotated_image

def run():
    cap = cv.VideoCapture(0)
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    cv.namedWindow('Minha Imagem!', cv.WINDOW_NORMAL)
    cv.resizeWindow('Minha Imagem!', width, height + 100)

    cv.createTrackbar('Rotation Angle', 'Minha Imagem!', 0, 360, lambda x: None)
    cv.createTrackbar('Scale', 'Minha Imagem!', 0, 100, lambda x: None)

    fps = 30
    delay = int(1000 / fps)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não consegui capturar frame!")
            break

        angle = cv.getTrackbarPos('Rotation Angle', 'Minha Imagem!')
        scale_percent = cv.getTrackbarPos('Scale', 'Minha Imagem!')
        scale = 0.65 + (scale_percent / 100.0) * (1.75 - 0.65)

        transformed_image = apply_transformations(frame, angle, scale)

        cv.imshow('Minha Imagem!', transformed_image)

        cv.resizeWindow('Minha Imagem!', transformed_image.shape[1], transformed_image.shape[0] + 100)

        if cv.waitKey(delay) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    run()
import numpy as np
import cv2 as cv

def rotate_image(image, angle):
    angle_rad = np.radians(angle)
    cos_angle = np.cos(angle_rad)
    sin_angle = np.sin(angle_rad)
    h, w = image.shape[:2]
    center = np.array([[w / 2], [h / 2]])

    rotation_matrix = np.array([[cos_angle, -sin_angle],
                                 [sin_angle, cos_angle]])

    rotated_image = np.zeros_like(image)

    for y in range(h):
        for x in range(w):
            original_coords = np.array([[x], [y]]) - center
            new_coords = rotation_matrix @ original_coords + center
            new_x, new_y = int(new_coords[0]), int(new_coords[1])

            if 0 <= new_x < w and 0 <= new_y < h:
                rotated_image[y, x] = image[new_y, new_x]

    return rotated_image

def scale_image(image, scale):
    scale = max(0.65, min(scale, 1.75))
    h, w = image.shape[:2]
    new_size = (int(w * scale), int(h * scale))
    scaled_image = np.zeros((new_size[1], new_size[0], 3), dtype=image.dtype)

    for y in range(new_size[1]):
        for x in range(new_size[0]):
            original_x = int(x / scale)
            original_y = int(y / scale)
            if 0 <= original_x < w and 0 <= original_y < h:
                scaled_image[y, x] = image[original_y, original_x]

    return scaled_image

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

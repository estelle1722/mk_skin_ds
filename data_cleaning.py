import cv2
import os
import numpy as np


def compute_gradient(path):
    img = cv2.imread(path)
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    return np.abs(sobel_x).mean() + np.abs(sobel_y).mean()


def main(path, keep=1200):
    results = dict()
    for name in os.listdir(path):
        abs_path = os.path.join(path, name)
        gradient = compute_gradient(abs_path)
        results[abs_path] = gradient
    results = sorted(results.items(), key=lambda item:item[1])
    assert len(results) > keep
    for idx, (key, _) in enumerate(results):
        if idx >= keep:
            os.remove(key)


if __name__ == '__main__':
    main('./ds/normal')
    main('./ds/lesion')

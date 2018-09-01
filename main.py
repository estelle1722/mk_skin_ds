"""
make dataset manually:
step 1:extract a portion of ISIC2017 and ImageNet
step 2:crop a part of image labeled normal from ISIC2017 as the healthy
step 3:attach ImageNet to healthy image as the lsion
"""
import shutil
import cv2
import random
import os

from util import clear


def crop_skin(im, height=64, width=64):
    """
    randomly crop a portion of original image with height*width from the top-left corner,the top-right corner,
    the button-left corner and the button-right corner respectively
    """
    h, w, _ = im.shape
    pos_x = random.randint(0, 100)
    pos_y = random.randint(0, 100)
    top_left = im[pos_y: (pos_y + height), pos_x: (pos_x + width), :]

    pos_x = random.randint(w - 200, w - 100)
    pos_y = random.randint(0, 100)
    top_right = im[pos_y: (pos_y + height), pos_x: (pos_x + width), :]

    pos_x = random.randint(0, 100)
    pos_y = random.randint(h - 200, h - 100)
    button_left = im[pos_y: (pos_y + height), pos_x: (pos_x + width), :]

    pos_x = random.randint(w - 200, w - 100)
    pos_y = random.randint(h - 200, h - 100)
    button_right = im[pos_y: (pos_y + height), pos_x: (pos_x + width), :]
    return top_left, top_right, button_left, button_right


def main(skin_data_dir, image_net_data_dir, target_path='ds'):
    """
    TODO: refactoring this function

    """
    path_lst = [os.path.join(skin_data_dir, name) for name in os.listdir(skin_data_dir)]
    image_net_lst = [os.path.join(image_net_data_dir, name) for name in os.listdir(image_net_data_dir)]
    clear(target_path)
    thred = len(path_lst) // 2
    idx = 0

    for nums, path in enumerate(path_lst, 0):
        im = cv2.imread(path)
        top_left, top_right, button_left, button_right = crop_skin(im)
        if nums < thred:
            # the lesion area nums with 1, 2, 3 account for 60%,30% and 10% respectively.
            rand_arr = [1, 2, 3, 2, 1, 1, 1, 2, 1, 1, 2]
            for _ in range(rand_arr[random.randint(0, 9)]):
                image_net_im = resize(image_net_lst[idx])
                top_left = attach(top_left, image_net_im)
                idx += 1
            saved_path = '%s/lesion_top_left_%s' % (target_path, path.split('/')[-1])
            cv2.imwrite(saved_path, top_left)

            for _ in range(rand_arr[random.randint(0, 9)]):
                image_net_im = resize(image_net_lst[idx])
                top_right = attach(top_right, image_net_im)
                idx += 1
            saved_path = '%s/lesion_top_right_%s' % (target_path, path.split('/')[-1])
            cv2.imwrite(saved_path, top_right)

            for _ in range(rand_arr[random.randint(0, 9)]):
                image_net_im = resize(image_net_lst[idx])
                button_left = attach(button_left, image_net_im)
                idx += 1
            saved_path = '%s/lesion_button_left_%s' % (target_path, path.split('/')[-1])
            cv2.imwrite(saved_path, button_left)

            for _ in range(rand_arr[random.randint(0, 9)]):
                image_net_im = resize(image_net_lst[idx])
                button_right = attach(button_right, image_net_im)
                idx+=1
            saved_path = '%s/lesion_button_right_%s' % (target_path, path.split('/')[-1])
            cv2.imwrite(saved_path, button_right)
        else:
            saved_path = '%s/normal_top_left_%s' % (target_path, path.split('/')[-1])
            cv2.imwrite(saved_path, top_left)

            saved_path = '%s/normal_top_right_%s' % (target_path, path.split('/')[-1])
            cv2.imwrite(saved_path, top_right)

            saved_path = '%s/normal_button_left_%s' % (target_path, path.split('/')[-1])
            cv2.imwrite(saved_path, button_left)

            saved_path = '%s/normal_button_right_%s' % (target_path, path.split('/')[-1])
            cv2.imwrite(saved_path, button_right)


def attach(skin_im, image_net_im):
    target_height, target_width, _ = skin_im.shape
    source_height, source_width, _ = image_net_im.shape
    pos_x = random.randint(0, target_width - source_width - 1)
    pos_y = random.randint(0, target_height - source_height - 1)
    skin_im[pos_y: (pos_y + source_height), pos_x: (pos_x + source_width), :] = image_net_im
    return skin_im


def resize(path, size=((2, 2), (4, 4), (8, 8))):
    im = cv2.imread(path)
    return cv2.resize(im, size[random.randint(0, len(size) - 1)])


if __name__ == '__main__':
    main('isic_2017', 'image_net')

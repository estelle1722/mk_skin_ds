import cv2
import os

from util import clear, copy


class Split(object):
    """
    Split NORMAL and LESION dataset into train and val part.
    In the mean time, resizing images will also be done
    """

    def __init__(self, source, train_path, val_path, percentage=0.8):
        self.source = source
        self.train_path = train_path
        self.val_path = val_path
        self.percentage = percentage

        for tag in self.source.keys():
            train_path = os.path.join(self.train_path, tag)
            val_path = os.path.join(self.val_path, tag)
            if os.path.exists(train_path):
                clear(train_path)
            else:
                os.makedirs(train_path)
            if os.path.exists(val_path):
                clear(val_path)
            else:
                os.makedirs(val_path)

    def __call__(self, *args, **kwargs):
        # iterate label-path dict to split these image labeled NORMAL_ and LESION
        for tag, path in self.source.items():
            images_lst = os.listdir(path)
            train_nums = int(self.percentage * len(images_lst))
            # iterate images list and copy these to responding directory(train and val) respectively
            for idx, name in enumerate(images_lst):
                abs_path = os.path.join(path, name)
                # if less than targeted training image nums: copy to train/NORMAL_ or train/LESION
                # else: copy to val/NORMAL_ or val/LESION(depend on the variable 'tag')
                target_path = os.path.join(self.train_path, tag, name) if idx < train_nums \
                    else os.path.join(self.val_path, tag, name)
                copy(abs_path, target_path)
                print('copy %s to %s' % (abs_path, target_path))


if __name__ == '__main__':
    # Split({'normal': './ds/8_8/normal', 'lesion': './ds/8_8/lesion'},
    #       './ds/8_8/train',
    #       './ds/8_8/val')()
    Split({'normal': './ds/4_4/normal', 'lesion': './ds/4_4/lesion'},
          './ds/4_4/train',
          './ds/4_4/val')()
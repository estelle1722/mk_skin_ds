# mk_skin_ds
This project intends to make custom-defined skin dataset with ISIC 2017 medical images and ImageNet.In other words,I want to attach images origining from ImageNet to skin images from ISIC 2017 so that the images containing images random selected from ImageNet can be seen as lesion.This project can be conducted by three steps as follows:

1. extract a portion of ISIC2017 and ImageNet
2. crop a part of image labeled normal from ISIC2017 as the healthy
3. attach ImageNet to healthy image as the lsion
4. only remain typical images to simplify this dataset

After that,I obtain a custom-defined dataset with 1,183 normal images and 1,114 lesion images.Finally,these images are  divided into training dataset and validate dataset.

## usage

Please run the script `main.py`:

```bash
python main.py
```

In this script,a original skin image will be cropped from corners,i.e.:the upper left corner,the lower left corner,the top right corner and the lower right corner.In the same time,a corresponding image from ImageNet will be selected and resized.Then a portion of the former will be replaced with the latter and saved to the disk.

Next,

In  fact,because of randomness in the processing of sampling,not all images are what we needs.Thus I just remain typical images.Running the script `data_cleaning.py` will achieve this purpose:

```bash
python data_cleaning.py
```

Note that I use *Sobel* operator to compute first-order gradient and keep images with small gradient because images with slow gradient means no dramatic changes in brightness in general.After passing through the steps above,I have picked up satisfying images.Next all I need to do is just to split these images into two part and use it to train neural network.

Please contact me if there are any questions.

## reference

- https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_gradients/py_gradients.html
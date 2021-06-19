# -*- coding: utf-8 -*-
'''
@Time          : 20/04/25 15:49
@Author        : huguanghao
@File          : demo.py
@Noice         :
@Modificattion :
    @Author    : mikecaav
    @Time      : 21/06/18 11:50
    @Detail    : removed detect video and detect skimage
'''

from yolov4.tool.utils import *
from yolov4.tool.torch_utils import *
from yolov4.tool.darknet2pytorch import Darknet
import cv2

"""hyper parameters"""
use_cuda = True

def detect_cv2(model, cfgfile, weightfile, img):

    if use_cuda:
        model.cuda()

    num_classes = model.num_classes
    if num_classes == 20:
        namesfile = './yolov4/data/voc.names'
    elif num_classes == 80:
        namesfile = './yolov4/data/coco.names'
    else:
        namesfile = './yolov4/data/x.names'
    class_names = load_class_names(namesfile)
    sized = cv2.resize(img, (model.width, model.height))
    sized = cv2.cvtColor(sized, cv2.COLOR_BGR2RGB)

    for i in range(2):
        start = time.time()
        boxes = do_detect(model, sized, 0.4, 0.6, use_cuda)
        finish = time.time()

    return plot_boxes_cv2(img, boxes[0], class_names=class_names)    



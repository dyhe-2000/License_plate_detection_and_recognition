import torch
from torch.utils.data import Dataset, DataLoader
from imutils import paths
import numpy as np
import random
import cv2
import os

filename = "train\皖AQ4025.jpg"
# Image = cv2.imread(filename)
Image = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
print(Image.shape)
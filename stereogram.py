import numpy as np
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('img_path', action='store', type=str, help='translate image path')
parser.add_argument('output', action='store', type=str, default='output.jpg', help='output image name')
args = parser.parse_args()

img = Image.open(args.img_path)
resize = np.array(img.resize((int(img.width / 10), int(img.height / 10))))
left_img = resize[:, int(resize.shape[1]/10):]
right_img = resize[:, 0:int(resize.shape[1]-resize.shape[1]/10)]

result = np.hstack((left_img, right_img))
Image.fromarray(result).save(args.output)
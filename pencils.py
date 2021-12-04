import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.transform import resize
from skimage import color
from os import listdir
from scipy.ndimage import label
from skimage.exposure import adjust_sigmoid
from skimage.filters import threshold_otsu, gaussian

path = "images/"

files = [file for file in listdir(path)]
pencils = 0

def rang (raanges):
	ptmp = 0
	for raange in raanges:
		fig_rang = raange.area
		per_fig = raange.perimeter
		per_ar = fig_rang / per_fig
		if 6 < per_ar < 10 and 2500 < fig_rang < 4500:
			ptmp += 1
	print(ptmp)

	return ptmp

for file in files:
	image = plt.imread(path + file)
	rb = color.rgb2gray(image)
	rb = resize(rb, (rb.shape[0]//10, rb.shape[1]//10))
	rb = adjust_sigmoid(rb, cutoff=10, gain=3)
	rb = gaussian(rb, sigma=3)
	bnr = rb.copy()
	bnr[rb >= threshold_otsu(rb)] = 0
	bnr[bnr > 0] = 1
	labeled = label(bnr)[0]
	raanges = regionprops(labeled)
	pencils = pencils + rang(raanges)


print("Кол-во карандашей: " + str(pencils))
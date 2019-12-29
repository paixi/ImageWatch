from imagewatch import ImageWatch
from glob import glob
images = glob("test/*.png")
iw = ImageWatch(images, nrow=8)
iw.start()

#GIF Mario with Python ✨

import imageio.v3 as iio

filenames = ['mario2.jpeg', 'mario1.jpeg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('mario.gif', images, duration = 500, loop = 0)
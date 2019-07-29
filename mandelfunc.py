#!/usr/bin/env python3
#
#
# Asis A Sotelo
#
#mandelfunc.py
#


import numpy as np




## 2D Mandelbrot Function

def mandelbrot(c, thresh = 2, max_iter = 25):

    z = c

    for i in range(max_iter):
        if np.abs(z) > thresh:
            return i
        z = z*z + c

    return 0

## The Mandelbrot Set Graphed to Width x and Height y

def mandelbrot_set(x_min,y_min,x_max,y_max, WIDTH = 580, HEIGHT =270, thresh = 2, max_iter=30):
    x_axis = np.linspace(x_min, x_max, WIDTH)
    y_axis = np.linspace(y_min,y_max, HEIGHT)

    # CREATE A ARRAY OF VALUES THAT RETURN THE ITERATION OF THE ESCAPE OF mandelbrot_set

    image = np.array([mandelbrot_set(complex(x,y), thresh, max_iter) for y in y_axis for x in x_axis])


    return image

## We must define the boundaries of the image

def bound(center, span, zoom):

    boundl = center - (span/(2.0**zoom))
    boundr = center + (span/(2.0**zoom))

    return boundl,boundr

## Plotting a colored image

def plot_colored_image(image, rgb, shape, x_size, y_size, title):

    width, height= shape
    colored_image = np.zeros((width,height,3))
    red, green, blue = rgb

    colored_image[:,:,0] = image* red
    colored_image[:,:,1] = image * green
    colored_image[:,:,2] = image * blue


center1 = -.5, 0.0
print(center1)
delta_x = 1
delta_y = 1
width = 500
height = 500
threshold = 2
b1 = bound(-.5,1,1)
print(b1)
rgb =(.5, .2, .9)
## 3D Mandelbulb Function

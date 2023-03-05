#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 12:05:51 2023

@author: davidalexanderbehrens
"""

import matplotlib.cm
from PIL import Image
from mandelbrot import MandelbrotSet
from viewport import Viewport

def paint(mandelbrot_set, viewport, palette, smooth):
     for pixel in viewport:
         stability = mandelbrot_set.stability(complex(pixel), smooth)
         index = int(min(stability * len(palette), len(palette) - 1))
         pixel.color = palette[index % len(palette)]
         
def denormalize(palette):
     return [
         tuple(int(channel * 255) for channel in color)
         for color in palette
    ]

colormap = matplotlib.cm.get_cmap("twilight").colors
palette = denormalize(colormap)



mandelbrot_set = MandelbrotSet(max_iterations=512, escape_radius=1000)
image = Image.new(mode="RGB", size=(512, 512))
viewport = Viewport(image, center=-0.7435 + 0.1314j, width=0.002)
paint(mandelbrot_set, viewport, palette, smooth=True)
image.show()

from PIL.ImageColor import getrgb

def hsb(hue_degrees: int, saturation: float, brightness: float):
     return getrgb(
         f"hsv({hue_degrees % 360},"
         f"{saturation * 100}%,"
         f"{brightness * 100}%)"
     )

mandelbrot_set = MandelbrotSet(max_iterations=20, escape_radius=1000)
for pixel in Viewport(image, center=-0.75, width=3.5):
     stability = mandelbrot_set.stability(complex(pixel), smooth=True)
     pixel.color = (0, 0, 0) if stability == 1 else hsb(
         hue_degrees=int(stability * 360),
         saturation=stability,
         brightness=1,
     )

image.show()
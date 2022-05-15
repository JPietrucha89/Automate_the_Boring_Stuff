# Pillow is a third-party Python module for interacting with image files. The module has several functions that make it easy to crop, resize, and edit the content of an image. With the power to manipulate images the same way you would with software such as Microsoft Paint or Adobe Photoshop, Python can automatically edit hundreds or thousands of images with ease

# Computer Image  --------------------------------------------------------------------
# In order to manipulate an image, you need to understand the basics of how computers deal with colors and coordinates in images and how you can work with colors and coordinates in Pillow.

# Colors and RGBA Values --------------------------------------------------------------------
# Computer programs often represent a color in an image as an RGBA value. An RGBA value is a group of numbers that specify the amount of red, green, blue, and alpha ( or transparency) in a color. Each of these component values is an integer from 0 (none at all) to 255 (the maximum). These RGBA values are assigned to individual pixels
# a pixel is the smallest dot of a single color the computer screen can show(as you can imagine, there are millions of pixels on a screen). A pixel’s RGB setting tells it precisely what shade of color it should display. Images also have an alpha value to create RGBA values. If an image is displayed on the screen over a background image or desktop wallpaper, the alpha value determines how much of the background you can “see through” the image’s pixel.

# In Pillow, RGBA values are represented by a tuple of four integer values. For example, the color red is represented by(255, 0, 0, 255). This color has the maximum amount of red, no green or blue, and the maximum alpha value, meaning it is fully opaque. Green is represented by(0, 255, 0, 255), and blue is (0, 0, 255, 255). White, the combination of all colors, is (255, 255, 255, 255), while black, which has no color at all, is (0, 0, 0, 255).

# If a color has an alpha value of 0, it is invisible, and it doesn’t really matter what the RGB values are. After all, invisible red looks the same as invisible black.

# Pillow offers the ImageColor.getcolor() function so you don’t have to memorize RGBA values for the colors you want to use. This function takes a color name string as its first argument, and the string 'RGBA' as its second argument, and it returns an RGBA tuple.
from PIL import ImageColor
from PIL import Image
import os
from pathlib import Path

print(ImageColor.getcolor('red', 'RGBA'))  # (255, 0, 0, 255)
print(ImageColor.getcolor('RED', 'RGBA'))  # (255, 0, 0, 255)
print(ImageColor.getcolor('Black', 'RGBA'))  # (0, 0, 0, 255)
print(ImageColor.getcolor('chocolate', 'RGBA'))  # (210, 105, 30, 255)
print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))  # (100, 149, 237, 255)

# Coordinates and Box Tuples --------------------------------------------------------------------
# Image pixels are addressed with x- and y-coordinates, which respectively specify a pixel’s horizontal and vertical locations in an image. The origin is the pixel at the top-left corner of the image and is specified with the notation (0, 0). The first zero represents the x-coordinate, which starts at zero at the origin and increases going from left to right. The second zero represents the y-coordinate, which starts at zero at the origin and increases going down the image. This bears repeating: y-coordinates increase going downward, which is the opposite of how you may remember y-coordinates being used in math class.

# Many of Pillow’s functions and methods take a box tuple argument. This means Pillow is expecting a tuple of four integer coordinates that represent a rectangular region in an image. The four integers are, in order, as follows:

# Left The x-coordinate of the leftmost edge of the box.
# Top The y-coordinate of the top edge of the box.
# Right The x-coordinate of one pixel to the right of the rightmost edge of the box. This integer must be greater than the left integer.
# Bottom The y-coordinate of one pixel lower than the bottom edge of the box. This integer must be greater than the top integer.
catIm = Image.open(Path(os.getcwd(), 'working_with_images', 'zophie.png'))

# Working with the Image Data Type --------------------------------------------------------------------
# An Image object has several useful attributes that give you basic information about the image file it was loaded from: its width and height, the filename, and the graphics format(such as JPEG, GIF, or PNG).
print(catIm.size)  # (816, 1088) tuple of the image’s width and height in pixels
width, height = catIm.size
print(width)  # 816
print(height)  # 1088
print(catIm.filename)  # 'zophie.png'
print(catIm.format)  # 'PNG'
print(catIm.format_description)  # 'Portable network graphics'

# saving image with different extension
catIm.save(Path(os.getcwd(), 'working_with_images', 'zophie.jpg'))

# Pillow also provides the Image.new() function, which returns an Image object—much like Image.open(), except the image represented by Image.new()’s object will be blank.
# Here we create an Image object for an image that’s 100 pixels wide and 200 pixels tall, with a purple background
im = Image.new('RGBA', (100, 200), 'purple')
im.save(Path(os.getcwd(), 'working_with_images', 'purpleImage.png'))
# We call Image.new() again to create another Image object, this time passing(20, 20) for the dimensions and nothing for the background color ➋. Invisible black, (0, 0, 0, 0), is the default color used if no color argument is specified, so the second image has a transparent background
im2 = Image.new('RGBA', (20, 20))
im2.save(Path(os.getcwd(), 'working_with_images', 'transparentImage.png'))

# Cropping images --------------------------------------------------------------------
# The crop() method on Image objects takes a box tuple and returns an Image object representing the cropped image. The cropping does not happen in place—that is, the original Image object is left untouched, and the crop() method returns a new Image object. Remember that a boxed tuple—in this case, the cropped section—includes the left column and top row of pixels but only goes up to and does not include the right column and bottom row of pixels.
catIm = Image.open(Path(os.getcwd(), 'working_with_images', 'zophie.png'))
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save(Path(os.getcwd(), 'working_with_images', 'cropped.png'))

# Copying and pasting images --------------------------------------------------------------------
# The copy() method will return a new Image object with the same image as the Image object it was called on. This is useful if you need to make changes to an image but also want to keep an untouched version of the original.
catCopyIm = catIm.copy()
# The catIm and catCopyIm variables contain two separate Image objects, which both have the same image on them. Now that you have an Image object stored in catCopyIm, you can modify catCopyIm as you like and save it to a new filename, leaving zophie.png untouched.
# The paste() method is called on an Image object and pastes another image on top of it.
faceIm = catIm.crop((335, 345, 565, 560))
faceIm.size  # (230, 215)
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save(Path(os.getcwd(), 'working_with_images', 'pasted.png'))
# First we pass crop() a box tuple for the rectangular area in zophie.png that contains Zophie’s face. This creates an Image object representing a 230×215 crop, which we store in faceIm. Now we can paste faceIm onto catCopyIm. The paste() method takes two arguments: a “source” Image object and a tuple of the x- and y-coordinates where you want to paste the top-left corner of the source Image object onto the main Image object. Here we call paste() twice on catCopyIm, passing (0, 0) the first time and (400, 500) the second time. This pastes faceIm onto catCopyIm twice: once with the top-left corner of faceIm at (0, 0) on catCopyIm, and once with the top-left corner of faceIm at (400, 500).

# Resizing and image --------------------------------------------------------------------
# The resize() method is called on an Image object and returns a new Image object of the specified width and height. It accepts a two-integer tuple argument, representing the new width and height of the returned image.
width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save(
    Path(os.getcwd(), 'working_with_images', 'quartersized.png'))
svelteIm = catIm.resize((width, height + 300))
svelteIm.save(Path(os.getcwd(), 'working_with_images', 'svelte.png'))
# Note that the resize() method does not edit the Image object in place but instead returns a new Image object.

# Rotating and flipping and image --------------------------------------------------------------------
# Images can be rotated with the rotate() method, which returns a new Image object of the rotated image and leaves the original Image object unchanged. The argument to rotate() is a single integer or float representing the number of degrees to rotate the image counterclockwise.
catIm.rotate(90).save(
    Path(os.getcwd(), 'working_with_images', 'rotated90.png'))
catIm.rotate(180).save(
    Path(os.getcwd(), 'working_with_images', 'rotated180.png'))
catIm.rotate(270).save(
    Path(os.getcwd(), 'working_with_images', 'rotated270.png'))

# FLIPPING
catIm.transpose(Image.FLIP_LEFT_RIGHT).save(
    Path(os.getcwd(), 'working_with_images', 'horizontal_flip.png'))
catIm.transpose(Image.FLIP_TOP_BOTTOM).save(
    Path(os.getcwd(), 'working_with_images', 'vertical_flip.png'))

# Changing invidual pixels --------------------------------------------------------------------
# The color of an individual pixel can be retrieved or set with the getpixel() and putpixel() methods. These methods both take a tuple representing the x- and y-coordinates of the pixel. The putpixel() method also takes an additional tuple argument for the color of the pixel. This color argument is a four-integer RGBA tuple or a three-integer RGB tuple.
# make a new image that is a 100×100 transparent square.
im = Image.new('RGBA', (100, 100))
im.getpixel((0, 0))  # (0, 0, 0, 0)
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
im.getpixel((0, 0))  # (210, 210, 210, 255)
im.getpixel((0, 50))  # (169, 169, 169, 255)
im.save('putPixel.png')

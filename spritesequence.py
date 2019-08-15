from PIL import Image
import math
import os

###utility functions###

def get_factors(x):
    #returns a list of x's factors
    
    array = []

    for i in range(1, x + 1):
        if x % i == 0:
            array.append(str(i))
        
    return array

######

def check_square (offsetX, offsetY, size):
# Checks each pixel in a column and then moves to the
# next row until the entire square has been checked.
#
# Returns true if at least 1 pixel within the square is opaque.

    isFull = False
    x1 = offsetX
    y1 = offsetY

    x2 = offsetX + size
    y2 = offsetY + size

    pixelsX = x1
    pixelsY = y1

    while pixelsX < x2:
        pixel = img.load()[pixelsX,pixelsY]
        pixelsY += 1
        
        if pixelsY > y2:
            pixelsY = y1
            pixelsX += 1
        if pixelsY >= img.size[1]:
            pixelsY = y1
            pixelsX += 1
            
        if pixel[3] > 0:
            isFull = True
            return isFull
            break
    if pixel[3] <= 0:
        isFull = False
        return isFull



def find_filled_squares(totalFrames,frameSize,cols):
# Runs the check_square function for each frame in the image.
# Each square that returns true has its coordinates added to the list "array".
# These are the filled squares. The empty squares returned false, and are ignored.
#
# Returns the list of the coordinates.

    array = []
    rectX = 0
    rectY = 0
    filledSquares = 0
    i = 0
    
    while i < totalFrames:
        
        if check_square(rectX * frameSize, rectY * frameSize,frameSize) == True:
            filledSquares += 1
            array.append([rectX * frameSize, rectY * frameSize])

        i += 1
        rectX += 1
        if rectX >= cols:
            rectY += 1
            rectX = 0
            
    return array

def paste_squares(array,frameSize):
# Creates a new image and populates it with the frames found in find_filled_squares.
# "crop" cuts a region out of the input image.
# "paste" pastes said region onto on the new image.
# The crop and paste sizes need to be the same.
# This process repeats for each frame from find_filled_squares.
#
# Returns the output image.

    output = Image.new("RGBA", (len(array) * frameSize, frameSize), (0,0,0,0))

    rectX = 0
    rectY = 0

    coord = 0,0
    i = 0

    for x in range(0,len(array)):
        coord = array[x]
        rectX = coord[0]
        rectY = coord[1]
        cropRect = (rectX,rectY,rectX + frameSize,rectY + frameSize)
        finalRect = (i,0,i + frameSize,frameSize)
        i += frameSize
        
        region = img.crop(cropRect)
        output.paste(region,finalRect)
    return output

def main_program():
    # Prints the image dimensions.
    print
    print("Image dimensions: " + str(img.size[0]) + "x" + str(img.size[1]))
    print

    # Gets a list of the image's factors, so the user can select one.
    # The frame size needs to be a factor of the image's width, because
    # otherwise there would be fractions of frames and such.
    img_factors = (get_factors(img.size[0]))

    # If the width is prime, a message will appear.
    # An image with a prime length can only be evenly divided
    # two ways, but the option is still available.
    if len(img_factors) <= 2:
            print("WARNING: the width of the image is a prime number.")
            print
            
    print(img_factors)
    frameSize = (raw_input("Choose one of the above for the frame-size: "))

    while frameSize not in img_factors:
        frameSize = (raw_input("Please choose a number from the list: "))

    frameSize = int(frameSize)

    cols = img.size[0] / frameSize
    rows = img.size[1] / frameSize
    totalFrames = cols * rows

    print
    print("This image has " + str(cols) + " columns and " + str(rows) + " rows.")
    print("There are " + str(totalFrames) + " frames in total.")
    print

    filledSquares = find_filled_squares(totalFrames,frameSize,cols)
    print("Creating image sequence...")
    output = paste_squares(filledSquares,frameSize)
    output.save('output.png')
    
    print("Success! The output (" + str(len(filledSquares)*frameSize) + "x" + str(frameSize) + ") has been saved to" + os.getcwd())

image_name = (raw_input("Enter the directory of the image: "))
img = Image.open(image_name)
main_program()


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


#print(im.format, im.size, im.mode)
#im.show()
def imRes(photo):
    im = Image.open(photo)
    imWidth, imHeight = im.size
    return im.resize((imWidth//2, imHeight//2))

im1 = imRes('rf.jpg')
#im1.show()

im2 = imRes('Снимок.JPG')

im1.paste(im2, (50,20))
#im1.show('ggwp')
#font = ImageFont.truetype("sans-serif.ttf", 16)

imdraw = ImageDraw.Draw(im1)
imdraw.text((10, 10), "Samle text", (123, 231, 23))

im1.save('test.png')
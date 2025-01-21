from PIL import Image

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
im1.show('ggwp')





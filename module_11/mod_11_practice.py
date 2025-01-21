from PIL import Image
im = Image.open('rf.jpg')
print(im.format, im.size, im.mode)
#im.show()

out = im.resize((256, 256))
out.show()



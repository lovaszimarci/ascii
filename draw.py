from PIL import Image, ImageShow
img = Image.open(r"/home/lovaszimarci/ascii/venus_face.jpg")
img = img.convert("L")

# width 220
# height 168
# ascii alpha scale return value 0-255


print(img.getpixel((219,167)), img.size, img.mode)


def write_to_file(character):
    pass



def evaluate(value_of_pixel):
    pass



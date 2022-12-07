from PIL import Image, ImageShow
img = Image.open(r"/home/lovaszimarci/ascii/venus_face.jpg")
img = img.convert("L")

# width 220
# height 168
# ascii alpha scale return value 0-255


print(img.getpixel((219,167)), img.size, img.mode)


def break_line():
    with open("venus_face.txt", "a") as f:
        f.write("\n")


def write_to_file(character):
    
    with open("venus_face.txt","a") as f:
        f.write(character)
        f.close()



def evaluate(value_of_pixel):
    if value_of_pixel <= 25.5:
        write_to_file(" ")
    elif value_of_pixel > 25.5 and value_of_pixel <= 51:
        write_to_file(".")
    elif value_of_pixel > 51 and value_of_pixel <= 76.5:
        write_to_file(":")
    elif value_of_pixel > 76.5 and value_of_pixel <= 102:
        write_to_file("-")
    elif value_of_pixel > 102 and value_of_pixel <= 127.5:
        write_to_file("=")
    elif value_of_pixel > 127.5 and value_of_pixel <= 153:
        write_to_file("+")
    elif value_of_pixel > 153 and value_of_pixel <= 178.5:
        write_to_file("*")
    elif value_of_pixel > 178.5 and value_of_pixel <= 204:
        write_to_file("#")
    elif value_of_pixel > 204 and value_of_pixel <= 229.5:
        write_to_file("%")
    elif value_of_pixel > 229.5 and value_of_pixel <= 255:
        write_to_file("@")


def go_to_first_line():
    pass


def loop():
    
    for vertical in range(167):
        break_line()
        for horizontal in range(219):
            evaluate(img.getpixel((horizontal, vertical)))
            write_to_file(" ")



def main():
    

    loop()

main()

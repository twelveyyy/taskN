# cSpell:disable 
# load from PIL
from PIL import Image 
def fromImg():
    #########################

    img_img = "test1.png"
    img_txt = "test1.txt"

    #########################
    # open the img with the Image module
    with Image.open(img_img) as im:
        with open(img_txt, "w") as fo:
            # size outputs tuple
            width, height = im.size
            # writeln the offset + dimensions (offset is hardcoded in this case)
            fo.write(str(f"0 0 {width} {height}\n"))
            # go thr all the pixels
            for y in range(height):
                for x in range(width):
                    # print their values
                    fo.write(str(im.getpixel((x, y))))
                    fo.write(str("\n"))
def toImg():
    import ast
    ##########################

    img_img = "test2.png"
    img_txt = "test1.txt"
    
    ##########################
    
    with open(img_txt, "r") as fi:
        with Image.open(img_img) as im:
            # read the starting cords and dimenisons from 1st line
            ox, oy, width, height = map(int, fi.readline().split())
            for y in range(height):
                for x in range(width):
                    # current index + offset
                    im.putpixel((x+ox, y+oy), ast.literal_eval(fi.readline()))
        # save changes before closing
        im.save(img_img)
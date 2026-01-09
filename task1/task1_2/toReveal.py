########################

limiter = "meow"
image = "IMG_6583.png"

########################

from PIL import Image 
# convert bin to ascii
def bin2ascii(text):
    ascii_text = ""
    # split bits into bytes
    for i in range(0, len(text), 8):
        byte = text[i:i+8]
        ascii_text += chr(int(byte, 2))
    return ascii_text
# start to reveal the message in the image
def reveal_message(txt,img_path):
    # this ensures the img is RGB, for the code below expects 3 channels
    img = Image.open(img_path).convert("RGB")

    width, height = img.size
    lsb = ''
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            # append the last bit
            lsb = lsb+str(r & 1) 
            lsb = lsb+str(g & 1) 
            lsb = lsb+str(b & 1)
    # convert the whole lsb stream to ascii then use split() to extract the message
    # if unable to find one appropriate, it will return indexerror
    print(bin2ascii(lsb).split(limiter)[1])
# __main__
reveal_message(limiter, image)

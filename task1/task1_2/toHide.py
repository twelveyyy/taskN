########################

message = "https://hackmd.io/vQgUo2edR0WyZZ3d2-NSOQ"
limiter = "meow"
image = "IMG_6583.png"

########################

from PIL import Image 
# converting ASCII to binary
def ascii2bin(text,textLimit):
    return ''.join(format(ord(char), '08b') for char in textLimit+text+textLimit)
# start to conceal the message in the image
def hide_message(txt,img_path):
    # convert.
    message_n = ascii2bin(txt, limiter)
    # this ensures the img is RGB, for the code below expects 3 channels
    img = Image.open(img_path).convert("RGB")
    # quick check whether its possible to fit the message in
    width, height = img.size
    if ((width * height) * 3) < len(message_n):
        return print("No bueno,\ntry again with a larger image or smaller message")
    print("in progress..")
    # split color channels
    img_r = (img.get_flattened_data(band=0))
    img_g = (img.get_flattened_data(band=1))
    img_b = (img.get_flattened_data(band=2))
    
    t = 0
    new_r=[]
    new_g=[]
    new_b=[]
    # iterate thr every pixels in the img
    for i in range(width*height):
        # check whether the message has ended. 
        # if ended then clone the value, otherwise cut off the last bit and replace it with the corresponding bit in message
        # this ensures all channels in the indexing pixels are filled, this is needed for later
        if (t < len(message_n)):
            new_r.append((img_r[i] & ~1)|int(message_n[t]))
            t = t+1
        else:
            new_r.append(img_r[i])
        if (t < len(message_n)):
            new_g.append((img_g[i] & ~1)|int(message_n[t]))
            t = t+1
        else:
            new_g.append(img_g[i])
        if (t < len(message_n)):
            new_b.append((img_b[i] & ~1)|int(message_n[t]))
            t = t+1
        else:
            new_b.append(img_b[i])
        # all bits in message are concealed, quit the loop
        if (t >= len(message_n)):
            break
    # combine the channels into rgb tuples for pixels
    # this will always embed the message to the start, it is possible to add offset using for loop
    # but for convenience i will use putdata 
    img.putdata(list(zip(new_r, new_g, new_b)))
    # update the img
    img.save(image)
    print(f"File: {image} updated.")

# __main__
hide_message(message, image)

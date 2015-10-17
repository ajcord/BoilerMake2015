from PIL import Image

def combineImages():
    initialImage = Image.open("image.jpg")
    stickerImage = Image.open("images/creepy.png")
    stickerSize = stickerImage.size()

    a = initialImage.load() #loads pixel data
    b = stickerImage.load()

    for w in stickerSize[0] :#width
        for h in stickerSize[1] : #height
            a[w, h] = (a[w,h] * 0.5() + (b[w,h] * 0.5)


    initialImage.save("blended.jpg", "JPEG")

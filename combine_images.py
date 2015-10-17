from PIL import Image

def combineImages():
    initialImage = Image.open("image.jpg")
    stickerImage = Image.open("images/creepy.png")
    #stickerSize = stickerImage.size()

    initialImage.paste(stickerImage, (0,0), stickerImage)

    initialImage.save("blended.jpg", quality=95)

    #a = initialImage.load() #loads pixel data
    #b = stickerImage.load()

    #result = initialImage.copy()
    #array = []

    #for w in stickerSize[0] :#width
    #    for h in stickerSize[1] : #height
    #        array[w, h] = (a[w,h] * 0.5() + (b[w,h] * 0.5)

    #result.putdata(array)
    #result.save("blended", "JPEG")

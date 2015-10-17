from PIL import Image

def combineImages():
    initialImage = Image.open("image.jpg")
    stickerImage = Image.open("images/creepy.png")
    stickerSize = stickerImage.size()

    a = initialImage.load() #loads pixel data
    b = stickerImage.load()

    for (int w = 0; w < stickerSize[0]; w++) :#width
        for (int h = 0; h < stickerSize[1]; h++) : #height
            a[w, h] = (a[w,h] * 0.5() + (b[w,h] * 0.5)


    initialImage.save('Blended.png')

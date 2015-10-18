from PIL import Image
import random

def addSticker():
    initialImage = Image.open("image.jpg")
    if (random.randint(0, 2) == 1):
        imageArray = ["creepy", "ghost", "skeleton"]
        imageString = random.randint(0, len(imageArray) - 1)
        stickerImage = Image.open("images/"+imageString+".png")

        initialImage.paste(stickerImage, (random.randint(0, 520),random.randInt(0, 280)), stickerImage)
    else :
        #don't add sticker

    initialImage.save("blended.jpg", quality=95)

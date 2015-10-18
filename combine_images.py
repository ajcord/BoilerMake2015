from PIL import Image
import random

def addSticker():
    initialImage = Image.open("image.jpg")
    if (random.randint(0, 2) == 0):
        imageArray = ["creepy", "ghost", "skeleton"]
        index = random.randint(0, len(imageArray))
        stickerImage = Image.open("images/"+imageArray[index]+".png")

        initialImage.paste(stickerImage, (random.randint(0, 520),random.randInt(0, 280)), stickerImage)
    else :
        print("No sticker added")

    initialImage.save("blended.jpg", quality=95)

from PIL import Image
import random

def addSticker():
    initialImage = Image.open("image.jpg")
    if (random.randint(0, 8) >=2):
        imageArray = ["creepy", "ghost", "skeleton", "web", "Jack-o-Lantern","trump"]
        index = random.randint(0, len(imageArray) - 1)
        print(index)
        stickerImage = Image.open("images/"+imageArray[index]+".png")

        initialImage.paste(stickerImage, (random.randint(0, 520),random.randint(0, 280)), stickerImage)
    else :
        print("No sticker added")

    initialImage.save("blended.jpg", quality=95)

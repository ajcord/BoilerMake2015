from PIL import Image

def addSticker():
    initialImage = Image.open("image.jpg")
    stickerImage = Image.open("images/creepy.png")

    initialImage.paste(stickerImage, (0,0), stickerImage)

    initialImage.save("blended.jpg", quality=95)

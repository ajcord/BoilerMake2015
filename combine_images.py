import Image

def combineImages(){
    initialImage = Image.open("image.jpg")
    #inImageSize = initialImage.size()
    stickerImage = Image.open("images/creepy.png")

    #for (int i = 0; i < inImageSize[0]; i++){
    #
    #}

    result = Image.blend(initialImage, stickerImage, 0.5)

    result.save('Blended.png')

}


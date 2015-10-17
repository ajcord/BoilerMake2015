import Image

def mergeImages(filemain, filesticker):
	main_image = Image.open(filemain)
	sticker = Image.open(filesticker)
	
	xm, ym = main_image.size
	filesticker.resize(xm,ym)

	return Image.blend(main_image, sticker, 0.2)
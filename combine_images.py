import sys
import struct
import imghdr

def get_image_size(fhandle):
	try:
		fhandle.seek(0) # Read 0xff next
		size = 2
		ftype = 0
		while not 0xc0 <= ftype <= 0xcf:
			fhandle.seek(size, 1)
			byte = fhandle.read(1)
			print byte
		while ord(byte) == 0xff:
		    byte = fhandle.read(1)
		ftype = ord(byte)
		size = struct.unpack('>H', fhandle.read(2))[0] - 2
		# We are at a SOFn block
		fhandle.seek(1, 1)  # Skip `precision' byte.
		height, width = struct.unpack('>HH', fhandle.read(4))
	except Exception: #IGNORE:W0703
		return

main_imageURI = sys.argv[1]
background_imageURI = sys.argv[2]

main_image_file = open(main_imageURI, "rb")
background_image_file = open(background_imageURI, "rb")

print get_image_size(main_image_file)
print get_image_size(background_image_file)

print main_imageURI + background_imageURI

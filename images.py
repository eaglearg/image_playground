from PIL import Image, ImageFilter
'''
img = Image.open('./Pokedex/pikachu.jpg')
filtered_image = img.convert('L')
filtered_image.save("grey.png", 'png')

crooked = filtered_image.rotate(90)
crooked.save('crooked.png', 'png')

resize = filtered_image.resize((300, 300))
resize.save('resize.png', 'png')

resizeWithoutLoosingAspectRatio = filtered_image
resizeWithoutLoosingAspectRatio.thumbnail((250,200))
resizeWithoutLoosingAspectRatio.save('thumbnail.png')

box = (100,100,400,400)
region = filtered_image.crop(box)
region.save('crop.png', 'png')

#filtered_image.show()
'''


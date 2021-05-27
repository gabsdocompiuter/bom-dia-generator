import sys
import random
sys.path[0] += '\\..'

from helpers.image_helper import ImageHelper

image_helper = ImageHelper()

assets_dir = "D:/github/bom-dia-generator/bom-dia-generator/assets/"

img = random.randint(0, 10)
print(img)

image_asset = f"{assets_dir}/images/backgrounds/{img}.jpg"
font_asset = f"{assets_dir}/fonts/0.ttf"

blur_image = image_helper.blur_image(image_asset, 5)
resize_image = image_helper.resize_image(blur_image, 1024, 1024)
final_image = image_helper.add_text(resize_image, font_asset, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tristique ligula vitae molestie suscipit.')
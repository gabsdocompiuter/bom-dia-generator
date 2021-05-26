import sys
sys.path[0] += '\\..'

from helpers.image_helper import ImageHelper

image_helper = ImageHelper()

assets_dir = "D:/github/bom-dia-generator/bom-dia-generator/assets/"
image_asset = f"{assets_dir}/images/backgrounds/2.jpg"
font_asset = f"{assets_dir}/fonts/0.ttf"

blur_image = image_helper.blur_image(image_asset, 5)
final_image = image_helper.add_text(blur_image, font_asset, 'BOM DIA, KKKKKKK')
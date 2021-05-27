from PIL import Image, ImageFilter, ImageDraw, ImageFont
import textwrap

class ImageHelper:
    def __init__(self):
        pass

    def blur_image(self, image, blur_perc):
        original_image = Image.open(image)

        blur_image = original_image.filter(ImageFilter.BoxBlur(blur_perc))
        return blur_image

    def resize_image(self, image, width, height):
        image_width, image_height = image.size

        left = (image_width - width) / 2
        right = (image_width + width) / 2
        top = (image_height - height) / 2
        bottom = (image_height + height) / 2

        if left < 0:
            left = 0
        
        if top < 0:
            top = 0

        if right > (image_width - left):
            right = image_width - left

        if bottom > (image_height - top):
            bottom = image_height - top

        print((left, top, right, bottom))

        return image.crop((left, top, right, bottom))

    def add_text(self, image, font_asset, message):
        image_draw = ImageDraw.Draw(image)
        image_font = ImageFont.truetype(font_asset, 80)

        width, height = image.size

        #decide a cor do texto
        rgb_image = image.convert('RGB')
        r, g, b = rgb_image.getpixel((width / 2, height / 2))
        text_color = (255 - r, 255 - g, 255 - b)

        lines = textwrap.wrap(message, width=30)
        position_y = height / 3

        for line in lines:
            text_width, text_height = image_draw.textsize(line, font=image_font)

            position_x = (width  - text_width)  / 2
            
            image_draw.text((position_x, position_y), line, font=image_font, fill=text_color)
            position_y += text_height

        image.show()

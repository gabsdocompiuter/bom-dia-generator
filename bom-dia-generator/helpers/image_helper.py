from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageHelper:
    def __init__(self):
        pass

    def blur_image(self, image, blur_perc):
        original_image = Image.open(image)

        blur_image = original_image.filter(ImageFilter.BoxBlur(blur_perc))
        return blur_image

    def cut_image(self, width, height):
        pass

    def add_text(self, image, font_asset, message):
        image_draw = ImageDraw.Draw(image)
        image_font = ImageFont.truetype(font_asset, 80)

        width, height = image.size
        text_width, text_height = image_draw.textsize(message, font=image_font)

        rgb_image = image.convert('RGB')
        r, g, b = rgb_image.getpixel((width / 2, height / 2))
        print(f'{r}, {g}, {b}')
        text_color = (255 - r, 255 - g, 255 - b)

        position_x = (width  - text_width)  / 2
        position_y = (height - text_height) / 2

        image_draw.text((position_x, position_y), message, font=image_font, fill=text_color)
        image.show()

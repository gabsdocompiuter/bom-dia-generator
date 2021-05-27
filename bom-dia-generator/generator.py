from helpers.image_helper import ImageHelper

import os
import random

class Generator:
    def __init__(self):
        self.image_helper = ImageHelper()
        self.assets_dir = f'{os.getcwd()}/assets'

    def __get_items_count(self, folder):
        count = len([name for name in os.listdir(folder) if os.path.isfile(os.path.join(folder, name))])

        return count - 1

    def get_font_asset(self):
        folder = f'{self.assets_dir}/fonts'
        fonts_count = self.__get_items_count(folder)
        rnd = random.randint(0, fonts_count)

        return f'{folder}/{rnd}.ttf'

    def get_background_asset(self):
        folder = f'{self.assets_dir}/images/backgrounds'
        backgrounds_count = self.__get_items_count(folder)
        rnd = random.randint(0, backgrounds_count)

        return f'{folder}/{rnd}.jpg'

    def get_message(self):
        return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tristique ligula vitae molestie suscipit'

    def generate_image(self):
        font_asset = self.get_font_asset()
        background_asset = self.get_background_asset()
        message = self.get_message()

        blur_image = self.image_helper.blur_image(background_asset, 5)
        resized_image = self.image_helper.resize_image(blur_image, 1024, 1024)
        final_image = self.image_helper.add_text(resized_image, font_asset, message)

        final_image.show()

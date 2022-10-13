from doctest import Example
import pyautogui
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO)

class LocateOnScreen(object):

    def locate(self, image, confidence=0.8, trasnform_ratio=0.1):
        # Imagenes base
        positive_img = Image.open(image)
        negative_img = Image.open(image)

        # Tamanios base
        positve_width, positive_height = positive_img.size
        negative_width, negative_height = negative_img.size
        
        logging.info(f'LocateOnScreen::locate() | Original size: {positive_img.size}')

        # Lmites
        MAX_SIZE = 1000
        MIN_SIZE = 0

        exchanger = False
        current_candidate = positive_img

        # Intevalo de control
        while (positive_height < MAX_SIZE and negative_height > MIN_SIZE) or \
                (positve_width < MAX_SIZE and negative_width > MIN_SIZE):
            try:
                jobSettingsLocation = pyautogui.locateOnScreen(
                    current_candidate, confidence=confidence)
                if jobSettingsLocation:
                    logging.info(f'LocateOnScreen::locate() | [OK] Found - size: {current_candidate.size}')
                    return jobSettingsLocation
            except Exception as e:
                logging.info(f'LocateOnScreen::locate() | Error - {e}')

            logging.info(f'LocateOnScreen::locate() | [NOK] Not Found - size: {current_candidate.size}')

            if exchanger:
                positive_img = positive_img.resize(
                    (positve_width, positive_height), Image.ANTIALIAS
                )
                positive_height += int(positive_height * trasnform_ratio)
                positve_width += int(positve_width * trasnform_ratio)
                current_candidate = positive_img
            else:
                negative_img = negative_img.resize(
                    (negative_width, negative_height), Image.ANTIALIAS
                )
                negative_width -= int(negative_width * trasnform_ratio)
                negative_height -= int(negative_width * trasnform_ratio)
                current_candidate = negative_img

            exchanger = not exchanger

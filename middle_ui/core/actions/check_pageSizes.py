import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))))

class CheckPageSizes(AbsractAction):

    def execute(self) -> str:
        pageSizes = []
        try:
            self.search_img("middle_ui//core//resources//settingsSizesANSI.png")
            pageSizes.append("ansi")
        except Exception as e:
            pass

        try:
            self.search_img("middle_ui//core//resources//settingsSizesAmerican.png")
            pageSizes.append("american")
        except Exception as e:
            pass
        
        try:
            self.search_img("middle_ui//core//resources//settingsSizesArchitectural.png")
            pageSizes.append("architectural")
        except Exception as e:
            pass

        try:
            self.search_img("middle_ui//core//resources//settingsSizesDINA.png")
            pageSizes.append("iso-jis")
        except Exception as e:
            pass

        try:
            self.search_img("middle_ui//core//resources//settingsSizesISO.png")
            pageSizes.append("iso")
        except Exception as e:
            pass
        
        try:
            self.search_img("middle_ui//core//resources//settingsSizesJIS.png")
            pageSizes.append("jis")
        except Exception as e:
            pass

        try:
            self.search_img("middle_ui//core//resources//settingsSizesPhoto.png")
            pageSizes.append("photo")
        except Exception as e:
            pass
        
        try:
            self.search_img("middle_ui//core//resources//settingsSizesSuper.png")
            pageSizes.append("super")
        except Exception as e:
            pass
        
        print(pageSizes)

    def search_img(self, path):
        printJobUri = os.path.join(project_dir, path)
        locator = LocateOnScreen()
        nestingButtonLocation = locator.locate(printJobUri)
        nestingButton = pyautogui.center(nestingButtonLocation)
        pyautogui.moveTo(nestingButton.x, nestingButton.y)


       





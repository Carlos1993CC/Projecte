from xmlrpc.client import boolean
import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class CheckTIFFCuttingLinesVisible(AbsractAction):

    def execute(self) -> str:
        try:
            imageMargins = os.path.join(project_dir, "middle_ui//core//resources//TIFFcuttingLines.png")
            locator = LocateOnScreen()
            imageMarginsLocation = locator.locate(imageMargins)
            imageMarginsPoint = pyautogui.center(imageMarginsLocation)
            pyautogui.moveTo(imageMarginsPoint.x, imageMarginsPoint.y)
            print("True")
        except:
            print("False")
            raise Exception("Error al buscar el elemento")
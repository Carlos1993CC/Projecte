from xmlrpc.client import boolean
import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class CheckUnlockedIcon(AbsractAction):

    def execute(self) -> str:
        try:
            unlockedIcon = os.path.join(project_dir, "middle_ui//core//resources//unlocked_icon.png")
            locator = LocateOnScreen()
            unlockedIconLocation = locator.locate(unlockedIcon)
            unlockedIconPoint = pyautogui.center(unlockedIconLocation)
            pyautogui.moveTo(unlockedIconPoint.x, unlockedIconPoint.y)
            print("True")
        except:
            print("False")
            raise Exception("Error al buscar el elemento")
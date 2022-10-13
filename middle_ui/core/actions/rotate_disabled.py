from xmlrpc.client import boolean
import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class RotateDisabled(AbsractAction):

    def execute(self) -> str:
        try:
            printJobUri = os.path.join(project_dir, "middle_ui//core//resources//rotate_button_disabled.png")
            locator = LocateOnScreen()
            makeCopiesLocation = locator.locate(printJobUri)
            jobSettingsPoint = pyautogui.center(makeCopiesLocation)
            pyautogui.moveTo(jobSettingsPoint.x, jobSettingsPoint.y)
            print("True")
        except:
            print("False")
            raise Exception("Error al buscar el elemento")





from xmlrpc.client import boolean
import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class IsSelected(AbsractAction):

    def execute(self) -> str:
        try:
            printJobUri = os.path.join(project_dir, "middle_ui//core//resources//layout_clip_content_selected.png")
            locator = LocateOnScreen()
            jobSettingsLocation = locator.locate(printJobUri)
            jobSettingsPoint = pyautogui.center(jobSettingsLocation)
            pyautogui.moveTo(jobSettingsPoint.x, jobSettingsPoint.y)
            print("True")
        except:
            print("False")
            raise Exception("Error al buscar el elemento")





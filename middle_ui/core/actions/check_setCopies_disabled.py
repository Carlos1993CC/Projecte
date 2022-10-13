from xmlrpc.client import boolean
import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class CheckSetCopiesDisabled(AbsractAction):

    def execute(self) -> str:
        try:
            setCopiesDisabled = os.path.join(project_dir, "middle_ui//core//resources//set_copies_disabled_button.png")
            locator = LocateOnScreen()
            setCopiesDisabledLocation = locator.locate(setCopiesDisabled)
            setCopiesDisabledPoint = pyautogui.center(setCopiesDisabledLocation)
            pyautogui.moveTo(setCopiesDisabledPoint.x, setCopiesDisabledPoint.y)
            print("True")
        except:
            print("False")
            raise Exception("Error al buscar el elemento")
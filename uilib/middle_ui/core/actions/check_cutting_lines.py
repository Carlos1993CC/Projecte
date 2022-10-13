from xmlrpc.client import boolean
import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class CheckCuttingLines(AbsractAction):

    def execute(self) -> str:
        try:
            cuttingLines = os.path.join(project_dir, "middle_ui//core//resources//cutting_lines.png")
            locator = LocateOnScreen()
            cuttingLinesLocation = locator.locate(cuttingLines)
            cuttingLinesPoint = pyautogui.center(cuttingLinesLocation)
            pyautogui.moveTo(cuttingLinesPoint.x, cuttingLinesPoint.y)
            print("True")
        except:
            print("False")
            raise Exception("Error al buscar el elemento")
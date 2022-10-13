import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class OpenMakeCopies(AbsractAction):

    def execute(self) -> str:
        printJobUri = os.path.join(project_dir, "middle_ui//core//resources//make_copies_button.png")
        locator = LocateOnScreen()
        makeCopiesLocation = locator.locate(printJobUri)
        makeCopiesPoint = pyautogui.center(makeCopiesLocation)
        pyautogui.click(makeCopiesPoint.x, makeCopiesPoint.y)





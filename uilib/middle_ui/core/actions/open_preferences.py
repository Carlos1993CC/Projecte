import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class OpenPreferences(AbsractAction):

    def execute(self) -> str:
        printJobUri = os.path.join(project_dir, "middle_ui//core//resources//preferences_sidebar_button.png")
        locator = LocateOnScreen()
        makeCopiesLocation = locator.locate(printJobUri)
        jobSettingsPoint = pyautogui.center(makeCopiesLocation)
        print(jobSettingsPoint)
        pyautogui.click(jobSettingsPoint.x, jobSettingsPoint.y)

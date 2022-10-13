import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class AddFileButton(AbsractAction):

    def execute(self) -> str:
        printJobUri = os.path.join(project_dir, "middle_ui//core//resources//add_file_button.png")
        locator = LocateOnScreen()
        jobSettingsLocation = locator.locate(printJobUri)
        jobSettingsPoint = pyautogui.center(jobSettingsLocation)
        pyautogui.click(jobSettingsPoint.x, jobSettingsPoint.y)
        #pyautogui.click(jobSettingsPoint.x, jobSettingsPoint.y)




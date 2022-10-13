import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class OpenJobSettings(AbsractAction):

    def execute(self) -> str:
        printJobUri = os.path.join(project_dir, "middle_ui//core//resources//job_settings_sidebar_button.png")
        locator = LocateOnScreen()
        jobSettingsLocation = locator.locate(printJobUri)
        jobSettingsPoint = pyautogui.center(jobSettingsLocation)
        print(jobSettingsPoint)
        pyautogui.click(jobSettingsPoint.x, jobSettingsPoint.y)





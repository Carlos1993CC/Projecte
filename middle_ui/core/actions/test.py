import pyautogui
import pyscreeze
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from PIL import Image

from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))))


class Test(AbsractAction):


    def execute(self) -> str:

        printJobUri = os.path.join(
            project_dir, "middle_ui//core//resources//test.png")

        locator = LocateOnScreen()
        jobSettingsLocation = locator.locate(printJobUri)
        
        jobSettingsPoint = pyautogui.center(jobSettingsLocation)
        print(jobSettingsLocation)
        pyautogui.doubleClick(jobSettingsPoint.x, jobSettingsPoint.y)




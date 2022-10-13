import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.lib.LocateOnScreen import LocateOnScreen

project_dir = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))))

class GetNestingState(AbsractAction):

    def execute(self) -> str:
        try:
            self.attempt_img("middle_ui//core//resources//nesting_button_disabled.png")
            print("DISABLED")
            return
        except Exception as e:
            pass

        try:
            self.attempt_img("middle_ui//core//resources//nesting_button_no_selected.png")
            print("NO_SELECTED")
            return
        except Exception as e:
            pass
        
        try:
            self.attempt_img("middle_ui//core//resources//nesting_button_selected.png")
            print("SELECTED")
            return
        except Exception as e:
            pass



    def attempt_img(self, path):
        printJobUri = os.path.join(project_dir, path)
        locator = LocateOnScreen()
        nestingButtonLocation = locator.locate(printJobUri)
        nestingButton = pyautogui.center(nestingButtonLocation)
        pyautogui.moveTo(nestingButton.x, nestingButton.y)


       





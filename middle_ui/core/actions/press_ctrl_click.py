import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction

class PressCtrlClick(AbsractAction):

    def execute(self) -> str:
        with pyautogui.hold('ctrl'):
            pyautogui.click()
import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction

class PressCtrlA(AbsractAction):

    def execute(self) -> str:
        pyautogui.hotkey('ctrl', 'a')
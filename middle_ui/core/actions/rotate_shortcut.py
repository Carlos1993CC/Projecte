import pyautogui
import os
from middle_ui.core.abstract.AbstractAction import AbsractAction

class RotateShortcut(AbsractAction):

    def execute(self) -> str:
        pyautogui.hotkey('ctrl', 'r')
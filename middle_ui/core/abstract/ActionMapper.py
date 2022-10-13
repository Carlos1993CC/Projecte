

from middle_ui.core.actions.add_file_button import AddFileButton
from middle_ui.core.actions.check_print_button_disabled import CheckPrintButtonDisabled
from middle_ui.core.actions.check_setCopies_disabled import CheckSetCopiesDisabled
from middle_ui.core.actions.close_alert_button import CloseAlertButton
from middle_ui.core.actions.get_nesting_state import GetNestingState
from middle_ui.core.actions.is_selected import IsSelected
from middle_ui.core.actions.open_history import OpenHistory
from middle_ui.core.actions.open_job_settings import OpenJobSettings
from middle_ui.core.actions.open_make_copies import OpenMakeCopies
from middle_ui.core.actions.press_ctrl_a import PressCtrlA
from middle_ui.core.actions.press_ctrl_click import PressCtrlClick
from middle_ui.core.actions.rotate_disabled import RotateDisabled
from middle_ui.core.actions.rotate_shortcut import RotateShortcut
from middle_ui.core.actions.print_checked import PrintChecked
from middle_ui.core.actions.open_preferences import OpenPreferences
from middle_ui.core.actions.check_locked_icon import CheckLockedIcon
from middle_ui.core.actions.check_unlocked_icon import CheckUnlockedIcon
from middle_ui.core.actions.check_logo_margins import CheckLogoMargins
from middle_ui.core.actions.check_cutting_lines import CheckCuttingLines
from middle_ui.core.actions.check_pageSizes import CheckPageSizes
from middle_ui.core.actions.check_pageSizes_thumbnail import CheckPageSizesThumbnail
from middle_ui.core.actions.check_TIFF_cuttingLines_visible import CheckTIFFCuttingLinesVisible
from middle_ui.core.actions.test import Test

class ActionMapper(object): 
    actions = {
        "open_job_settings" : OpenJobSettings,
        "close_alert_button" : CloseAlertButton,
        "add_file_button" : AddFileButton,
        "check_cutting_lines" : CheckCuttingLines,
        "check_TIFF_cuttingLines_visible" : CheckTIFFCuttingLinesVisible,
        "check_logo_margins" : CheckLogoMargins,
        "check_locked_icon" : CheckLockedIcon,
        "check_pageSizes" : CheckPageSizes,
        "check_pageSizes_thumbnail" : CheckPageSizesThumbnail,
        "check_print_button_disabled" : CheckPrintButtonDisabled,
        "check_setCopies_disabled" : CheckSetCopiesDisabled,
        "check_unlocked_icon" : CheckUnlockedIcon,
        "get_nesting_state" : GetNestingState,
        "is_selected" : IsSelected,
        "open_history" : OpenHistory,
        "open_make_copies" : OpenMakeCopies,
        "open_preferences" : OpenPreferences,
        "press_ctrl_a" : PressCtrlA,
        "press_ctrl_click" : PressCtrlClick,
        "print_checked" : PrintChecked,
        "rotate_disabled" : RotateDisabled,
        "rotate_shortcut" : RotateShortcut,
        "test" : Test
    }
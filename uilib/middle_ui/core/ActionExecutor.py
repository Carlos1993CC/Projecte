from typing import Dict
from middle_ui.core.abstract.AbstractAction import AbsractAction
from middle_ui.core.abstract.ActionMapper import ActionMapper

class ActionHandler(object):

    def __init__(self, actionID, args: Dict = {}) -> None:
        self.actionID = actionID
        self.args = args

    def execute(self) -> str:
        try:    
            ActionClass: AbsractAction = ActionMapper.actions[self.actionID]
            action = ActionClass(self.actionID, self.args)
            return action.execute()
        except Exception as e:
            raise e
     



    

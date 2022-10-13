
from argparse import Namespace
from middle_ui.core.ActionExecutor import ActionHandler
from middle_ui.launcher.Argument import Argument

if __name__ == "__main__":
    # Read arguments
    arguments: Namespace = Argument.parse_args()
    #Perform requested action
    actionHandler: ActionHandler = ActionHandler(arguments.action)
    output = actionHandler.execute()
    exit(output)

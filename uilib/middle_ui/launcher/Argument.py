
import argparse

class Argument(object):
    @staticmethod
    def parse_args() -> argparse.Namespace:
        parser = argparse.ArgumentParser()
        requiredArgs = parser.add_argument_group('required arguments')
        requiredArgs.add_argument('-a', '--action', type=str,
                                  metavar='action', help="Action to peform")
        return parser.parse_args()
   
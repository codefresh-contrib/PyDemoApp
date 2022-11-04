class Printer:
    def __init__(self, return_print_string: bool):
        self._return_print_string = return_print_string

    def print_func(self, print_str: str) -> str:
        print(print_str)
        if self._return_print_string:
            return print_str
        return ""
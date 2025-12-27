from ui.console import info
from ui.banner import BLUE, RESET

class Stats:
    def __init__(self):
        self.files=0
        self.comments=0
        self.blank=0

    def show(self):
        print(f"""{BLUE}
Files cleaned      : {self.files}
Comments removed   : {self.comments}
Blank lines removed : {self.blank}
{RESET}""")

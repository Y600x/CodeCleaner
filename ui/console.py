import os
GREEN="\033[92m"; RED="\033[91m"; RESET="\033[0m"

def clear_terminal():
    os.system("cls" if os.name=="nt" else "clear")

def info(m): print(f"{GREEN}[✔] {m}{RESET}")
def err(m): print(f"{RED}[✘] {m}{RESET}")

from ui.banner import CYAN, RESET

def progress_bar(i,total,w=40):
    p=int(i/total*100)
    f=int(w*i/total)
    bar="█"*f+"-"*(w-f)
    print(f"\r{CYAN}[{bar}] {p}%{RESET}",end="",flush=True)

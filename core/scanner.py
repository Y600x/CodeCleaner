import os
from utils.comments import COMMENT_SYMBOLS

def collect_files(path, recursive, exclude):
    files=[]
    if os.path.isfile(path):
        return [path]

    for root,dirs,fs in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude]
        for f in fs:
            if any(f.endswith("."+k) for k in COMMENT_SYMBOLS):
                files.append(os.path.join(root,f))
        if not recursive:
            break
    return files

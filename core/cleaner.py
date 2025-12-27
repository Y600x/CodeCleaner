import shutil
from utils.comments import COMMENT_SYMBOLS

def clean_file(src, dst, args, stats):
    ext = src.split(".")[-1]
    comment = COMMENT_SYMBOLS.get(args.lang or ext)

    with open(src,"r",errors="ignore") as f:
        lines = f.readlines()

    if args.min_lines and len(lines) < args.min_lines:
        return

    cleaned=[]
    for l in lines:
        s=l.strip()
        if not s:
            stats.blank+=1; continue
        if comment and s.startswith(comment):
            stats.comments+=1; continue
        cleaned.append(l)

    stats.files+=1

    if args.dry_run:
        return

    if args.backup:
        shutil.copy(src, src+".bak")

    with open(dst,"w") as f:
        f.write("# Cleaned by FlashBytes-Team | Telegram : @FlashBytess\n\n")
        f.writelines(cleaned)

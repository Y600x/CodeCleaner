#!/usr/bin/env python3
from ui.console import clear_terminal, info, err
from ui.banner import banner
from ui.progress import progress_bar
from core.scanner import collect_files
from core.cleaner import clean_file
from core.stats import Stats
from utils.report import generate_report

import argparse, os, sys, time
from concurrent.futures import ThreadPoolExecutor

def main():
    clear_terminal()

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h","--h","--help",action="help",help="Show help")

    parser.add_argument("-i","--input",help="File or directory")
    parser.add_argument("-o","--output",help="Output file")
    parser.add_argument("-r","--recursive",action="store_true")
    parser.add_argument("--backup",action="store_true")
    parser.add_argument("--stats",action="store_true")
    parser.add_argument("--no-banner",action="store_true")

    parser.add_argument("--dry-run",action="store_true")
    parser.add_argument("--exclude",default="")
    parser.add_argument("--lang")
    parser.add_argument("--threads",type=int,default=1)
    parser.add_argument("--report")
    parser.add_argument("--min-lines",type=int)
    parser.add_argument("--ci",action="store_true")
    parser.add_argument("--sign",action="store_true")
    parser.add_argument("--format")

    args = parser.parse_args()

    if not args.no_banner and not args.ci:
        banner()

    if not args.input:
        err("Missing -i / --input")
        sys.exit(1)

    stats = Stats()
    exclude = args.exclude.split(",") if args.exclude else []

    files = collect_files(args.input, args.recursive, exclude)
    if not files:
        err("No supported files found")
        return

    with ThreadPoolExecutor(max_workers=args.threads) as exe:
        for i,f in enumerate(files,1):
            out = args.output or f + ".clean"
            exe.submit(clean_file, f, out, args, stats)
            progress_bar(i, len(files))
            time.sleep(0.01)

    print()
    info("Done")

    if args.stats:
        stats.show()

    if args.report:
        generate_report(args.report, stats)

    if args.sign:
        info("GPG sign placeholder")

if __name__ == "__main__":
    main()

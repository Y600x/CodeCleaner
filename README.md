# CodeCleaner
CodeCleaner is a professional Python-based command-line tool designed to clean source code by removing programming comments and excessive blank lines.  
It supports more than 14 programming languages and follows a clean, minimal CLI style similar to professional security and development tools.

---

## Features

- Removes line comments (`#`, `//`)
- Removes extra blank lines
- Supports more than 14 programming languages
- Works with single files and directories
- Recursive directory scanning
- Dry-run mode (no file modification)
- Detailed statistics
- Multi-threaded processing
- Report generation (JSON / TXT)
- Automatic file backups
- ANSI-colored output with optional banner
- CI-friendly mode
- Modular and extensible architecture

---

## Supported Languages

- Python  
- Bash  
- Ruby  
- YAML  
- INI / CONF  
- JavaScript  
- TypeScript  
- Java  
- C / C++  
- C#  
- Go  
- PHP  
- Swift  
- Kotlin  

---

## Project Structure

```text
codecleaner/
├── codecleaner.py          # CLI entry point
├── core/                   # Core cleaning logic
├── ui/                     # Console UI, banner, progress bar
├── utils/                  # Helpers and reporting
├── examples/               # Test files
├── README.md
└── requirements.txt


---

Installation

git clone https://github.com/Y600x/codecleaner.git
cd codecleaner
python3 codecleaner.py -h

No external dependencies are required.


---

Usage

Show help

python codecleaner.py -h

Clean a single file

python codecleaner.py -i test.py

Specify output file name

python codecleaner.py -i test.py -o test.clean.py

Clean a directory recursively

python codecleaner.py -i src/ -r

Create backup and show statistics

python codecleaner.py -i app.py --backup --stats

Dry run (no changes applied)

python codecleaner.py -i app.py --dry-run


---

Available Options

Option	Description

-h, --h, --help	Show help message
-i, --input	Input file or directory
-o, --output	Output file name
-r, --recursive	Recursive scan
--backup	Create a backup of the original file
--stats	Display statistics
--no-banner	Disable banner output
--dry-run	Simulate execution without writing files
--exclude	Exclude files or directories
--lang	Force language detection
--threads	Number of threads to use
--report	Generate a report (JSON or TXT)
--min-lines	Minimum number of lines required to process a file
--ci	CI mode (no colors or banner)
--sign	GPG signing (placeholder)
--format	Code formatting (placeholder)



---

Example Test File

A test file is provided for validation and experimentation:

examples/test.py


---

Security and Notes

Docstrings are preserved by default

The tool does not modify code logic

Safe for use in CI/CD pipelines

Designed for maintainability and future expansion




---

Author and Team

FlashBytes-Team
Telegram: https://t.me/FlashBytess


---

Disclaimer

This tool is intended for educational and development purposes only.
The authors are not responsible for misuse.


---

Support

If you find this project useful, consider starring the repository, submitting issues, or contributing improvements.

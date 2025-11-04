import sys
from pathlib import Path
from colorama import Fore, Style


COLOR_DIR = Fore.BLUE + Style.BRIGHT
COLOR_FILE = Fore.GREEN
COLOR_RESET = Style.RESET_ALL

SPACE = "    "


def display_dir_structure(path: Path, prefix: str = ''):
    contents = sorted([
        item for item in path.iterdir() if item.name not in ('.git', '__pycache__', 'venv', 'venv_hw04')
    ], key=lambda x: (not x.is_dir(), x.name))

    for item in contents:
        connector = SPACE
        output = f"{prefix}{connector}"

        if item.is_dir():
            dir_name = item.name
            print(f"{output}{COLOR_DIR}{dir_name}/{COLOR_RESET}")
            new_prefix = prefix + SPACE
            display_dir_structure(item, new_prefix)

        elif item.is_file():
            file_name = item.name
            print(f"{output}{COLOR_FILE}{file_name}{COLOR_RESET}")


def main():
    target_path = Path(sys.argv[1])
    print(f"{COLOR_DIR}{target_path.name}/{COLOR_RESET}")
    display_dir_structure(target_path)


if __name__ == "__main__":
    main()

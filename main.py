import argparse
import os
import sys


def get_dir_size(path):
    """
    Calculate the size of a directory including all subdirectories and files.
    Takes input argument as the path to the directory.
    Returns total size of the directory in bytes.
    """
    size = 0
    for dir_path, dir_name, sub_dirs in os.walk(path):
        for sub_dir in sub_dirs:
            sub_dir_path = os.path.join(dir_path, sub_dir)
            size += os.path.getsize(sub_dir_path)
    return size


def print_dir_size(dir, recursive=False, human=False, indent=""):
    """
    Print the size of a directory and optionally its subdirectories based on input recursive flag.
    Takes input argument as the directory path, optional recursive flag, optional human flag, and optional indent string.
    Returns total size of the directory in bytes.
    """
    size = get_dir_size(dir)
    print(f"{indent}{dir}: {format_size(size, human)}")
    if recursive:
        for sub_dir in os.listdir(dir):
            sub_dir_path = os.path.join(dir, sub_dir)
            if os.path.isdir(sub_dir_path):
                print_dir_size(sub_dir_path, recursive, human, indent + " ")
    return size


def format_size(size, human):
    """
    Format the size given in bytes to a human readable format based on input human flag.
    Takes input argument as the directory size in bytes, and optional human flag.
    Returns formatted size in a String format.
    """
    if not human:
        return f"{size} bytes."
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(size) < 1024:
            return f"{size} {unit}B."
        size //= 1024
    return f"{size} YB."


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="List of directories: ")
    parser.add_argument('dirs', nargs='*')
    parser.add_argument('--recursive', action='store_true')
    parser.add_argument('--human', action='store_true')
    args = parser.parse_args()
    if len(args.dirs) == 0:
        print("Please provide at least one directory!")
        parser.print_help()
        sys.exit(1)
    cumulative_size = 0
    for dir in args.dirs:
        if os.path.isdir(dir):
            size = print_dir_size(dir, args.recursive, args.human)
            cumulative_size += size
        else:
            print("Not a Valid Directory!")
    print(f"Cumulative Total: {format_size(cumulative_size, args.human)}")


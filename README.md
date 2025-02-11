# Storage Evaluator Tool

This command-line utility calculates and displays the sizes of directories. It supports multiple directories, recursive size calculation, and human-readable output formats.

## Features

- Calculate sizes of multiple directories
- Recursive calculation of subdirectory sizes (optional)
- Human-readable size format (optional)
- Cumulative total size calculation

## Requirements

- Python 3.x

## Usage

Run the script from the command line with the following syntax:
`python3 main.py /path/to/dir_1 /path/to/dir_2 /path/to/dir_n --recursive --human`


### Arguments

- `dir_1 dir_2 dir_n`: One or more directories to calculate sizes for.

### Options

- `--recursive`: Calculate sizes recursively, including all subdirectories.
- `--human`: Display sizes in human-readable format (e.g., KB, MB, GB).

## Output

The script will display the size of each specified directory (and subdirectories if --recursive is used), followed by a cumulative total of all directories.

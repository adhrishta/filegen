import os
import argparse
import sys

def parse_size(size_str):
    """Convert size input (e.g., 1KB, 2MB, 3GB) to bytes."""
    if not size_str:
        raise ValueError("File size must be specified.")

    size_str = str(size_str).upper().strip()  # Ensure it's a string
    units = {"KB": 1024, "MB": 1024**2, "GB": 1024**3}

    for unit in units:
        if size_str.endswith(unit):
            return int(size_str[:-len(unit)]) * units[unit]
    
    return int(size_str)  # Assume bytes if no unit is provided

def create_files(num_files, file_size, output_dir):
    """Creates multiple files with a specified size in the given directory."""
    
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists
    
    for i in range(1, num_files + 1):
        file_path = os.path.join(output_dir, f"file_{i}.smpl")
        
        with open(file_path, "wb") as f:
            f.write(os.urandom(file_size))  # Write random data
        
        print(f"Created: {file_path}")

def print_help():
    """Displays custom help message."""
    help_text = """
Usage: python FileGen.py -n NUM -s SIZE -o OUTPUT

Arguments:
  -n, --num     Number of files to create (e.g., 100)
  -s, --size    Size of each file (e.g., 1KB, 1MB, 1GB)
  -o, --output  Output directory for generated files

Examples:
  python FileGen.py -n 10 -s 512KB -o test_files
  python FileGen.py -n 20 -s 1MB -o output_folder
"""
    print(help_text)
    sys.exit(0)  # Exit after showing help

def main():
    parser = argparse.ArgumentParser(description="Generate multiple files of a given size.", add_help=False)
    parser.add_argument("-n", "--num", type=int, help="Number of files to create (e.g., 100)")
    parser.add_argument("-s", "--size", type=str, help="Size of each file (e.g., 1KB, 1MB, 1GB)")
    parser.add_argument("-o", "--output", type=str, help="Output directory (e.g., my_files)")

    # Manually check for help argument
    if "-h" in sys.argv or "--help" in sys.argv:
        print_help()

    args = parser.parse_args()

    try:
        # Handle missing arguments with user input
        if args.num is None:
            args.num = int(input("Enter the number of files to create: "))

        if args.size is None:
            args.size = input("Enter the file size (e.g., 1KB, 1MB, 1GB): ")

        if args.output is None:
            args.output = input("Enter the output directory name: ")

        file_size_bytes = parse_size(args.size)  # Convert size input to bytes
        create_files(args.num, file_size_bytes, args.output)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting.")
        sys.exit(0)  # Exit without error

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)  # Exit with error status

if __name__ == "__main__":
    main()

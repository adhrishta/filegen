import os
import argparse
import sys

def parse_size(size_str):
    """Convert size input (e.g., 1KB, 2MB, 3GB) to bytes."""
    if not size_str:
        raise ValueError("File size must be specified.")

    size_str = str(size_str).strip().upper()
    units = {"KB": 1024, "MB": 1024**2, "GB": 1024**3}

    for unit in units:
        if size_str.endswith(unit):
            number = float(size_str[:-len(unit)].strip())
            return int(number * units[unit])
    
    return int(size_str)  # Assume bytes if no unit is provided

def validate_inputs(num_files, file_size):
    if num_files <= 0:
        raise ValueError("Number of files must be greater than 0.")
    if file_size <= 0:
        raise ValueError("File size must be greater than 0 bytes.")

def create_files(num_files, file_size, output_dir):
    """Creates multiple .txt files with 'lorem ipsum' content up to specified size."""
    os.makedirs(output_dir, exist_ok=True)
    content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    content_bytes = content.encode("utf-8")
    content_len = len(content_bytes)

    for i in range(1, num_files + 1):
        file_path = os.path.join(output_dir, f"file_{i}.txt")
        with open(file_path, "wb") as f:
            written = 0
            while written + content_len <= file_size:
                f.write(content_bytes)
                written += content_len
            if written < file_size:
                f.write(content_bytes[:file_size - written])
        print(f"Created: {file_path} ({file_size} bytes)")

def print_help():
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
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="Generate multiple .txt files with lorem ipsum content.", add_help=False)
    parser.add_argument("-n", "--num", type=int, help="Number of files to create")
    parser.add_argument("-s", "--size", type=str, help="Size of each file (e.g., 1KB, 1MB)")
    parser.add_argument("-o", "--output", type=str, help="Output directory")

    if "-h" in sys.argv or "--help" in sys.argv:
        print_help()

    args = parser.parse_args()

    try:
        if args.num is None:
            args.num = int(input("Enter the number of files to create: "))
        if args.size is None:
            args.size = input("Enter the file size (e.g., 1KB, 1MB): ")
        if args.output is None:
            args.output = input("Enter the output directory name: ")

        file_size_bytes = parse_size(args.size)
        validate_inputs(args.num, file_size_bytes)
        create_files(args.num, file_size_bytes, args.output)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting.")
        sys.exit(0)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

# FileGen
Simple app to automatically generate dummy text (.txt) file(s) 

Usage: python FileGen.py -n NUM -s SIZE -o OUTPUT

Arguments:
  -n, --num     Number of files to create (e.g., 100)
  -s, --size    Size of each file (e.g., 1KB, 1MB, 1GB)
  -o, --output  Output directory for generated files

Examples:
  python FileGen.py -n 10 -s 512KB -o test_files
  python FileGen.py -n 20 -s 1MB -o output_folder
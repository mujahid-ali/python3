#!/usr/bin/python3
# It will replace the first line of the file (if contains) from python to python3
import sys

def main():
    filename = sys.argv[1]
    with open(filename) as fin:
        lines = fin.readlines()
    lines[0] = lines[0].replace('python', 'python3')
    print(lines[0])
    with open(filename, 'w') as fout:
        for line in lines:
            fout.write(line)

if __name__ == "__main__":
    sys.exit(main())

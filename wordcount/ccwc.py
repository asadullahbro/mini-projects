#!/usr/bin/env python3
import sys
def print_usage():
    print("Usage: ccwc [OPTION] <filename>\nIf no OPTION is given, ccwc outputs lines, words, and bytes.")
    print("Options:")
    print("  -c   count bytes")
    print("  -m   count characters")
    print("  -w   count words")
    print("  -l   count lines")

def count_bytes(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return len(data)
def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return len(lines)
def count_words(filename):
    with open(filename, "r", encoding="utf-8") as w:
        text = w.read()
        words = len(text.split())
    return words
def char_count(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.read()
    return len(text)
def main():
    args = sys.argv[1:]
    if len(args) == 0 or len(args) > 2:
        print_usage()
        sys.exit(1)
    if len(args) == 1:
        filename = sys.argv[0]
        try:
            lines = count_lines(filename)
            words = count_words(filename)
            bytes_ = count_bytes(filename)
            print(f"{lines}\t{words}\t{bytes_} {filename}")
        except FileNotFoundError:
            print(f"Error: file '{filename}' not found.")
    else:
        option, filename = args
        try:
            if option == "-c":
                byte_count = count_bytes(filename)
                print(f"{byte_count} {filename}")
            elif option == "-l":
                line_count = count_lines(filename)
                print(f'{line_count} {filename}')
            elif option == "-w":
                word_count = count_words(filename)
                print(f'{word_count} {filename}')
            elif option == "-m":
                chars = char_count(filename)
                print(f"{chars} {filename}")
            else:
                print_usage()
                sys.exit(1)
        except FileNotFoundError:
            print(f"Error: file '{filename}' not found.")
if __name__ == "__main__":
    main()

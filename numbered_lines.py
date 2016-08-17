#!/usr/bin/env python3


def numbered_lines():
    with open("small.txt", "r") as small_file:
        with open("big.text", "w") as big_file:
            line_counter = 1
            small_file_lines = small_file.read().split("\n")
            for small_file_line in small_file_lines:
                if small_file_line.strip() != "":
                    big_file.writelines(
                        str(line_counter) + " " + small_file_line + "\n")
                    line_counter += 1


def main():
    numbered_lines()

if __name__ == "__main__":
    main()

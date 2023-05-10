#!/usr/bin/env python3

import sys
import os


def to_snake_case(string):
    output = ""
    for i, v in enumerate(string):
        if v.isupper() and i < len(string) - 1:
            output += "_"
        output += v.lower()
    return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        os.rename(sys.argv[1], to_snake_case(sys.argv[1]))
        print(f"Successfully renamed file: {sys.argv[1]}")

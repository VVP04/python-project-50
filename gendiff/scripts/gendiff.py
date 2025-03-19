#!/usr/bin/env python3
from gendiff.cli import get_args
from gendiff.engine import generate_diff


def main():
    args = get_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
  
    
if __name__ == '__main__':
    main()
import argparse


def get_args():
    parser = argparse.ArgumentParser(
    prog='gendiff',
    description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        dest='format',
        default='stylish',
        type=str,
        help='set format of output',
    )
    args = parser.parse_args()
    return args
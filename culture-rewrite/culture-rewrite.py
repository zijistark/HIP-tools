#!/usr/bin/python
__author__ = 'zijistark'
VERSION = '0.1.0'


import os
import sys
import traceback
import argparse
import history


def get_args():
    parser = argparse.ArgumentParser(
        description="Split or merge cultures throughout CKII character history files automatically.",
    )
    parser.add_argument('input-file', metavar='FILENAME',
                        help='name of CSV file containing dynasty and early -> later culture mappings')
    parser.add_argument('--date', required=True,
                        help='date at which the early -> later cultural transition occurs for characters, '
                             'based upon their birth date (e.g., 1120.1.1)')
    parser.add_argument('--history-dir', required=True,
                        help='path to directory from which to load preexisting character history')
    parser.add_argument('--output-history-dir', default='./characters',
                        help='path at which the new character history directory should be created [default: '
                             '%(default)s]')
    parser.add_argument('--force', '-f', action='store_true',
                        help='if the given new character history directory already exists, '
                             'delete it, and recreate it with the new character history')
    parser.add_argument('--verbose', '-v', action='count', default=0,
                        help='show verbose information about what the script is doing;'
                             'repeat this option multiple times for increasing amounts of information')
    parser.add_argument('--version', '-V', action='version', version='%(prog)s '+VERSION,
                        help='show program version and quit')
    parser.add_argument('--debug', '-D', action='store_true',
                        help='show program debugging information')
    return parser.parse_args()


def main():
    args = get_args()
    try:
        print(str(args)+'\n')

        # TODO: check input file exists and open cleanly

        char_hist = history.CharHistory(sys.stdout, args.verbose)
        char_hist.parse_dir(args.history_dir)
        print(str(char_hist.files['italian_tuscan.txt']))

        return 0

    except:
        sys.stderr.write('\nUnexpected fatal error occurred! Stack trace:\n\n')
        traceback.print_exc(file=sys.stderr)
        return 255



if __name__ == '__main__':
    sys.exit(main())

import argparse

def main(args):
    def init():
        parser = argparse.ArgumentParser(
            description='This program solves project Euler (https://projecteuler.net/) problem #54',
            epilog="Copyright (c) 2019 Bradley Workman"
            )

        parser.add_argument('-f','--file', required=True, dest='file', metavar='<file>', help="""Input file with poker hands. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.""")

        return parser.parse_args(args[1:])

    # parse arguments
    args = init()


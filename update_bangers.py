import argparse

BANGER_LIST_FILE = 'a-banger-a-day.txt'
BANGER_GUESSING_GAME_FILE = 'banger-guessing-game.txt'
BANGER_SNIPPET_GUESSING_GAME_FILE = 'banger-snippet-guessing-game.txt'


def add_line_to_file(file_name, line):
    with open(file_name, 'a') as f:
        f.write(line)
        f.write('\n')

def add_banger(args):
    banger_text = args.date + ": " + args.artist + " - " + args.title
    add_line_to_file(BANGER_LIST_FILE, banger_text)
    add_line_to_file(BANGER_SNIPPET_GUESSING_GAME_FILE, banger_text)
    if args.lyrics:
        add_line_to_file(BANGER_GUESSING_GAME_FILE, banger_text)
    print(f"Added Banger:\n{banger_text}")


parser = argparse.ArgumentParser(description='Process some integers.')
subparsers = parser.add_subparsers()
parser_update = subparsers.add_parser('add', help='Add a banger')
parser_update.add_argument('-d', '--date', metavar='DATE', type=str, required=True,
                    help='Banger Date as dd.mm.yy')
parser_update.add_argument('-a', '--artist', metavar='ARTIST', type=str, required=True,
                    help='Banger Artist')
parser_update.add_argument('-t', '--title', metavar='TITLE', type=str, required=True,
                    help='Banger Title')
parser_update.add_argument('-l', '--lyrics', action='store_true',
                    help='Add Banger to BangerGuessingGame list')
parser_update.set_defaults(func=add_banger)

args = parser.parse_args()
args.func(args)
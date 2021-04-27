import argparse

BANGER_LIST_FILE = 'a-banger-a-day.txt'
BANGER_GUESSING_GAME_FILE = 'banger-guessing-game.txt'
BANGER_SNIPPET_GUESSING_GAME_FILE = 'banger-snippet-guessing-game.txt'
LINE_FEED = '\n'.encode('utf8')


def upload():
    # Receive auth token
    with open("usr-pass.txt", "r") as up:
        data = up.read()
        token = data.rstrip("\n")
    g = github.Github("token")
    repo = g.get_repo("TheSuperDodo/a-banger-a-day")
    file = repo.get_contents("a-banger-a-day.txt")
    bangers = ""
    with open (BANGER_LIST_FILE, "r") as bangersFile:
        bangers=bangersFile.read()
    repo.update_file("a-banger-a-day.txt", args.date, bangers, file.sha)

def add_line_to_file(file_name, line):
    with open(file_name, 'ab') as f:
        f.write(LINE_FEED)
        f.write(line)

def add_banger(args):
    banger_text = args.date + ": " + args.artist + " - " + args.title
    unicode_banger_text = banger_text.encode('utf8')
    add_line_to_file(BANGER_LIST_FILE, unicode_banger_text)
    add_line_to_file(BANGER_SNIPPET_GUESSING_GAME_FILE, unicode_banger_text)
    if args.lyrics:
        add_line_to_file(BANGER_GUESSING_GAME_FILE, unicode_banger_text)
    print(f"Added Banger:\n{unicode_banger_text}")
    upload()


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



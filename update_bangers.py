import argparse, github, base64

BANGER_LIST_FILE = 'a-banger-a-day.txt'
BANGER_GUESSING_GAME_FILE = 'banger-guessing-game.txt'
BANGER_SNIPPET_GUESSING_GAME_FILE = 'banger-snippet-guessing-game.txt'
LINE_FEED = '\n'.encode('utf8')

def get_repo():
# Receive auth token
    with open("usr-pass.txt", "r") as up:
        data = up.read()
        token = data.rstrip("\n")
        g = github.Github(token)
        return g.get_repo("TheSuperDodo/a-banger-a-day")
    
def download(fileToDownload, repo):
    gitBangerFile = base64.b64decode(repo.get_contents(fileToDownload).content)
    with open (fileToUpload, "wb") as bangersFile:
        bangersFile.write(gitBangerFile)

def upload(fileToUpload, repo):
    gitBangerFile = repo.get_contents(fileToUpload)
    bangers = ""
    with open (fileToUpload, "rb") as bangersFile:
        bangers=bangersFile.read()
    repo.update_file(fileToUpload, args.date, bangers, gitBangerFile.sha)

def add_line_to_file(file_name, line):
    repo = get_repo()
    download(file_name, repo)
    with open(file_name, 'ab') as f:
        f.write(LINE_FEED)
        f.write(line)
    upload(file_name, repo)
    

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



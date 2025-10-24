import sys
from stats import count, countChars, sortedDicts

def get_book_text(path):
    content = ''
    with open(path) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    print('============ BOOKBOT ============')
    print('Analyzing book found at {path}...'.format(path=path))
    print('----------- Word Count ----------')
    print('Found {nb} total words'.format(nb=count(text)))
    print('--------- Character Count -------')
    sored = sortedDicts(countChars(text))
    for dico in sored:
        char = dico['char']
        num = dico['num']
        if char.isalpha() == False:
            continue
        print('{char}: {num}'.format(char=char, num=num))
    print('============= END ===============')

main()

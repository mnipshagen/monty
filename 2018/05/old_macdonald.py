import re

def read_verse(filename):
    with open(filename) as f:
        verse = f.read()
    f.closed

    return verse

def delete_meow(verse):
    return verse

def sing_song(verse):
    print(verse)


verse = read_verse('old_macdonald.txt')

verse = delete_meow(verse)

sing_song(verse)

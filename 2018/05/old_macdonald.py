import re

# this is just to read in the song text.
# stay tuned for next week when we talk about file in- & output
def read_verse(filename):
    """This reads in a file and returns a its contents."""
    with open(filename) as f:
        verse = f.read()
    f.closed

    return verse

# implement this
def delete_meow(verse):
    return verse

# impement this as well
def sing_song(verse):
    print(verse)

# and here we go!
verse = read_verse('old_macdonald.txt')
verse = delete_meow(verse)
sing_song(verse)
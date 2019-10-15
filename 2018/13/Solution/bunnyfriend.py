"""
This module implements the Bunnyfriend class.

  A BunnyFriend is a creature that is born small and fluffy and has
      the dream of becoming a big, full-grown bunny!
  We want to help its dream come true by feeding and playing with it,
but be careful... if you don't play enough, it might grow to resent you...
"""
__all__ = ["Bunnyfriend"]

import time

from hangman import game


class Bunnyfriend:
    """
    This class represents a small bunny to care for in a Tamagotchi-like manner.

    A bunnyfriend can be in 1 of 4 moods: happy, sad, grown_happy and grown_angry.
    There are 5 class variables for that matter:
    There are four constants, one for each mood: HAPPY, SAD, GROWN_HAPPY, GROWN_ANGRY
    and there is ILLUSTRATIONS which is a dictionary mapping from the moods onto 
    ASCII art representing the mood.

    A bunnyfriend can be played with or fed. Each day one meal is consumed by the
    bunnyfriend. The bunnyfriend can also be taught some words that can be used
    in a game of hangman. There are some words already to mix them up and make the
    game more interesting. However, until the bunnyfriend has not learned a word,
    playing will not start a round of hangman.

    If the bunnyfriend comes of age or its food level reaches 0, the bunny will venture
    out into the world and no longer be interactable.
    """
    HAPPY = "happy"
    SAD = "sad"
    GROWN_HAPPY = "grown happy"
    GROWN_ANGRY = "grown angry"

    with open("happy.txt") as happy,\
        open("sad.txt") as sad,\
        open("grown_happy.txt") as grown_happy,\
        open("grown_angry.txt") as grown_angry:
        ILLUSTRATIONS = {
            HAPPY : happy.read(),
            SAD : sad.read(),
            GROWN_HAPPY : grown_happy.read(),
            GROWN_ANGRY : grown_angry.read()
        }

    def __init__(
        self,
        name,
        food_capacity=3,
        days_to_grow=10,
        play_to_grow_happy=15
    ):
        """
        Constructs a new bunnyfriend.

        Each bunnyfriend starts with two meals already in its belly and at age 0.
        All bunnyfriends also begin their life happy and with no learned words.

        Args:
            name:
                the name of the bunny friend
            food_capacity:
                how much food the bunny stomach can fit
            days_to_grow:
                How many days have to pass before the bunny grows
            play_to_grow_happy:
                How many times the bunny friend needs to be played with to grow
                up happily
        """
        self.name = name
        self._food_capacity = food_capacity
        self._current_food = 2
        self.age = 0
        self._played = 0
        self._days_to_grow = days_to_grow
        self._play_to_grow_happy = play_to_grow_happy
        self._mood = Bunnyfriend.HAPPY
        self._learned_words = False
        self._learned_words_file = open("words.txt", "a+")
        self._interactable = True
        self._played_today = False

    @property
    def interactable(self):
        """Wrapper for read-only interactable property."""
        return self._interactable

    def _play(self):
        """
        Plays with the bunnyfriend.

        Raises the play counter by 1 so it can grow up happy, an also flags
        played_today as true for the mood adjustment. If the bunnyfriend
        has already learend a word, a round of hangman is played.
        """
        self._played_today = True
        self._played += 1

        if self._learned_words:
            game()

    def _feed(self):
        """
        Feeds the bunnyfriend one meal.

        Returns:
            True if feeding was successfull, False if stomach is at full capacity
        
        Raises:
            ValueError:
                When the amount of current food is below 0 or beyond the capacity
        """
        if 0 < self._current_food < self._food_capacity:
            self._current_food += 1
            return True
        if self._current_food == self._food_capacity:
            return False
        else:
            raise ValueError("Something is wrong with the bunny's stomach. "
                f"It has {self._current_food} out of {self._food_capacity} "
                "meals in his belly.")

    def _teach_word(self):
        """
        Teaches the bunnyfriend a new word for a hangman game.

        All words will be transformed into lowercase and all whitespace removed.
        The user can then choose whether the transformed word should be learned.
        If so, the word is appended to the words file which holds the words for
        hangman. It also flags _learned_words as True.

        Returns:
            The newly learned word
        """
        self._learned_words = True
        
        correct = False
        while not correct:
            word = input(f"What word shall {self.name} learn?")
            word = ''.join(word.lower().split())
            correct = input(f'Is "{word}" the word you want to teach (y/n): ').lower() == 'y'

        self._learned_words_file.writeline(word)
        return word

    def interact(self):
        """
        Interact with the bunnyfriend.

        Asks the user what they want to do with the bunnyfriend. They can choose
        to feed it, okay with it, or teach it a new word. If none of those options
        the bunnyfriend is ignored, and nothing happens.

        Returns:
            True if interaction is done, False if bunnyfriend is not interactable
        """
        if not self.interactable:
            return False

        feed_lst = ['feed', 'f']
        play_lst = ['play', 'p']
        teach_lst = ['teach', 't']

        print("You can feed (f), play with (p) or teach a word (t) to your bunny friend."
            f" Input anything else to ignore {self.name} for now.")
        action = input("What do you want to do? (f/p/t) ").lower()
        if action in feed_lst + play_lst + teach_lst:
            time.sleep(1)

        if action in feed_lst:
            if self._feed():
                print(f"You fed {self.name}. Delicious!")
            else:
                print(f"{self.name} is not hungry right now.")
        elif action in play_lst:
            self._play()
            print(f"You played with {self.name}. What a good time.")
        elif action in teach_lst:
            word = self._teach_word()
            print(f"Wow! What a smart bunny. {self.name} knows {word} now!")
        else:
            print(f"You let {self.name} be for now and mind your own stuffs.")

        return True

    
    def pass_day(self):
        """
        Passes a day in the bunnyfriend's life.

        The bunnyfriend will age by 1 and will consume one meal. If the current
        food capacity will sink below one with that, the bunnyfriend will run
        away. It updates the mood of the bunnyfriend accordingly whether it 
        was played with today.

        If the aged bunnyfriend has reached the days it needs to grow, it will
        grow up.
        """
        self._current_food -= 1
        if self._current_food < 1:
            self._run_away()

        self._mood = Bunnyfriend.HAPPY if self._played_today else Bunnyfriend.SAD

        self._played_today = False
        self.age += 1

        if self.age == self._days_to_grow:
            self._grow()

    def _grow(self):
        """
        The bunnyfriend grows up!

        Depending on whether the bunnyfriend was played with enough or not,
        it will grow up to be either happy or angry. The grown-up bunnyfriend
        will not be interactable. In the end the grown bunnyfriend will be 
        printed.
        """
        if self._played >= self._play_to_grow_happy:
            self._mood = Bunnyfriend.GROWN_HAPPY
        else:
            self._mood = Bunnyfriend.GROWN_ANGRY
        
        self._interactable = False
        print(self)

    def _run_away(self):
        """
        The bunnyfriend was not cared for and ran away.

        An underfed bunnyfriend will be sad and run away. This means it will no
        longer be interactable and leave the user.
        """
        self._mood = Bunnyfriend.SAD
        self._interactable = False
        print(self)

    def __str__(self):
        """Prints a representation of the current state of the bunnyfriend."""
        if self.interactable:
            return (
                f"{self.name} is {self._mood} and its food level is at "
                f"{self._current_food}/{self._food_capacity}.\n"
                f"{Bunnyfriend.ILLUSTRATIONS[self._mood]}"
            )
        elif self._mood == Bunnyfriend.GROWN_ANGRY:
            return (
                f"{Bunnyfriend.ILLUSTRATIONS[self._mood]}\n"
                f"{self.name} has been transformed by your unloving care. It is "
                f"now a monstrous, angry bunny. You better run."
            )
        elif self._mood == Bunnyfriend.GROWN_HAPPY:
            return (
                f"{Bunnyfriend.ILLUSTRATIONS[self._mood]}\n"
                f"Thanks to your good care, {self.name} has grown up to be a "
                f"happy adult monster bunny. {self.name} ventures out to explore"
                f" the world and see what more there is to do."
            )
        else:
            return f"{self.name} has left to explore the world and seek fortune."

    def __del__(self):
        self._learned_words_file.close()
        print("closed file")

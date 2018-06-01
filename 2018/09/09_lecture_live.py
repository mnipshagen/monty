
# coding: utf-8

# In[14]:

class Person:
    
    def __init__(self, surname, firstname, height, age, weight, favorite_colour='blue'):
        self.surname = surname
        self.firstname = firstname
        self.height = height
        self.age = age
        self.weight = weight
        self.favorite_colour = favorite_colour
        
    def bmi(self):
        return self.weight / (self.height**2)

    def greet(self, other_person):
        print(f"{self}: I am greeting {other_person}")
        other_person.be_greeted(self)
        
    def be_greeted(self, other_person):
        print(f"{self}: I am greeted by {other_person}")
    
    def __str__(self):
        return f"{self.firstname} {self.surname}"


# In[17]:

mo = Person('Nipshagen','Moritz',1.81,24,10)
antonia = Person('Hain','Antonia',1.63,22,10,'42')


antonia.greet(mo)


# In[23]:

class PartOfUniversity:
    
    def __init__(self, id_, university_name):
        self.id = id_
        self.university = university_name
        
    def belongs_to(self):
        return self.university


# In[28]:

class Student(Person, PartOfUniversity):
    
    def __init__(self, surname, first_name, height, age, weight, fav_colour, matriculation_number, university):
        Person.__init__(self, surname, first_name, height, age, weight, fav_colour)
        PartOfUniversity.__init__(self, matriculation_number, university)
        
    def __str__(self):
        return Person.__str__(self) + f", from {self.university}"


# In[29]:

antonia = Student('Hain','Antonia',1.63,22,10,'42', 123987, 'Harvard University')


# In[30]:

mo.greet(antonia)


# In[1]:

class Hangman:
    
    def __init__(self, word, max_tries):
        self.word = word
        self.tries = max_tries
        self.guessword = ['_' for _ in range(len(self.word))]
        self.guesses = []
    
    def update_guessword(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.guessword[i] = guess
        
        
    def play(self):
        while self.tries > 0 and '_' in self.guessword:
            print(self.guessword)
            print("Guesses so far:", self.guesses)
            
            guess = input("Next guess: ")
            if guess in self.word:
                self.update_guessword(guess)
            else:
                self.tries -= 1
                self.guesses.append(guess)
        
        self.end()
        
    def end(self):
        if not '_' in self.guessword:
            print("You win! Awesome!")
        else:
            print("You hang. Better luck in your next life!")


# In[2]:

game = Hangman("lemon",5)


# In[5]:

game.play()


# In[ ]:




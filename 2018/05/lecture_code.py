import re

# pattern =''; string = ''
# re.search(pattern, string)

# import re

# print(re.match("a", "a"))
# print(re.match("abc", "abc"))

# print(re.match("a(b)", "ab"))

# print(re.match("ba*", "b"))
# print(re.match("ba*", "baaa"))

# print(re.match("(a|b|ab)cd", "acd"))
# print(re.match("(a|b|ab)cd", "abcd"))

# print(re.match("1+", "1111111"))
# print(re.match("ha?llo", "hllo"))
# print(re.match("ha?llo", "haallo"))
# print(re.match(""))

print(re.match("\\\\", "\\"))
print(re.match(r"\\", "\\"))
print(r'quote \'')

match = re.match(r"(a*)b\1", "aabaaa")
print(match[0])
match = re.match(r"(a*)b\1", "aaba")
print(match)
match = re.match(r"(a*)(b{1,3})\1\2", "abbabb")
print(match.groups())

matches = ["house mouse", "blue true", "bake brake", "mock sock"]
no_match = ["hippo horse", "dog cat", "home castle", "legend hero"]

regex = r'(.+?)(..+) (.+)\2'

for i in matches:
    print(re.match(regex, i)[2])
for i in no_match:
    if re.match(regex, i):
        print("{}! It's a match!".format(i))

import re

print(re.search('a.*a', 'abbabba')[0])
print(re.search('a.*?a', 'abbabba')[0])
print(re.search('a.*?a$', 'abbabba')[0])

import binary # file from last slide

for b in ["0b01010", "01b110", "0b110", "0b", "0b010b", "0bb100", "0b1", "1b001"]:
    print('{} : {}'.format(b, binary.fsa(b)))


print("{1}{0}".format("a", "b")) #-> 'ba'
print("Candidate {0}: {name}, {age}".format(1, age=23, name='Fred')) #-> 'Candidate 1: Fred,23'



age = 23
# print("My age is " + age + "!")

print("My age is " + str(age) + "!")

print("{:_<10s}".format("hi"))
print("{:+4}".format(35))
print("{:10.3f}".format(1/3))

age = 17
print(f"My age is {age:-^6}.")
print(f"I will be {age + 1} next year! So I will be {'not ' if (age + 1) < 18 else ''}allowed to drive!")

print("My age is %6d" % age)

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
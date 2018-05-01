if 5 > 3:
    print("The math checks out!")
    print("You only see this if the math checked out.")

var = "interrupting statement"

    # no block anymore so..
    e = "This is a syntax error"


if apple == orange:
    print("Oh. This is odd.")
    print("Have you tried turning it off and on again?")
# no indentation anymore
else:
    # indent again
    print("Phew. World saved.")

print("Check done.")


if time == action_time:
    if action == menu:
        open_menu()
    elif action == attack:
        attack_closest()
    elif action == secret_action:
        repeatedly_open_cd_tray()
    elif action is None:
        print("Do something!")
    else:
        play_idle_animation()
elif time == tea_time:
    activate(british_mode)
else:
    exit()


if user == "admin":
    print("You passed the really secure check! Hello Admin")
else:
    # this works, but looks worse
    if user == "default":
        print("Hello super special user!")
    else:
        # it’s getting out of hand
        if user is None:
            print("I guess I am alone now")
        else:
          print("An unexpected value!")


if user == "admin":
    print("You passed the really secure check! Hello Admin")
elif user == "default":
    print("Hello super special user!")
elif user is None:
    print("I guess I am alone now")
else:
    print("An unexpected value!")


temp = 32

if temp >= 17:
    msg = "Pleasant"
elif temp >= 27:
    msg = "Warm"
else:
    msg = "Out of range"


temp = 32

if temp >= 27:
    msg = "Warm"
elif temp >= 17:
    msg = "Pleasant"
else:
    msg = "Out of range"


temp = 32

if temp >= 27:
    msg = "Warm"
if temp >= 17:
    msg = "Pleasant"
if temp >= -10:
    msg = "Out of range"


counter = 0
while counter < 10:
    if counter % 2 == 0:
        print(counter, end=', ')
    counter += 1

print(counter) # will print 10


print(' x : x^2')
for x in range(-5,6):
    print(x, ':', x**2)


while True:
    print('°_°', end=' ')


for item in 'Python':
    print(item, end=', ')


for x in "Python":
    if x == "h":
        break
    print(x, end=' ')


counter = 0
while counter < 10:
    if counter >= 5:
        break
    print(counter, end=' ')
    counter += 1
print(counter < 10)


for val in my_list:
    if val == target:
        break


counter = 0
while counter <= 10:
    if counter % 2 == 0:
        continue
    print(counter, end=' ')


counter = 0
while counter < 10:
if counter > 5:
continue
counter += 1
print(counter, end=' ')


def func():
    pass

for i in range(10):
    pass

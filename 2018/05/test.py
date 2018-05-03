import re
match = re.match(r"(.*) ((a+)(b+))", "1234 aaabbb")
print(match.groups())


# import binary  # file from last slide

# for b in ["0b01010", "01b110", "0b110", "0b", "0b010b", "0bb100", "0b1", "1b001"]:
#     print('{} : {}'.format(b, binary.fsa(b)))

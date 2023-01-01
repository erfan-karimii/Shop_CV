import re
x = '009809024485880'

print(bool(re.compile("^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$").match(x)))
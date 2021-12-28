
a = "1" + 2 * "3" + "1"
# (output) 1331
print(a)

b = 1 + "2" * 3 + "1"
# TypeError: can't multiply sequence by non-int of type 'str'
# (correct answer) b = 1 + int("2") * 3 + int("1")
# (correct output) 8
print(b)

c = 1 + 2 * 3 / 3 + 1
# (output) 4.0
print(c)

d = "1" + "2" * "3" + "1"
# TypeError: can't multiply sequence by non-int of type 'str'
# (correct answer) d = "1" + "2" * int("3") + "1"
# (correct output) 12221
print(d)

e = 1 + False/True
# (output) 1.0
print(e)

f = 1 + True/False
#zero division error, True is 1 and False is 0
print(f)

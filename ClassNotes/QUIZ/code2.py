# d = {"a": 1, "b":2, "c":3}
# b = {"namne": "alice", "age": 20, "major": "physics"}
# print(len(d))

import re 
def f2(st1, ch1, ch2):
    st2 = ch1 + '.*' + ch2
    return(re.findall(st2, st1))

mys = "This will implement a regular expression search."
print(f2(mys,'p','l'))
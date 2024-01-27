from types import ClassMethodDescriptorType


a = ""
b = ()
c = []
d = {}
e = (1)
f = (1,)
g = [1]
h = {1}
i = {"one":1}
typea, typeb, typec, typed, typee, typef, typeg, typeh, typei = type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i)
types = "a = {}, b = {}, c = {}, d = {}, e = {}, f = {}, g = {}, h = {}, i = {}"
print(types.format(typea, typeb, typec, typed, typee, typef, typeg, typeh, typei))
a={}
print(type(a))

b={2:'xy',25:"rajesh",'star':5}
print(b)
# now we want to access the value then we want to acess the key 

c={2:'xy',25:"rajesh",'star':5}
print(c[25])

# methods In dictionary
"""
get 
update
values 
keys
items
"""
d={2:'xy',25:"rajesh",'star':5}
print(d.get(2))# get method 

e={2:'xy',25:"rajesh",'star':5}
print(e.values())# values method 

f={2:'xy',25:"rajesh",'star':5}
print(f.keys())# keys method 

g={2:'xy',25:"rajesh",'star':5}
print(g.items()) # Items Method

m={2:'xy',25:"rajesh",'star':5}
print(m.update({4:6}))
print(m)# update method

# using the for loop 

for i in {2:'xy',25:"rajesh",'star':5}: # in output only keys are display
  print(i)

# we want values 
for i in {2:'xy',25:"rajesh",'star':5}.values(): # in output only values are display
  print(i)
# we want items 
for i in {2:'xy',25:"rajesh",'star':5}.items(): # in output only items are display
  print(i) 
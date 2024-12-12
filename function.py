#string-------------------------------------------------------------------------------------------
s = "hi world"

# print(s.capitalize())#only 1st char in a string
# print(s.casefold())# = s.lower()
# print(s.lower())#u -> l
# print(s.upper())#l -> u
# print(s.islower())#must all char in lower
# print(s.isupper())#must all char in upper
# print(s.swapcase())#l -> u & u -> l

# print(s.isalnum())#must be 'a'&12 without space
# print(s.isalpha())#without space
# print(s.isdecimal())#0 - 9 = isdigit() = isnumeric()
# print(s.isdigit())#0 - 9
# print(s.isnumeric())# 0 - 9
# print(s.isspace())#only space ex- 'a b' -> f / ' ' -> t
# print(s.isascii())#ascii value possible or not ex- "🤔🤔" -> false

# print(s.replace('a','-'))#1st <- 2nd
# print(s.count("a"))#must be str
# print(s.index("l"))#return index if (char repitation >2) then return 1st one index
# print(s.rindex("l"))#from right
# print(s.find("hi"))#return index from left ex- "hi hi" -> 0
# print(s.rfind("hi"))#from right ex- "hi hi" -> 3
# print(s.split(" "))#return list
# print(s.partition("l"))
# print(s.rpartition("l"))

# print(s.splitlines())#if s have \n then split it
# print(s.expandtabs())#if s have \t then replace it
# print(s.format("biki",8,...))# = f'string s have {},{}
# print(s.format_map({'name':'john','roll':23}))# = f'string s have {name},{roll} | 
# print(s.maketrans('hw','JX'))#dict table from their ascii ex- 'AB','ab'[65:91,66:92]
# print(s.translate(s.maketrans('hw','jk')))#replace according to maketrans

# print(s.isprintable())#if s have \n,\t,\0 then false
# print(s.isidentifier())#identifier -> not space,no special char,.....
# print(s.istitle())#Bik Sam-> true / Bik sam -> false
# print(s.title())#bik sam is good -> Bik Sam Is Good
# print(s.startswith())#only check 1st char
# print(s.endswith("h"))#true/false

# print(s.zfill(2))#s len == 2 if not fill with 0 [pre-s]
# print(s.center(5,"*"))#s len == 5 if not fill with '*' [pre-s-post]
# print(s.ljust(10,"*"))# = center() [fil from left[string]] untill s len == 10
# print(s.rjust(10,"*"))# = center() [fill from right[string]] untill s len == 10

# print(s.encode())#b' s '
# print(s.strip())#remove space from both
# print(s.lstrip())#remove space from left[user]
# print(s.rstrip())#remove space from right[user]
# print(" ".join(list))#return string


#list-------------------------------------------------------------------------------------------------------------
l = []

# l.append(4)#single add
# print(l.extend([1,2,3]))#bulk add

# l.clear()#all remove
# print(l.pop(index))#remove by index
# print(l.remove(element))#remove by value

# l1 = l.copy()#same copy
# print(l.count(element))#same as string
# print(l.index(element))#return index
# print(l.insert(index, element))#insert at index
# l2 = l.reverse()#only reverse
# l3 = l.sort(reverse=True)#reverse/......




#Dictionary-----------------------------------------------------------------------------------------------------
d = {1:'a',2:'b',3:'c'}

# d.update(5,'e')#add key-value
# d1 = d.clear()#remove all
# print(d.pop(1))#remove key-value
# print(d.popitem())#remove last key-value
# d2 = d.copy()#copy

#                                                            print(d.fromkeys(6:'q'))

# print(d.items())#list , tuple form
# print(d.keys())#all keys
# print(d.values())#show all values

# print(d.setdefault(4,'d'))#show key value if key not present insert value
# print(d.get(1))#get key value


#tuple----------------------------------------------------------------------------------------------------------
t = (1,2,3,4,5)

# print(t.count(2))#count
# print(t.index(2))#index


#set------------------------------------------------------------------------------------------------------------
s = {2,3,4,5}

# s.add()#add
# s.update()#add
# s.clear()#all remove
# s.discard(3)#remove specific item
# s.remove(5)#remove specific item
# s.pop()#remove only 1st one
# s.copy()#copy

#                                                           s.difference()

#                                                                   s.difference_update()

#                                                                s.intersection()

#                                                           s.intersection_update()

#                                                               s.isdisjoint()

#                                                                       s.issubset()

#                                                               s.issuperset()

#                                                                s.symmetric_difference()

#                                                               s.symmetric_difference_update()

#                                                                   s.union()

#Negative indexing

s='hello world'
print(s[-3])# print reverse of word

#Slicing
print(s[0:6:2]) #here starting value is starting point and mid value is ending point of given String and last value is number of increament

#Reverse Slicing
print(s[6:0:-1]) #one point be mevtion that if we use negative indexing then starting value should be greater than mid value

#reverse string in one line of code
print(s[::-1])

#editing and deleting given dtring
# Note:- Python String are emmutable

s='Ankit Kumar Sharma'
#del s # it behave like delete but it cant delet string
#print(s) 

#del s[-1:-5:-2] throw error
print(s)

#arithmatic operator in string : [+,*]
print("Like"+" "+"Mom")
print("Like Mom"*10) #print 10 Time of like mom in same line

#Relational operator in String
#All relational operator will work here
print("Ankit">"Kumar")# using laxography for cheak that 
print("Kumar"<"kumar")

#one most thing is that empty String if false and it have one char then true

#function in String
#Common function
# 1. len
# 2. min
# 3. max
# 4. sorted return sorted list
# 4. sorted("name",revers=true) return sorted list in decreasing order

p="my name"
#captalyze function
print(p.capitalize())#conver first leter of word is capital

# title function
print(p.title()) # convert capital letter of first word of first letter

#upper function
print(p.upper()) # convert all letter in upper case

#lower function
print(p.lower()) # convert all letter in lower case

#swapcase()
print(p.swapcase()) # convert upper to lower and lower to upper

#index():- retuer position of sub string if not present then throw error
#finde():- retuer position of sub string if not present then return -1
#count():- count char who have present in given string
#endswith():- cheak that string is end with given substring
#startswith():- cheak that string is start with given substring

name='Ankit k Sharma'
gender='Male'

print('Hi My Name is {}, My gender is {}'.format(name,gender))

# isalnum,isalpha,isdigit,isidentifier
print('iamankit123'.isalnum())
print('32423'.isdigit())
print('firs-name'.isidentifier())
print('firs_name'.isidentifier())

# split means todna and join means jodna
# split() break on space
# split(i) break on i
# join()
print('i am ankit Kumar Sharma'.split())
print('my name is ankit Kumar sharma'.split('is'))

print(" ".join(['i', 'am', 'ankit', 'Kumar', 'Sharma']))

# replace and strip
# rplace besicaly replace given word at the place of existing word
# strip besicaly remoove all space after the last char

print('i am ankit kumar sharma'.replace('ankit','gaytri'))
print('i am ankit kumar sharma                    '.strip())

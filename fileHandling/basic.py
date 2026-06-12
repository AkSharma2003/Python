# there are Two types of File
#     1. Text File :-  All programable file are called text file
#     2. Binary file :- Image, Vidio, Music, exe are called binary file
    
    
# How file I/O is done in most programing language
#     -> Open a File
#     -> Read/Write Data
#     -> Close the file
    

# case 1:
# if the file is not present
f=open('sample.txt','w') 
f.write('Hello world')
f.close()

# write multiple line string
f=open('sample1.txt','w')
f.write('hello world')
f.write('\nhow are you')
f.close()


# case 2: 
# file is allready present
f=open('sample.txt','w')
f.write('Miss Pai') # replace all line with this line
f.close()

# apend contant
f=open('sample1.txt','a')
f.write('\nI am fine',)
f.close()

# write Lines
L=['hello','\nhi','\nI am ankit kumar sharma']
f=open('sample.txt','w')
f.writelines(L)
f.close()

# why use f.close() : 1st is memory and second is sefty


# reading from file
f=open('sample.txt','r')
print(f.read())
f.close()

# Reading up to n charehtor
f=open('sample1.txt','r')
print(f.read(10)) # here pass 10 so read only first 10 char
f.close()

# print line by line using readline()
f=open('sample.txt','r')
print(f.readline()) # print first line
f.close()
 
 
# reading entire file using readline
print("using read file using readline ")
f=open('sample.txt','r')
while True:
    data=f.readline()
    if data=="":
        break
    else:
        print(data,end='')
    
f.close()

# using context maneger with
    # with aouto close the File
with open('sample1.txt','w') as f:
    f.write('Ankit Kumar Sharma')
    
    
# read file using with
with open('sample1.txt','r') as f:
    print(f.read())
    
    
# moving within a file 10 cahr then 10 char
with open('sample.txt','r') as f:
    print(f.read(10))
    print(f.read(10))


# how to load big file in ram
# write 1000 time hello world
big_l= ['hello world'for i in range(10000)]
with open('big.txt','w') as a:
    a.writelines(big_l)
    
# read file
with open('big.txt','r') as f:
    chunk_size=10
    while len(f.read(chunk_size))>0:
        print(f.read(chunk_size),end='**')
        f.read(chunk_size)
    
# f.tell() give current location of curseor
# t.seek(n) move cursor to n position acording to n


# seek during write

with open('sample.txt','w') as f:
    f.write('Hello')
    f.seek(0)
    f.write('Xa') #Hello then Xallo
    
    # problwms with working in text moode
        # can't work with binary file like image
        # not good for other data like int/float/list/touple
        
 
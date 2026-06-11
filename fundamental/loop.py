# #while loop
# i=1
# while i<11:
#     print(2*i)
#     i+=1

# # while loop with else conitio 
# # else condition generaly use with if condition but here is deferent condition 
# print()
# j=1
# while j<=3:
#     print(j*10)
#     j+=1
# else:
#     print("Limit is crossed")

#for Loop

for i in range(1,11): # 1 is include but 11 is exclude here is third number is hide it is itrator
    print(i,end=" ")
print()

for i in range(10,0,-1): # -1 is third itrator who step of jumping number
    print(i,end=" ")

# nested loop
#print uniq pair

for i in range(1,5):
    for j in range(1,5):
        print(i,j)
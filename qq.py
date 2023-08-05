s="my name is chiku"
# count=0
# for x in s:
#     if x=="i":
#         count+=1
#         if count==2:
#             x="n"
#
#     print(x,end="")
d=s.split()
for i in d:
    print(i[::-1],end=" ")
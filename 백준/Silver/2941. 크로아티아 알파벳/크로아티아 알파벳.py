cro_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]
k = input()

for word in cro_list:
    k= k.replace(word ,"1")

print(len(k))
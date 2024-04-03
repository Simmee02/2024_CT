score_dict = {"A+":4.5,"A0":4.0,"B+":3.5,
         "B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,
         "D0": 1.0,"F":0.0}
total_score = 0
temp = 0

for i in range(20):
    s= input().split(" ")
    if s[2] == "P":
        continue
    else:
        temp = temp + float(s[1])
        total_score = total_score + float(s[1]) * score_dict[s[2]]

if temp > 0:
    print(total_score/temp)
else:
    print("0")
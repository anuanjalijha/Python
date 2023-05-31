n = int(input())
res = []
grade = []
for i in range(n):
    name = input()
    score = float(input())
    res.append([name,score])
    grade.append(score)
grade = sorted(set(grade)) 
m = grade[1]
name = [] 
for val in res:
    if m==val[1]:
        name.append(val[0])
name.sort()
for nm in name:
    print(nm)          
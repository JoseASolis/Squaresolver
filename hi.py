print("Inserte nombre del archivo")
a = input() + '.txt'
f =open(a,'r')
r = f.read().split(' ')
n = int(r[0])
nd = r[1:]
goal = n * (n * n + 1) / 2;
print("dimensiones :",n)
print("goal",goal)
nd.reverse()
m = [[nd.pop() for i in range(n)] for j in range(n)]
print ("Cubo: ")
for i in range(n):
    print(m[i],'\n')
min_sum,max_sum= 0,0
minn = 1
maxx = n * n
for i in range (n):
    min_sum += minn
    minn += 1
    max_sum += maxx
    maxx += 1
min_b,max_b = abs(goal - min_sum), abs(goal - max_sum)
if min_sum < max_sum:
     final_b = max_sum
else:
    final_b = min_sum
total_cases = 2 * n + 2
bias = total_cases * final_b
fitness = bias
print ("Max score: ",fitness)
for i in range(n):
    s =0
    for j in range(n):
        s +=int(m[i][j])
    fitness -= abs(goal-s)
for j in range(n):
    s=0
    for i in range(n):
        s += int(m[i][j])
    fitness -= abs(goal-s)
s = 0
for i in range(n):
    s+= int(m[i][i])
fitness -= abs(goal-s)
m.reverse()
s = 0
for i in range(n):
    s+= int(m[i][i])
fitness -= abs(goal-s)

print("Actual score: ",fitness)

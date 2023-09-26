"""
Python lists
lista=["egy",777,False,(12,1)]
print(lista[-1])
print(lista[-2])
x=[21,4,"Val",3.2]
for i in x:
    print(i)

for i in range(0,4):
    print(x[i])
"""
nul = []
#egységmátrix:
for i in range(0, 5):
  y = []
  for j in range(0, 5):
    if i == j:
      y.append(1)
    else:
      y.append(0)
  nul.append(y)
#print(nul)

for i in range(0, 5):
  for j in range(0, 5):
    print(nul[i][j], end=' ')
  print()

nul = []

for i in range(0, 5):
  y = []
  for j in range(0, 5):
    y.append(0)
  nul.append(y)
#print(nul)

for i in range(0, 5):
  for j in range(0, 5):
    print(nul[i][j], end=' ')
  print()



x=[1,0,32,4,'0']
if '0' in x:
    print("igen")
else:
    print("nem")
x[4]="go"
x.clear() #lista törlése
for i in range(1,11): #1-10
    if(i%2==0):
        x.append(i)
        print(i)

h=[z for z in range(1,11)] #tömb feltöltése
print(h)

ps=[z for z in range(1,11) if z%2 ==0]
print(ps)
new=[321,1,54,6,23,14,0]
new.sort()
print(new)





















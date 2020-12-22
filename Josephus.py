import matplotlib.pyplot as plt
import math

People = [] 

while True:
  n = input("Enter the Number of People(>1) : ")
  if n.isdigit() and int(n)>1:
    n = int(n)
    break
  else:
    print("Please Enter a Natural Number!")

for i in range(0, n): 
  People.append(i+1)
print(People)

x = []
y = []
alpha = 2 * math.pi / n
plt.axis("equal")

for k in range(0, n):
  x_point = n * math.cos(k*alpha)
  y_point = n * math.sin(k*alpha)
  plt.annotate("Person {}".format(k+1), (x_point, y_point))
  x.append(n * math.cos(k*alpha))
  y.append(n * math.sin(k*alpha))

plt.scatter(x, y, label= "stars", color= "green",  marker= "+", s=30) 
plt.show(block=False)

print("Press Enter for Further Steps!")

def josephus(ls):
  skip = 2
  skip -= 1
  idx = skip
  while len(ls) > 1:
    if input() == "" :
      print("Person {} Killed!".format(ls.pop(idx)))
      idx = (idx + skip) % len(ls)


      plt.clf()
      alpha = 2 * math.pi / n
      plt.axis("equal")

      for k in range(0, n):
        if k+1 in ls:

          x_point = n * math.cos(k*alpha)
          y_point = n * math.sin(k*alpha)
          plt.annotate("Person {}".format(k+1), (x_point, y_point))
          x.append(n * math.cos(k*alpha))
          y.append(n * math.sin(k*alpha))
        else:
          continue
      
      plt.scatter(x, y, label= "stars", color= "green",  marker= "+", s=30) 
      plt.show(block=False)



    else:
        print("Please Press Enter!")
  
  print("The Survivor is Person {}!".format(ls[0]))
  plt.show()
print(josephus(People))
eps=1e-6
class Candy:
  def __init__(self,v=0,w=0):
    self.v=v
    self.w=w
    
  def __lt__(self,other):
    return (self.v/self.w-other.v/other.w)>eps
n,w=list(map(int,input().split())
candies=[Candy() for i in range(n)]
for i in range(n):
  candies[i].v,candies[i].w=list(map(float,input().split()))
candies.sort()
totalW=0
totalV=0
for i in range(n):
  if (totalW + candies[i].w)<=w:
    totalW += candies[i].w
    totalV += cnadies[i].v
  else:
    totalV+= candies[i].v*float(w-totalW)/candies[i].w
    break
print('%.1f'%totalV)
         

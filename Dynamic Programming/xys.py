#%%
test = ["X", "X", "Y", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "Y", "Y", "Y", "X", "Y", "Y", "Y", "X", "Y", "Y", "Y"]
#%%
def minStep(str) -> int:
    xis = []
    yis = []
    for i, l in enumerate(str):
        if l == 'X':
            xis.append(i)
        else:
            yis.append(i)
    print(xis)
    print(yis)
    if len(xis)==0 or len(yis)==0:
        return 0
    if xis[-1] < yis[0]:
        return 0
    if yis[-1] < xis[0]:
        return min(len(xis), len(yis))
    
    p, q = 0, 0
    cty = 0
    ctx = 0
    while p < len(xis) and q < len(yis):
        minX, minY = xis[p], yis[q]
        if minX < minY:
            ctx += 1
            p += 1
        else:
            cty += 1
            q += 1
    if p < len(xis):
        return cty
    return min(ctx, cty)
# %%
def minStep(str) -> int:
      charX = 'X';
      numY = 0;
      minDel = 0;
      for i in range(0, len(str)):
          if (charX == str[i]):
              minDel = min(numY, minDel + 1);
          else:
              numY = numY + 1;
          print(i, minDel, numY)
      return minDel;
# %%
# particles = [1,3,5,7,9]
particles = [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]

diff = [particles[i] - particles[i-1] for i in range(1, len(particles))]
tot = 0
i = 1
count = 1
while i < len(diff):
    if diff[i-1] == diff[i]:
        count += 1
    else:
        tot += (count * (count - 1)) / 2
        count = 1
    i += 1
tot += (count * (count - 1)) / 2
print(tot)
# %%
def particleVelocity(particles):
    numStable = 0
    for i in range(len(particles)-2):
        for j in range(i+1, len(particles)-1):
            if particles[i+1] - particles[i] == particles[j+1] - particles[j]:
                numStable += 1
            else:
                break
    return numStable

particleVelocity(particles)

# %%

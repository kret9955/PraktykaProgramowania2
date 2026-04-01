import numpy as np
import time

pole = np.random.randint(0, 2, (20,20), int)

def next_step(pole):
    pole1 = np.zeros((20, 20), int)
    for x in range(20):
        for y in range(20):
            lives = check(pole, x, y)
            if lives == 3:
                pole1[x][y] = 1
            elif (lives == 2 or lives == 3) and pole[x][y] == 1:
                pole1[x][y] = 1
            elif (lives < 2 or lives > 3) and pole[x][y] == 1:
                pole1[x][y] = 0
    print(pole1)
    print("\n")
    return pole1

##def swap_signs(pole):
  ##      for x in range(pole.shape[0]):
      ##      for y in range(pole.shape[1]):
      ##          if (pole[x, y] == 1):
        ##            pole[x, y] = 'o'
          ##      else:
            ##        pole[x, y] = '.'
    ##    print(pole)

def check(pole, x, y):
    #a = [[x-1],[x],[x+1]]
    #b = [[y-1],[y],[y+1]]
    neighbors = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    result = 0
    for i in neighbors:
         if i[0] < 0 or i[0] >= 20 or i[1] < 0 or i[1] >= 20:
            result += 0
         else:
            if pole[i[0]][i[1]] == 1:
                result += 1
    return result

t = True
while t == True:
    pole = next_step(pole)
    time.sleep(1)
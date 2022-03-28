# See projecteuler.net for this combinatorics problem.
import math,time
start = time.time()
answer = 0

for n in range(1,101):
    for k in range(1,n):
        if math.comb(n,k) > 1000000:
            answer += 1

print(answer)

stop = time.time()
print(stop-start, "seconds")
#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

#  1. He can eat 1 cookie at a time 3 times [1] * 3
#  2. He can eat 1 cookie, then 2 cookies [1] + [2]
#  3. He can eat 2 cookies, then 1 cookie [2] + [1]
#  4. He can eat 3 cookies all at once. [3] * 1

# 3 cookies
111
12
21

# 4 cookies
1111
112
13
121
211
22
31

# 5 cookies
11111
1112
1121
1211


def eating_cookies(n, cache=None):
	print(cache)
	if cache is None:
		cache = [0] * (n + 1)
	if n <= 1:
		cache[n] = 1 
	if n == 2:
		cache[n] = 2
	elif cache[n] == 0:
		cache[n] = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
	return cache[n]

print(eating_cookies(4))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
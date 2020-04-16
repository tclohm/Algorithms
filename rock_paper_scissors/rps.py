#!/usr/bin/python

# understand
# inputs?
# range of inputs?
# how big can the input be?
# what are the outputs?
# what is the range of output?
# how big can the output be (how much data)?

# For example, given n = 2, your function should output the following:

# ```python
# [
	# ['rock', 'rock'], 
	# ['rock', 'paper'], 
	# ['rock', 'scissors'], 
	# ['paper', 'rock'], 
	# ['paper', 'paper'], 
	# ['paper', 'scissors'], 
	# ['scissors', 'rock'], 
	# ['scissors', 'paper'], 
	# ['scissors', 'scissors']
 # ]
# ```


import sys

def rock_paper_scissors(n):

	# base case
	# iteration towards the base case
	# call itself, recursively
	states = ['rock', 'paper', 'scissors']
	games = []

	return games


print(rock_paper_scissors(1))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
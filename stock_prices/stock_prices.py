#!/usr/bin/python

# understand: what is the problem asking me?
	# wants to find the max difference (in profit) between the stock price in linear time (left to right)
	# 

 # receive an input a list of stocks
 # return maximum profit that can made from single buy and sell
 # buy first before sell

 # `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530 = 3800 - 270
 # find maximum difference between the smallest and largest prices in the list of prices

import argparse

def find_max_profit(prices):
	# find the biggest gap between the numbers
	difference = -10000000
	for time, price in enumerate(prices):
		for it_time, it_price in enumerate(prices):
			if time - it_time > 0 and difference < price - it_price:
					#print("price:", price, "iteration price:", it_price, "\n\tprice - iteration price =", price-it_price)
				difference = price - it_price
	return difference

print(find_max_profit([1050, 270, 1540, 3800, 2]))
print(find_max_profit([100, 90, 80, 50, 20, 10]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
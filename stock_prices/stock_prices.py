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
	# difference set very low
	max_difference = -1000000000
	lowest_price = prices[0]

	# if our current price is lower than the lowest_price 
	# set it to new lowest price
	for i in range(0, len(prices) - 1):
		price_ahead = prices[i + 1]
		# if the current price is lower than our lowest_price, set it
		if prices[i] < lowest_price:
			lowest_price = prices[i]
		# if the price_ahead - lowest_price is greater than max_difference, set it
		if price_ahead - lowest_price > max_difference:
			max_difference = price_ahead - lowest_price

	return max_difference


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
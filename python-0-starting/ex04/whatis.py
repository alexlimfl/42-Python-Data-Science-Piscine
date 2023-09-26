# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: folim <folim@student.42kl.edu.my>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 22:22:16 by folim             #+#    #+#              #
#    Updated: 2023/09/18 22:22:17 by folim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def count_argv(argv):
	count = 0
	for _ in argv[1:]:
		count += 1
	return count


if count_argv(sys.argv) < 1:
	sys.exit(1)
try:
	if count_argv(sys.argv) > 1:
		raise AssertionError("more than one argument is provided")
except AssertionError as e:
	print(f"AssertionError: {e}")
	sys.exit(1)

try:
	number = int(sys.argv[1])
except ValueError:
	try:
		raise AssertionError("argument is not an integer")
	except AssertionError as e:
		print(f"AssertionError: {e}")
		sys.exit(1)

if number % 2 == 0:
	print("I'm Even.")
elif number % 2 != 0:
	print("I'm Odd.")

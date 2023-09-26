# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: folim <folim@student.42kl.edu.my>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 17:17:31 by folim             #+#    #+#              #
#    Updated: 2023/09/18 17:17:33 by folim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
	if type(object) is list:
		print("List :", type(object))
	if type(object) is tuple:
		print("Tuple :", type(object))
	if type(object) is set:
		print("Set :", type(object))
	if type(object) is dict:
		print("Dict :", type(object))
	if type(object) is str:
		print(object, "is in the kitchen :", type(object))
	if type(object) is int:
		print("Type not found")
	return 42
	
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: folim <folim@student.42kl.edu.my>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 15:07:48 by folim             #+#    #+#              #
#    Updated: 2023/09/18 15:07:52 by folim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"
ft_tuple = ft_tuple[0:1] + ("Malaysia!",)
ft_set.discard("tutu!")
ft_set.add("KL!")
ft_dict["Hello"] = "42KL!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

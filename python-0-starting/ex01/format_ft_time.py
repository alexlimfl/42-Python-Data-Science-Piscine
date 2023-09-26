# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: folim <folim@student.42kl.edu.my>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 16:20:33 by folim             #+#    #+#              #
#    Updated: 2023/09/18 16:20:34 by folim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime

start_date = datetime(1970, 1,1)
end_date = datetime.now()

duration = (end_date - start_date).total_seconds()
formatted_duration = f"{duration:,.4f}"
scientific_duration = f"{duration:.2e}"

print("Seconds since", start_date.strftime("%b %d, %Y")+":", formatted_duration,"or", scientific_duration, "in scientific notation")
print(end_date.strftime("%b %d, %Y"))
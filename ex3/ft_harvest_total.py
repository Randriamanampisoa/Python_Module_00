#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/28 12:37:25 by fanilran            #+#    #+#            #
#   Updated: 2026/04/04 13:16:07 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total():
    total_haverst = 0
    for i in [1, 2, 3]:
        harvest = int(input(f"Day {i} harvest: "))
        total_haverst += harvest
    print(f"Total harvest: {total_haverst}")

#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/28 13:09:36 by fanilran            #+#    #+#            #
#   Updated: 2026/04/02 15:09:49 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative():
    day = int(input("Day until harvest: "))
    for i in range(day):
        print(f"Day {i + 1}")
    print("Harvest time!")

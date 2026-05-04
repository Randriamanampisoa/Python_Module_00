#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/28 13:20:01 by fanilran            #+#    #+#            #
#   Updated: 2026/04/02 15:10:30 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive():
    day = int(input("Days until harveast: "))

    def ft_recursive(i):
        if i > day:
            return
        print(f"Day {i}")
        ft_recursive(i + 1)
    ft_recursive(1)
    print("Harvest time!")

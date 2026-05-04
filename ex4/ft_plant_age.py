#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/28 12:48:47 by fanilran            #+#    #+#            #
#   Updated: 2026/04/02 12:44:08 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plant_age():
    age = int(input("Enter plant age in day: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/28 12:57:19 by fanilran            #+#    #+#            #
#   Updated: 2026/03/28 15:11:02 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder():
    day = int(input("Day since last watering: "))
    if day > 2:
        print("Water the plants!")
    else:
        print("Plant are fine")

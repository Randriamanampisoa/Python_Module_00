#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plot_area.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/28 11:32:33 by fanilran            #+#    #+#            #
#   Updated: 2026/03/28 12:31:08 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    result = length * width
    print(f"Plot area: {result}")

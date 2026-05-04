#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/28 15:13:08 by fanilran            #+#    #+#            #
#   Updated: 2026/04/04 13:34:04 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed} seed: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed} seed: {quantity} grams total")
    elif unit == "area":
        print(f"{seed} seed: covers {quantity} square meters")
    else:
        print("Unknown unit type")

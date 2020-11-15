#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Przedmiot: Informatyka
# Kierunek studiów: Inżynieria Transportu
# Semestr: zimowy
# Rok akademicki: 2020/2021
# Data (dzień.miesiąc.rok): 25.10.2020
# Imię: Brajan
# Nazwisko: Kampioni
# Numer albumu ZUT: 50410

"""
Suma szeregu
Napisz program, który dla podanego całkowietego dodatniego N<1000000 oblicza
sume szeregu s=a1+a2+...+aN gdzie aK=(1+1/k)/k^3+1)
"""

n = int(input("Podaj ilość wyrazów, nie więcej niż 1000000: "))
sum1 = 0
for i in range(1, n + 1):
      
      # TODO: zastąpić 1 / i tym co naprawdę ma być liczone
      # 
      sum1 = sum1 + (1 / i) 

# TODO: albo anglielski - albo polski - jeżeli chodzi o język naturalny
#
print("The sum of series is", round(sum1,2))

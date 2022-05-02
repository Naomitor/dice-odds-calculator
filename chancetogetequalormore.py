# Calculates the chance to get any given value out of a die
import getnumbers

diceamount, diceeyes, minimum = getnumbers.getnumberswithminimum()


result = (1 / diceeyes * diceamount)*100

print(format(result, '.2f'))

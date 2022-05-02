# Calculates the chance to get any one value out of a die
import getnumbers

diceamount, diceeyes = getnumbers.getnumbers()

result = (1 / diceeyes * diceamount)*100

print(format(result, '.2f'))

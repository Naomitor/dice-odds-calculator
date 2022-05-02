# dice-odds-calculator
A training program that calculates the odds of any dice set thrown.

Todo:
- Overarching file that combines all the little codes and combines them to executable.
- Get the dicemaker to output a list of any given dice
    - After that expand on that to get all possibilities from one die, into a list for other features.
    - Rework meanthrow.py to accommodate the new lists 
- Have a graphical interface for easier navigation
    - Implement graphs to visualize the possibilities better

Finished:
- Can calculate the mean throw on all dice starting with the number one to given input
- Can intake multiple dice at once
- Can intake multiple dice sets at once
- Can calculate the chance to get any one value on any dice
- Can calculate the chance to get equal or more than one value on any dice

Description of the different files:

In getnumbers.py I tested different versions of taking in the dice sets from the user.
Right now I settled on the last one "differentdiceallatoncemultiple" ("" Quotation marks in this text are only for showing the exact input in the console or code), where the user puts in the dice sets like this: "2d6".
Where 2 is the number of dice thrown and 6 is the highest value on the dice.
The "d" is the marker for the code to detect where one ends and the next begins, so "11562d20000" would also be valid.
When the user wants to calculate multiple different dice for example a die with 8 sides and another one with 12 they can input them like this: "1d8 1d12".
The program can detect the space between the sets and calculates the next one accordingly.
I also coded a few error and exception handlers for wrong input.
Also in this file is the exit code.
Right now it can only handle dice with values starting at 1 and then increasing by one each step to the input given.
So even a die with one side that has a 1 would be possible but not a die that would contain on side that has the value 2.
A standard six sided die with the values 1,2,3,4,5,6 would be a valid input written as 1d6.

How it works: The input from the user is saved in one string which gets first searched for the string "end" if it is equal the program ends.
If not it searches for a "d" and any number if either are given it continues else it prints an error.
If it continues it starts a loop for the number of "d" in the string.
In that loop it now searches for the first "d" from the left, saves it, copies the string from position 0 to the first "d" as integer into the diceamount var, removes this part including the "d".
Then searches for the next space and stores it to copy the range from the new position 0 to the space as diceeyes var, after that it removes this string including the space.
It appends the diceamount and diceeys to the dicelist which will contain all the values at the end.
The format as example for "2d8" being [2,8] and any new dice sets being appended to that.
If no space is found it just copies from string position 0 to the end expecting the string end and no more sets after this being given.
Thus ending with appending the last diceamount and diceeyes to the dicelist which is returned to the calling process.

The meanthrow.py was the first idea I wanted to make, so right now it is the only bigger functioning part besides the getnumbers.py.
It can calculate the mean throw of any set of dice given by using this formula: Average = ((Max Die Roll + 1)/2) * Number of Same-sided Dice.
It starts with an instructions text after which it calls getnumbers.differentdiceallatoncemultiple function.
If no values are returned from the function it restarts.
Should there be values in the list returned it resets the variables and starts a loop over half the length of the list.
Because the dicelist is formatted as containing the dice amount thrown on the even positions and the highest dice eyes on the uneven positions.
It then calculates the formula and adds it to result repeating for all sets.
For the readability and user output it also appends the "resulttext" with the dice amount a "d" and the dice eyes  following with a ", " to space the different sets.
If the loop is done it removes the last ", " and prints the resulttext and the result containing the mean throw.
After which it repeats the whole loop to get the next sets as user input or get the exit code.

The chancetogetequal.py contains a little snippet that just calculates the chance to throw any one value on a die.

The chancetogetequalormore.py also contains just a little snippet that calculates the chance to throw any given value and more.
So one could say I need a 4 or more on a standard 6 sided die to achieve my goal, how high is the chance?

The other files hold mostly test codes and little snippets for the next feature.
That is the dicemaker.py, it should be able to take any dice into the equation, so that a user can create a die with 8 sides that contains the values 1,1,2,2,3,4,5,6,7,8.
For that to work I also need to rework the meanthrow.py later, so that it will calculate these dice correctly.
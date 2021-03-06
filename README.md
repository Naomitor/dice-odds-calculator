# dice-odds-calculator
A program that can calculate the odds and result of any dice set thrown.

Description of the different files:

In getnumbers.py I tested different versions of taking in the dice sets from the user.
I left the old versions for repurposing in other code.
Right now I settled on the last one "differentdiceallatoncemultiple" for meanthrow.py (" " Quotation marks in this text are only for showing the exact input in the console or code).
The user can put the dice in like this "2d6" where 2 is the number of dice thrown and 6 is the highest value on the dice.
The "d" is the marker for the code to detect where one ends and the next begins, so "11562d20000" would also be valid.
When the user wants to calculate multiple different dice for example a die with 8 sides and another one with 12 they can input them like this: "1d8 1d12".
The program can detect the space between the sets and calculates the next one accordingly.
I also coded a few error and exception handlers for wrong input.
Also in this file is the exit code.
Right now it can only handle dice with values starting at 1 and then increasing by one each step to the input given.
So even a die with one side that has a 1 would be possible but not a die that would contain one side that has the value 2.
A standard six sided die with the values 1,2,3,4,5,6 would be a valid input written as 1d6.

How it works: The input from the user is saved in one string which gets first searched for the string "end" if it is equal the program ends.
If not it searches for a "d" if it is given it continues else it prints an error.
If it continues it starts a loop for the number of "d" in the string.
In that loop it now searches for the first "d" from the left, saves it, copies the string from position 0 in the string to the first "d" as integer into the diceamount var, removes this part including the "d".
Then searches for the next space and stores it to copy the range from the new position 0 to the space as diceeyes var, after that it removes this string including the space.
It appends the "diceamount" and "diceeys" to the "dicelist" which will contain all the values at the end.
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

In dicemaker.py I created a little tool so that the program can get all possibilities of a throw into one list for future graphs.

The chancetogetequal.py contains a little snippet that just calculates the chance to throw any one value on a die.

The chancetogetequalormore.py also contains just a little snippet that calculates the chance to throw any given value and more.
So one could say I need a 4 or more on a standard 6 sided die to achieve my goal, how high is the chance?

The end goals for this program are:
- Have a graphical output to simplify user experience
- Have user defined dice work like a 6 sided die with the numbers 3,3,4,5,6,6
- Have simple number addition for example, 2d6 +10 should give the result of the throw +10 as result
- Have all the code snippets work with the first 3 points these should include but are not limited to:
  - Can calculate the mean throw
  - Can calculate the chance to get any one throw
  - Can calculate the chance to get specific throw and/or all above or below
- Optimize with multiprocessing or better maths
# Coffee Machine https://hyperskill.org/projects/68

## Stage 1
The first version of the program just makes you a coffee. It should print to the standard output what it is doing as it makes the drink

## Stage 2
Let's break the task into several steps:

* First, read the numbers of coffee drinks from the input.
* Figure out how much of each ingredient the machine will need. Note that one cup of coffee made on this coffee machine contains 200 ml of water, 50 ml of milk, and 15 g of coffee beans.
* Output the required ingredient amounts back to the user.

## Stage 3
Write a program that does the following:

* It requests the amounts of water, milk, and coffee beans available at the moment, and then asks for the number of cups a user needs.
* If the coffee machine has enough supplies to make the specified amount of coffee, the program should print "Yes, I can make that amount of coffee".
* If the coffee machine can make more than that, the program should output "Yes, I can make that amount of coffee (and even N more than that)", where N is the number of additional cups of coffee that the coffee machine can make.
* If the amount of given resources is not enough to make the specified amount of coffee, the program should output "No, I can make only N cups of coffee* ".

## Stage 4
Your program should print the coffee machine's state, process one query from the user, as well as print the coffee machine's state after that. Try to use functions for implementing every action that the coffee machine can do.

## Stage 5
Write a program that will work endlessly to make coffee for all interested persons until the shutdown signal is given. Introduce two new options: "remaining" and "exit".

Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, the program should output a message that says it can't make a cup of coffee.

And the last improvement to the program at this step — if the user types "buy" to buy a cup of coffee and then changes his mind, they should be able to type "back" to return into the main cycle.

## Stage 6
Your final task is to refactor the program. Make it so that you can communicate with the coffee machine through a single method. Good luck!
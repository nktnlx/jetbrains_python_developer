This is the 7th project completed by me from [JetBrains Python Developer track.](https://hyperskill.org/tracks/2)

rock_paper_scissors -- a playable Rock-Paper-Scissors game, with a Player vs Computer mode. Practiced use of arrays, the Random library, formatted strings, and algorithms.  
It has also an extended version of the game. Before the start of the game, the user will be able to choose the options that will be used. After entering his/her name, the user should provide a list of options separated by a comma.  
For example: *rock,paper,scissors,lizard,spock*. The general rule is that words to the right of your word are beating your word and words to the left from it are defeated by it. For example, *rock and paper* are beaten by *scissors* and *scissors* are defeated by *lizard and spock*. The list of options can have as much items as user will provide as long as they are comma separated.  
If the user inputs an empty line, your program should start the game with default options: rock. paper and scissors.     

An example of the script execution:  
```
Enter your name: Tim 
Hello, Tim

rock,paper,scissors,lizard,spock
Okay, let's start

scissors
There is a draw (scissors)

lizard
Sorry, but the computer chose spock

spock
There is a draw (spock)

rock
Sorry, but the computer chose paper

rock
Well done. The computer chose lizard and failed

rock
Well done. The computer chose lizard and failed

!rating
Your rating: 650

!exit
Bye!
```


The code was created using Python 3.8  
If your machine has an installed Python 3, you can run the code in terminal(command line):  
$ python3 game.py  


--------------------------------------------
Fill free to contact me via nktn.lx@gmal.com  
Follow me on twitter: @nktn_lx  
And here on github: github.com/nktnlx  
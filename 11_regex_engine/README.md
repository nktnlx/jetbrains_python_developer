This is the 11th project completed by me from [JetBrains Python Developer track.](https://hyperskill.org/tracks/2)

Regex Engine -- In this project, you will write an extendable regex engine that can handle basic regex syntax, including literals (a, b, c, etc.), wild-cards (.), and metacharacters (?, +, ^, $). Learned about the regex syntax, practiced working with parsing and slicing, and got more familiar with boolean algebra and recursion.   

An example of the script execution:  
```
Input:    '^app|apple'           Output: True
Input:     'le$|apple'           Output: True
Input:      '^a|apple'           Output: True
Input:      '.$|apple'           Output: True
Input:  'apple$|tasty apple'     Output: True
Input:  '^apple|apple pie'       Output: True
Input: '^apple$|apple'           Output: True
Input: '^apple$|tasty apple'     Output: False
Input: '^apple$|apple pie'       Output: False
Input:    'app$|apple'           Output: False
Input:     '^le|apple'           Output: False

```


The code was created using Python 3.8  
If your machine has an installed Python 3, you can run the code in terminal(command line):  
$ python3 regex.py  


--------------------------------------------
Fill free to contact me via nktn.lx@gmal.com  
Follow me on twitter: @nktn_lx  
And here on github: github.com/nktnlx  
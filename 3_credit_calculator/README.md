This is the third project completed by me from JetBrains Python Developer track: https://hyperskill.org/tracks/2

There are two versions of the script:  
- creditcalc.py -- calculates annuity monthly payments, periods to repay a credit or a credit principal based on the user input through terminal.  

- creditcalc_terminal_args.py -- calculates annuity or differentiate monthly payments, periods to repay a credit, overpayment and a credit principal based on optional arguments provided when running the script.  
Optional arguments:  
  -h, --help            show this help message and exit  
  --type TYPE           type of your payment: annuity or diff  
  --principal PRINCIPAL principal of your credit   
  --periods PERIODS     number of periods  
  --interest INTEREST   interest rate of your credit  
  --payment PAYMENT     your monthly payment  

Example 1. To calculate differentiated payments for a credit principal 1,000,000, 10 month number of periods and 10% interest rate:    
$ python3 creditcalc_terminal_args.py --type=diff --principal=1000000 --periods=10 --interest=10  

Example 2. To find the annuity payment for the 60-month (or 5-year) credit loan with the principal 1,000,000 and a 9.5% interest:  
$ python3 creditcalc_terminal_args.py --type=annuity --principal=1000000 --periods=60 --interest=9.5  

Example 3. To calculate differentiated payments given the principal 500,000, the period of 8 months, and an interest rate of 7.8%:  
$ python3 creditcalc_terminal_args.py --type=diff --principal=500000 --periods=8 --interest=7.8  

Example 4. To calculate the principal for an individual paying 8,722 per month for 120 months (10 years) with an interest rate of 5.6%  
$ python3 creditcalc_terminal_args.py --type=annuity --payment=8722 --periods=120 --interest=5.6  

Example 5. To figure out how much time an individual needs to repay the credit loan with the principal 500,000, the monthly payment of 23,000 at a 7.8% interest rate:    
$ python3 creditcalc_terminal_args.py --type=annuity --principal=500000 --payment=23000 --interest=7.8  


The code was created using Python 3.8  
If your machine has an installed Python 3, you can run the code in terminal(command line) as shown in examples above.  



--------------------------------------------
Fill free to contact me via nktn.lx@gmal.com  
Follow me on twitter: @nktn_lx  
And here on github: github.com/nktnlx  
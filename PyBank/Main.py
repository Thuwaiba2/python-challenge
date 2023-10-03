import os
import csv

#Open file to read and file to output 
csvpath = os.path.join("Resources", "budget_data1.csv")


#set variables
months = 0
total_months = 0
total_profit_losses = 0
prev_profit_losses = 0
changes_profit_loss = 0
changes = 0
greatest_increase = ["",0]
greatest_decrease = ["",0]

#Open the budget data.csv file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_header = next(csv_reader)

    #calculate the totals 

    for row in csv_reader:
        total_months += 1
        total_profit_losses = total_profit_losses+int(row[1])

    #Calculate the changes in profit/losses &  greatest increase and decrease
        if total_months!=1:
            changes_profit_loss = int(row[1]) - prev_profit_losses
            changes += changes_profit_loss
            average_change = changes/(total_months-1)
            average_change = round(average_change,2)
        prev_profit_losses = int(row[1])
        if changes_profit_loss > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = changes_profit_loss      
        if changes_profit_loss < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = changes_profit_loss




        print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: (${greatest_increase})")
print(f"Greatest Decrease in Profits: (${greatest_decrease})")   
            

        
   #Print to Budget analysis file
textoutput = os.path.join("Analysis","budget_analysis.txt")
with open(textoutput, "w") as textfile:
   # Print Financial Analysis
     #Print total months
    textfile.write(f"Total Months:{total_months}\n")   
    textfile.write(f"   \n")
    #Print Total profit/loss
    textfile.write(f"Total:${total_profit_losses}\n")
    textfile.write(f"   \n")
    #Print Average change
    textfile.write(f"Average Change:${average_change}\n")
    textfile.write(f"   \n")
    #Print Greatest increase
    textfile.write(f"Greatest Increase In Profits:${greatest_increase}\n")
    textfile.write(f"   \n")
    #Print Greatest decrease
    textfile.write(f"Greatest Decrease In Profits:${greatest_decrease}\n")
    
   

  




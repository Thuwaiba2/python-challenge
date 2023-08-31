import os
import csv
csvpath = os.path.join("..","Desktop","python-challenge","PyBank","Resources", "budget_data.csv")
total_months=0
with open("budget.data_csv") as csvfile:
     
    csv_header=next('budget_data_csv')
    print(f"CSVHEADER:{csv_header}")
    csv_reader = csv.reader(csvfile, delimiter=",")
    for row in csv_reader:
     total_months:int
     total_profit_losses:int
     prev_profit_losses:int
     total_months= "total_months"+1
     total_profit_losses="total_profit_losses"+int(row["profit_losses"])
     changes_profit_loss=int(row["profit_losses"])-"prev_profit_losses"
     prev_profit_loss=int(row["profit_losses"])
     average_change=total_profit_losses/total_months
     greatest_increase:int
     if changes_profit_loss>greatest_increase[1]:
        Date:float
        greatest_increase[0]= row[Date]
        greatest_decrease:int
    if changes_profit_loss<greatest_decrease[1]:
     greatest_decrease[0]= row[Date]
     



     

     print; total_months:int    
    print (total_months)

    
     




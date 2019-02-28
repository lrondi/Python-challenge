import os
import csv

month=0
date=[]
total_amount=0
total_change=[]
total_change_av=[]
total_change_av_sum=0
max_inc=0
min_inc=0

file_path=os.path.join("..","Resources","budget_data.csv")

with open(file_path,newline='') as budget_csv:
    budget_reader=csv.reader(budget_csv,delimiter=',')
    #remove header
    budget_header=next(budget_reader)

    #calculate total number of months, total amount of prof/loss and make lists of dates and prof/loss
    for line in budget_reader:
        month+=1
        total_amount+=int(line[1])
        total_change.append(int(line[1]))
        date.append(line[0])

#iterate through list of profit/losses to calculate change
for i in range(1,len(total_change)):
    total_change_av.append(total_change[i]-total_change[i-1])

#calculate sum of changes
for i in total_change_av:
    total_change_av_sum+=i

#calculate avg of changes    
total_change_av_value=round(total_change_av_sum/(month-1),2)

#calculate max and min of profit/losses
max_inc=max(total_change_av)
min_inc=min(total_change_av)

#search for dates of max and min
for i in range(1,len(total_change_av)):
    if total_change_av[i]==max_inc:
        max_date=date[i+1]
for i in range(1,len(total_change_av)):
    if total_change_av[i]==min_inc:
        min_date=date[i+1]


print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {month}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${total_change_av_value}")
print(f"Greatest Increase in Profits: {max_date} $({max_inc})")
print(f"Greatest Decrease in Profits: {min_date} $({min_inc})")

#create txt file with results
file=open("financial_anaylisis.txt","w")
file.write("Financial Analysis\n")
file.write("--------------------------\n")
file.write(f"Total Months: {month}\n")
file.write(f"Total: ${total_amount}\n")
file.write(f"Average Change: ${total_change_av_value}\n")
file.write(f"Greatest Increase in Profits: {max_date} $({max_inc})\n")
file.write(f"Greatest Decrease in Profits: {min_date} $({min_inc})\n")
file.close()


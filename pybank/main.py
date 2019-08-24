import os
import csv
#creating a path
bankpath_csv_path = os.path.join("budget_data.csv")
with open(bankpath_csv_path, newline="") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvfile)
    print(f"Header: {csv_header}")
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#Write a function that does:
next
def analysis (hw):
   months= 0
   total = 0
   maxrev = 0
   minrev = 0
   avgchange = 0
   maxmonth = ""
   minmonth = ""
#Create a for loop
   for row in hw:
       month = row[0]
       total += row[1] #net profit
       #month += 1 #total months
       if row[1] > maxrev: #greatest increase
           maxrev = row[1]
           maxmonth = month
       if row[1] < minrev: #greatest decrease
           minrev = row[1]
           minmonth = month
   avgchange=float(total/month)
   return [months,total, maxrev,maxmonth,minrev,minmonth,avgchange]
def print_analysis(bankpath):
  months = str(bankpath[0])
  totalpl=int(bankpath[1])
  avgchange=(average/totalpl)
  print({months})
  print({totalpl})


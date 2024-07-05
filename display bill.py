total = 1000
vat = 0.195
total_amount = total*vat
bill =  "your total is {total}, and your tax is {vat}, total amount is {total_amount} "
print(bill.format(total = 1000 , vat = 0.195 , total_amount = total*vat))
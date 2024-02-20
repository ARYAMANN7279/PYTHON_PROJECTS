bill=float(input("what was the total bill?\n$"))
tip=int(input("how much tax will you pay(in percent) 10%,12% or 15%?\n"))
total=bill +bill*tip/100
print("your total bill is $",total)
n=int(input("how many people are there\n"))
final_amount="{:.2f}".format(total/n) #this will format any value to 2 decimal places,unlike round
print("each person will pay\n$",final_amount)
print("thanks for coming")
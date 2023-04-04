# 1: Print square of all numbers between 1 to 10 except even numbers

odd_numbers = []
for i in range(11):
    if i % 2 == 1:
        odd_numbers.append(i)
        print(i **2)


# 2: Write a program that prints following shape
# *
# **
# ***
# ****
# *****
# ```

for i in range(1,6):
    
    print("*" * i)
print("'''")


# 3: Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]
expense = int(input("Enter your Expenses: "))
month_found = False

for i in range(len(expense_list)):
    if expense_list[i] == expense:
        month_no = i + 1
        print("Expense for Month: ", month_no)
    
if expense not in expense_list:
    print(expense, ": Not Recorded for any month")


# 4: Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

for i in range(1,6):
    print("Completed ",i,  " Kilometers:")
    run = input("Are you Tired? 'yes/no': ").lower
    if run == "yes":
        print("You did not finish the race")
        break
    else:
        print(5- i, "kilometres to go")
        

if i == 5:
    print("CONGRATULATIONS YOU HAVE COMPLETED THE RACE")


# 5: After flipping a coin 10 times you got this result,
# ```
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0

for head in result:
    if head == "heads":
        count += 1
print("There are", count, "heads")
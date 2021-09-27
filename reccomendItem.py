import re
import pandas as pd

'''
This program will let users use the generated rule file from association.py and then
be able to enter a transaction to have items recommended to them

Here is an explanation of how the algorithm works

Given a set S of association rules and a new transaction t made by a customer, which contains a list of items,
if t matches the left-hand side of a rule r in S (meaning t is a superset of the left-hand side of r),
then the items in the right-hand side of r which do not occur in t will be recommended to the customer.
Note that t may match with multiple rules. If the recommended items from different rules overlap,
duplicates should be removed (that is, the set of recommended items should contain unique items).
For example, if there are four rules:

1)    {a, c} → {d, e}
2)    {c} → {b, e, f}
3)    {b, e} → {g, h, j}
4)    {a, b, c} → {e}

If the new transaction t is {a, b, c}, then t matches the left-hand sides of rules 1) 2) and 4).
The final recommended items should be {d, e, f}.
Note that b is not recommended because it is in t and e is recommended only once.
'''

# Take file with rules generated in association.py
df = pd.read_csv("rules.csv")

# Read the input file into a list of lists
rules = []
for index, row in df.iterrows():
    antecedent = list(map(int, re.findall(r'\d+', row['Antecedent'])))
    consequent = list(map(int, re.findall(r'\d+', row['Consequent'])))

    rule = [antecedent, consequent]
    rules.append(rule)

# new transaction
transaction = []

# Input the transaction
print("Format Ex : '2342, 4545, 5435, 244'")
curr = str(input("Enter Transaction : "))

# Parse Transaction
transaction = list(map(int, curr.split(',')))

# Find Items to be recommended to the user
recommendations = []
for rule in rules:
    if set(rule[0]).issubset(transaction):
        for item in rule[1]:
            if item not in transaction and item not in recommendations:
                recommendations.append(item)

# Store the recommended item names instead of id number
recommendation_names = []
df = pd.read_csv("ID2Name.csv")

# Traverse the dictionary file to find the id to item name mapping
for item in recommendations:
    for index, row in df.iterrows():
        if row[0] == item:
            recommendation_names.append(row[1])
            break

#  Print the recommended items for the user
if len(recommendations) > 0:
    print("Based on your transaction we recommend that you purchase these items")
    for i in range(len(recommendation_names)):
        print("id : " + str(recommendations[i]) + ",  item name : " + str(recommendation_names[i]))
else:
    print("No recommendations based on your purchase")

from efficient_apriori import apriori
import pandas as pd


file =open('trans.csv', 'r')

# Read the input file into a list of lists
data_tr = []
for line in file:
    line = line[:-1] # Remove the \n character at the end of the line
    data_tr.append(line.split(','))

# Prompt the user to input support and confidence thresholds
support_threshold = float(input('Input support threshold: '))
confidence_threshold = float(input('Input confidence threshold: '))

print("Generating frequent itemsets and association rules ...")

# Call the apriori function to generate frequent itemsets and strong association rules
freq_itemsets, rules = apriori(data_tr, min_support=support_threshold, min_confidence=confidence_threshold)

# Output the generated frequent itemsets to the standard output
for itemsetlen, itemsets in freq_itemsets.items():
    print('Length-', itemsetlen, 'frequent itemsets:')
    for itemset, support_count in itemsets.items():
        print(itemset, ':', support_count)

# Output the generated association rules to the standard output
print('\nStrong Association Rules:')
results = []
for rule in rules:
    if rule.lift >= 7:
        print(rule)
        results.append([rule.lhs, rule.rhs, rule.confidence, rule.lift, rule.support])

# Output the generated association rules to a csv file
resultsdf = pd.DataFrame(results, columns=['Antecedent', 'Consequent', 'confidence','lift','support'])
resultsdf.to_csv('rules.csv', index=False)
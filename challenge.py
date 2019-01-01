import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
from tabulate import tabulate

'''
This program completes the MAIS Application Coding Challenge given by McGill AI Society. Please refer to 
https://github.com/McGillAISociety/mais-202-coding-challenge for the description of the challenge.
'''

# Read the csv file
with open('data.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    arr = []
    for row in reader:
        if line_count == 0:
            line_count += 1
            continue
        else:
            arr.append([row[16], float(row[5])])    # Typecast interest rate to float
            # Testing code
            # print(f'Purpose is {row[16]:>19s}; '
            #       f'interest rate is {float(row[5]):>5.2f}%.')
            line_count += 1
    print(f'Processed {line_count - 1} loans.\n')   # line_count excludes the first line containing column names

# Compute average interest rate for each purpose
purposes = list(sorted(set(x[0] for x in arr)))     # Store purposes in a list and remove duplicate entries
n = len(purposes)
sum_int_rates = [0 for _ in range(n)]
num_loans = [0 for _ in range(n)]

for i in range(line_count - 1):
    for j in range(n):                      # Loop through the purpose of each line and all purposes
        if arr[i][0] == purposes[j]:        # for matching purposes
            sum_int_rates[j] += arr[i][1]   # update the sum of interest rates for the specific purpose
            num_loans[j] += 1               # and update the number of loans for the specific purpose

avg_int_rates = [sum_int_rates[i] / num_loans[i] for i in range(n)]

# Print out the results in tabular format
results = [[purposes[i], f'{avg_int_rates[i]:6.3f}%'] for i in range(n)]
print(tabulate(results, headers=['Purpose', 'Average Interest Rate'], tablefmt='presto'))

# Plot the bar chart
mpl.rcParams['xtick.labelsize'] = 6         # Make xtick labels smaller to improve readability
plt.bar(purposes, avg_int_rates, width=0.7, color=['b', 'g', 'r', 'c', 'm', 'y', 'b', 'g', 'r', 'c', 'm', 'y'])
plt.title('Comparison of Interest Rates of Loans by Purpose', fontsize=12)
plt.xlabel('Purpose', fontsize=10)
plt.ylabel('Average Interest Rate', fontsize=10)
plt.show()

gene_expression = {'TP53': 12.4, 'EGFR': 15.1, 'BRCA1': 8.2, 'PTEN': 5.3, 'ESR1': 10.7}
print(gene_expression)

gene_expression['MYC'] = 11.6
print(gene_expression)

import matplotlib.pyplot as plt
gene = list(gene_expression.keys())
expression = list(gene_expression.values())
pl = plt.bar(gene, expression, width=0.45, edgecolor='black')
plt.bar_label(pl, label_type = 'edge', fmt = '%.1f')
plt.xlabel('Gene name')
plt.ylabel('Expression value')
plt.yticks(range(0, 17, 2))
plt.title('Genes and Expression Values')
plt.savefig('gene_expression.png', dpi = 300, bbox_inches = 'tight')
plt.show()

interest = input("Select a gene: ")
if interest in gene_expression:
    print(f"The expression value of {interest} is {gene_expression[interest]}.")
else:
    print(f"Error, {interest} is not in the dictionary.")

number = len(gene_expression)
average = sum(expression) / number
print(f"The average gene expresion level is {average:.2f}.")

input("Press enter to exit.")
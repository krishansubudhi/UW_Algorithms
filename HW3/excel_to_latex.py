import pandas as pd
q6 = pd.read_excel('q5_complexities.xls', sheet_name='q6')
q6 = q6.set_index('n')
latex = q6.to_latex(caption = 'Question 6 results',label='table:q6')
print(latex)

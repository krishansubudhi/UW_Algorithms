import pandas as pd
q5 = pd.read_excel('q5_complexities.xls', sheet_name='q5')
q5 = q5.set_index('n')
latex = q5.to_latex(caption = 'Question 5 results',label='table:q5')
print(latex)

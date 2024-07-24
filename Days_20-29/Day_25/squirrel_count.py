

import pandas

data = pandas.read_csv('Squirrel_Census.csv')

fur_color_counts = data['Primary Fur Color'].value_counts().reset_index()
fur_color_counts.columns = ['Primary Fur Color', 'Count']
fur_color_counts.to_csv('fur_color_counts.csv', index=False)

print(fur_color_counts)

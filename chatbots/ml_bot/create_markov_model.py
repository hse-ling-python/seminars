import pandas as pd
import markovify

provs = pd.read_csv('dal_proverbs.csv', sep='\t', encoding='utf-8')

shuffled = provs.sample(frac=1)
train = ' '.join(shuffled.proverb)
m = markovify.Text(train)

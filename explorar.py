import pandas as pd

df = pd.read_csv('extrato_fake.csv', skipinitialspace=True)

print('==== Primeiras linhas ====')
print(df.head())

print('\n==== Total gasto por categoria ====')
print(df.groupby('categoria')['valor'].sum().sort_values(ascending=False))

print(f'\n==== Total do mês: R$ {df['valor'].sum():.2f}')
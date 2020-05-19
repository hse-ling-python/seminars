import pandas as pd
import numpy as np

letters = [let for let in 'abcdefghijklmnopqrstuvwxyz']


def generate_name():
    n1 = np.random.randint(3, 5)
    n2 = np.random.randint(3, 10)
    w1 = ''.join(np.random.choice(letters, n1)).capitalize()
    w2 = ''.join(np.random.choice(letters, n2)).capitalize()
    return f"{w1} {w2}"


def generate_df():
    K = 2500
    df = pd.DataFrame({
        'name': [generate_name() for _ in range(K)],
        'test_0': [np.round(100 * i / K + np.random.randint(-5, 5)) for i in range(K)],
        'test_1': [np.round(100 * i / K + np.random.randint(-15, 15)) + 10 for i in range(K)],
        'group': [np.random.randint(6) for _ in range(K)]
    })
    df.loc[df['test_0'] < 0, 'test_0'] = 0
    df.loc[df['test_0'] > 100, 'test_0'] = 100
    df.loc[df['test_1'] < 0, 'test_1'] = 0
    df.loc[df['test_1'] > 100, 'test_1'] = 100

    df['passed'] = df['test_1'].apply(lambda x: x > 40)
    return df

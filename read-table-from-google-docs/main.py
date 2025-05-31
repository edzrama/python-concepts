# Whole code for testing
import pandas as pd

doc_url =   'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'


def read_secret_message(source_url: str):
    
    table = pd.read_html(source_url, header=0, encoding='utf-8')[0]

    max_x = table['x-coordinate'].max()
    max_y = table['y-coordinate'].max()

    matrix = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, character, y in zip(table['x-coordinate'], table['Character'], table['y-coordinate']):
        matrix[y][x] = character

    for row in reversed(matrix):
        print(''.join(row))

read_secret_message(source_url=doc_url)
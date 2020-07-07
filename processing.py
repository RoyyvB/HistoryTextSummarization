import json
import os

def LoadData(article):

    with open(article, 'r', encoding="utf8") as f:
        data = json.load(f)

    print('Loaded {:,} articles from {}'.format(len(data), article))
    return data

def Execute():

    article = 'articles.json'
    data = LoadData(article)







def main():

    Execute()

if __name__ == '__main__':

    main()
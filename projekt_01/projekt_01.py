import argparse
from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import vcolor
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('name', help = 'name of file')
parser.add_argument('-n','--number', help = 'how many elements in histogram', type = int, default = 10)
parser.add_argument('-m','--minimal', help = 'minimal lenght of word', type = int, default = 0)

args = parser.parse_args()

with open(f'D:\VSCode Projects\projekt_01\{args.name}', encoding = 'utf8') as file:
    list = file.read().replace(',','').replace('!','').replace('—','').replace(':','').replace('«','').replace('»','').replace(';','').replace('…','').replace('?','').replace('.','').replace('*','').split()

dict = defaultdict(int)

for word in list:
    if len(word)>=args.minimal:
        dict[word] += 1

data = []

for i in range(args.number):
    word = max(dict, key=dict.get)
    data.append((word,dict[word]))
    del dict[word]

graph = Pyasciigraph()

pattern = [IBla, BWhi, UCya]
data_c = vcolor(data, pattern)

for line in graph.graph('Moj zajesuper histogram', data_c):
        print(line)
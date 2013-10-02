#!/usr/bin/env python

import dendropy
from dendropy.utility.fileutils import find_files
import sys

d = dendropy.DataSet()
o_file = sys.argv[1]
flist = find_files(top=o_file, filename_filter="*")
trees = dendropy.TreeList()
for tree_file in flist:
    trees.read_from_path(tree_file,'nexus')
d.attach_taxon_set()
d.read_from_path(tree_file, "nexus")	
print(d.taxon_sets[0].description(2))    

#H1 = helotrophidae & paraplea in in-group
h1 = 'Paraplea s','Helotrophi', 'Enithares', 'Nerthra sp', 'Ochterus m', 'Ilyocoris', 'Aphelochei','Laccotreph', 'Diplonychu'

#H2: helo in outgroup, but paraplea in in-group
h2 = 'Paraplea s','Enithares', 'Nerthra sp', 'Ochterus m', 'Ilyocoris', 'Aphelochei','Laccotreph', 'Diplonychu'
#Neither in in-group
h3 = 'Enithares', 'Nerthra sp', 'Ochterus m', 'Ilyocoris', 'Aphelochei','Laccotreph', 'Diplonychu'





split1 = trees.frequency_of_split(labels=h1)
print('Frequency of split %s: %s' % (h1, split1))

split2 = trees.frequency_of_split(labels=h2)
print('Frequency of split %s: %s' % (h2, split2))

split3 = trees.frequency_of_split(labels=h3)
print('Frequency of split %s: %s' % (h3, split3))
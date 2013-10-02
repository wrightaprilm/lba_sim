#!/usr/bin/env python

import dendropy
from dendropy import fileutils

flist = find_files(top=o_file, filename_filter="*")
for f in f_list:
	trees.read_from_path(f, 'nexus')

#H1 = helotrophidae & paraplea in in-group
h1 = ['Nerthra_sp____','Ochterus_marginatus___','Diplonychus_rusticus___','Laccotrephes_robustus___','Paraplea_sp____','Helotrophidae_sp____','Aphelocheirus_ellipsoideus___','Ilyocoris_cimicoides___','Enithares_tibialis___']
#H2: helo in outgroup, but paraplea in in-group
h2 = ['Nerthra_sp____','Ochterus_marginatus___','Diplonychus_rusticus___','Laccotrephes_robustus___','Paraplea_sp____','Aphelocheirus_ellipsoideus___','Ilyocoris_cimicoides___','Enithares_tibialis___']
#Neither in in-group
h2 = ['Nerthra_sp____','Ochterus_marginatus___','Diplonychus_rusticus___','Laccotrephes_robustus___','Aphelocheirus_ellipsoideus___','Ilyocoris_cimicoides___','Enithares_tibialis___']

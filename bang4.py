#!/usr/bin/env python
# -*- config: utf-8 -*-
import pdftotext
from collections import Counter
import string
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

balph1=u'অআইঈউঊঋএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৎংঃঁািীুূৃেৈোৌ'

with open('Lalshalu.pdf', 'rb') as f:
    pdf = pdftotext.PDF(f)

patto = "".join(pdf)

with open('NonditoNoroke.pdf', 'rb') as f:
    pdf = pdftotext.PDF(f)

patto = patto.join(pdf)

counts=Counter(patto)

sum=0
bcounts = []
for i in list(balph1):
    sum+=counts[i]

with open('Bn_out.tsv', 'w', encoding='utf-8') as out_file:
	out_file.write("{}\t{}\t{}\n".format('Letters', 'Relative Frequency (%)', 'Frequency'))
	for letter in list(balph1):
		bcounts.append((counts[letter]/sum)*100)
		out_file.write("{}\t{:.2f}\t{}\n".format(letter, (counts[letter]/sum)*100, counts[letter]))
	out_file.write("{}\t{}\t{}\n".format('Total Count', '100', sum))

prop = fm.FontProperties(fname='Nikosh.ttf',size=12)
#prop = fm.FontProperties(fname='kalpurush.ttf')
ypos = np.arange(len(balph1))

plt.figure(figsize=(20,7))
plt.bar(ypos, bcounts, align='center', alpha=0.5)
plt.xticks(ypos, balph1, FontProperties = prop)

for i, v in enumerate(bcounts):
	plt.text(i-.35, v+.2, '{:.2f}'.format(v), rotation='vertical')

plt.xlabel('Bangla Letters - Including Vowel Marks (কার সহ)', FontProperties = prop)
plt.ylabel('Relative Frequency (%)')
plt.margins(x=.023,y=.12)
plt.title('Relative Frequency of Letters in Bangla Text\nTotal Letters Counted: '+str(sum))
plt.savefig('ProgramOutputFig.png',bbox_inches='tight',pad_inches=.5)
plt.show()
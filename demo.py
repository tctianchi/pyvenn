# coding: utf-8

# ipython notebook requires this
# %matplotlib inline

# python console requires this
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import venn

labels = venn.get_labels([range(10), range(5, 15)], fill=['number', 'logic'])
fig, ax = venn.venn2(labels, names=['list 1', 'list 2'])
fig.savefig('venn2.png', bbox_inches='tight')
plt.close()

labels = venn.get_labels([range(10), range(5, 15), range(3, 8)], fill=['number', 'logic'])
fig, ax = venn.venn3(labels, names=['list 1', 'list 2', 'list 3'])
fig.savefig('venn3.png', bbox_inches='tight')
plt.close()

labels = venn.get_labels([range(10), range(5, 15), range(3, 8), range(8, 17)], fill=['number', 'logic'])
fig, ax = venn.venn4(labels, names=['list 1', 'list 2', 'list 3', 'list 4'])
fig.savefig('venn4.png', bbox_inches='tight')
plt.close()

labels = venn.get_labels([range(10), range(5, 15), range(3, 8), range(8, 17), range(10, 20)], fill=['number', 'logic'])
fig, ax = venn.venn5(labels, names=['list 1', 'list 2', 'list 3', 'list 4', 'list 5'])
fig.savefig('venn5.png', bbox_inches='tight')
plt.close()

labels = venn.get_labels([range(10), range(5, 15), range(3, 8), range(8, 17), range(10, 20), range(13, 25)], fill=['number', 'logic'])
fig, ax = venn.venn6(labels, names=['list 1', 'list 2', 'list 3', 'list 4', 'list 5', 'list 6'])
fig.savefig('venn6.png', bbox_inches='tight')
plt.close()


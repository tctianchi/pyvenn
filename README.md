# pyvenn
2 ~ 6 Sets Venn Diagram For Python

Use magic function in ipython notebook:
```python
%matplotlib inline

import venn
```

Or using non-interactive backend:
```python
import matplotlib
matplotlib.use('Agg')

import venn
```

Fetch labels of each subset in venn diagram. The input data is an array of iterable data(list, set, etc.). 
```python
In [5]: labels = venn.get_labels([
            range(10),
            range(5, 15)
        ], fill=['number', 'logic'])
In [6]: print labels
Out [6]: {'01': '01: 5', '10': '10: 5', '11': '11: 5'}
```

Plot functions are based on the labels:
```python
fig, ax = venn.venn2(labels, names=['list 1', 'list 2'])
fig.show()
```

![venn2](https://raw.githubusercontent.com/wiki/tctianchi/pyvenn/venn2.png)

More examples:
```python
labels = venn.get_labels([range(10), range(5, 15), range(3, 8)], fill=['number', 'logic'])
fig, ax = venn.venn3(labels, names=['list 1', 'list 2', 'list 3'])
fig.show()
```

![venn3](https://raw.githubusercontent.com/wiki/tctianchi/pyvenn/venn3.png)

```python
labels = venn.get_labels([range(10), range(5, 15), range(3, 8), range(8, 17)], fill=['number', 'logic'])
fig, ax = venn.venn4(labels, names=['list 1', 'list 2', 'list 3', 'list 4'])
fig.show()
```

![venn4](https://raw.githubusercontent.com/wiki/tctianchi/pyvenn/venn4.png)

```python
labels = venn.get_labels([range(10), range(5, 15), range(3, 8), range(8, 17), range(10, 20)], fill=['number', 'logic'])
fig, ax = venn.venn5(labels, names=['list 1', 'list 2', 'list 3', 'list 4', 'list 5'])
fig.show()
```

![venn5](https://raw.githubusercontent.com/wiki/tctianchi/pyvenn/venn5.png)

```python
labels = venn.get_labels([range(10), range(5, 15), range(3, 8), range(8, 17), range(10, 20), range(13, 25)], fill=['number', 'logic'])
fig, ax = venn.venn6(labels, names=['list 1', 'list 2', 'list 3', 'list 4', 'list 5', 'list 6'])
fig.show()
```

![venn6](https://raw.githubusercontent.com/wiki/tctianchi/pyvenn/venn6.png)

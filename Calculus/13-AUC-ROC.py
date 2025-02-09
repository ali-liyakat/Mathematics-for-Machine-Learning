# Area Under the ROC Curve

'''When we don't have a function but we do have 
coordinates, we can use the scikit-learn library's auc() method, which uses a numerical approach (the trapezoidal rule) to find the area under the curve described by the coordinates:'''

from sklearn.metrics import auc

xs = [0, 0,   0.5, 0.5, 1]
ys = [0, 0.5, 0.5, 1,   1]

print(auc(xs, ys))
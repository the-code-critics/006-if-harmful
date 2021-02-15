def penn2wn(tag):
    tags = {'N':'n', 'V':'v', 'J':'a', 'R':'r'}
    return tags.get(tag[0], None)

PENN2WN = {'N':'n', 'V':'v', 'J':'a', 'R':'r'}
WN2PENN = {v:k for v,k in PENN2WN.items()}

def penn2wn(tag):
    return PENN2WN.get(tag[0], None)

def wn2penn(tag):
    return WN2PENN.get(tag[0], None)


# -----------------------------------------------------------------------------

CLFS = [
    ('KNN-3', KNeighborsClassifier, {'n_neighbors':3}),
    ('KNN-5', KNeighborsClassifier, {'n_neighbors':5}),
    ('SVM-lin', SVC, {'C':0.1, 'kernel':'linear'})
]

def create_clf(clf):
    name, claz, kwargs = clf
    return claz(**kwargs)

def train(X, y):
    for clf in CLFS:
        _clf = create_clf(clf).fit(X, y)
        acc = _clf.score(X, y)
        print('name:', clf[0], 'acc', acc)


# -----------------------------------------------------------------------------


clzs = {
    'A': (ClassA, {'x':1}),
    'B': (ClassB, {'y':2})
}

clz, kwargs = clzs[name]
clz(**kwargs)
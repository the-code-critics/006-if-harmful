def penn_to_wn(tag):
    """Penn Treebank tag to Wordnet"""

    if tag.startswith('N'):
        return 'n'

    if tag.startswith('V'):
        return 'v'

    if tag.startswith('J'):
        return 'a'

    if tag.startswith('R'):
        return 'r'

    return None


# -----------------------------------------------------------------------------


def create_clf(name):
    if name == 'KNN-3':
        return KNeighborsClassifier(n_neighbors=3)
    if name == 'KNN-5':
        return KNeighborsClassifier(n_neighbors=5)
    if name == 'SVM-lin':
        return SVC(C=0.1, kernel='linear')
    ...
		 raise ValueError('Unknown clf: ' + name)

# -----------------------------------------------------------------------------

if name == 'A':
    return ClassA(x=1)
if name == 'B':
    return ClassB(y=2)
raise ValueError()
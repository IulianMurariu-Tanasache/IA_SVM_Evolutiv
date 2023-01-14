import sklearn.metrics as metrics

def evaluate(svm, test_data):
    y_true = []
    y_pred = []
    for entry in test_data:
        y_true.append(entry[1])
        y_pred.append(svm.prezicere(entry[0]))

    print('accuracy: ' + str(metrics.accuracy_score(y_true, y_pred)))
    print('precision: ' + str(metrics.precision_score(y_true, y_pred)))
    print('f1 score: ' + str(metrics.f1_score(y_true, y_pred)))
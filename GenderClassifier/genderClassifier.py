from sklearn import tree, svm, neural_network, ensemble, gaussian_process

#[height, weight, shoe size]
X = [[181,80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177,70, 40], [159, 55,37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']

clf_1 = tree.DecisionTreeClassifier()
clf_2 = svm.SVC()
clf_3 = neural_network.MLPClassifier()
clf_4 = ensemble.AdaBoostClassifier()
clf_5 = ensemble.RandomForestClassifier()
clf_6 = gaussian_process.GaussianProcessClassifier()

clf_1 = clf_1.fit(X,Y)
clf_2 = clf_2.fit(X,Y)
clf_3 = clf_3.fit(X,Y)
clf_4 = clf_4.fit(X,Y)
clf_5 = clf_5.fit(X,Y)
clf_6 = clf_6.fit(X,Y)

prediction_1 = clf_1.predict([[190, 70, 43]])
prediction_2 = clf_2.predict([[190, 70, 43]])
prediction_3 = clf_3.predict([[190, 70, 43]])
prediction_4 = clf_4.predict([[190, 70, 43]])
prediction_5 = clf_5.predict([[190, 70, 43]])
prediction_6 = clf_6.predict([[190, 70, 43]])

print(prediction_1, prediction_2, prediction_3, prediction_4, prediction_5, prediction_6, sep= "\n")

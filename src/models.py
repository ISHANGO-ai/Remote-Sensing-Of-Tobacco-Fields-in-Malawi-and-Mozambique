""" Randomforst classifier to train model"""

import numpy
#from config import args

import ee
import geemap
import pandas as pd

from geemap import ml
from sklearn import ensemble
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold, cross_validate
from sklearn.metrics import make_scorer, recall_score, accuracy_score, precision_score, f1_score



def randomforest():
  geemap.ee_initialize()
  ee.Authenticate()
  ee.Initialize()

  # read the feature table to train our RandomForest model
  # data taken from ee.FeatureCollection('GOOGLE/EE/DEMOS/demo_landcover_labels')

  url = "https://raw.githubusercontent.com/giswqs/geemap/master/examples/data/rf_example.csv"
  df = pd.read_csv(url)
  # specify the names of the features (i.e. band names) and label
  # feature names used to extract out features and define what bands

  feature_names = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7']
  label = "landcover"
  # get the features and labels into separate variables
  X = df[feature_names]
  y = df[label]
  # create a classifier and fit
  n_trees = 100 
  rf = ensemble.RandomForestClassifier(n_trees).fit(X,y)
  #We perform hyper parameter tunning.
  param_grid = {'n_estimators': [300, 500],
                      'max_depth':[50, 70],
                      'min_samples_split': [5, 10],
                      'min_samples_leaf': [2, 10]}
  #inner loop for tuning the hyperparameters
  cv_inner = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
  #outer loop for testing on holdout set
  cv_outer = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
  rf = ensemble.RandomForestClassifier()
  scorer = {'accuracy': make_scorer(accuracy_score),
            'precision': make_scorer(precision_score, average = 'macro'),
            'recall': make_scorer(recall_score, average = 'macro'),
            'f1_macro': make_scorer(f1_score, average = 'macro'),
            'f1_weighted': make_scorer(f1_score, average = 'weighted')}
  clf = RandomizedSearchCV(estimator=rf, param_distributions=param_grid, cv=cv_inner, random_state=42, n_iter=5)
  nested_score = cross_validate(clf, X=X, y=y, cv=cv_outer, scoring=scorer, return_estimator=True)
  model = clf.fit(X,y)
  #We print the optimal parameters for our model.
  from pprint import pprint
  pprint(model.best_estimator_.get_params())
  #We evaluate the performance of our model with the optimal parameters.
  nested_score

  #We now fit our model with the optimum parameter to the data.
  rf= ensemble.RandomForestClassifier(bootstrap= True,
  ccp_alpha= 0.0,
  class_weight= None,
  criterion= 'gini',
  max_depth= 50,
  max_features= 'auto',
  max_leaf_nodes= None,
  max_samples= None,
  min_impurity_decrease= 0.0,
  min_samples_leaf= 2,
  min_samples_split= 5,
  min_weight_fraction_leaf= 0.0,
  n_estimators= 300,
  n_jobs= None,
  oob_score= False,
  random_state= None,
  verbose= 0,
  warm_start= False).fit(X,y)


  # convert the estimator into a list of strings
  # this function also works with the ensemble.ExtraTrees estimator
  trees =  ml.rf_to_strings(rf,feature_names)
  # print the first tree to see the result
  print(trees[0])
  # number of trees we converted should equal the number of trees we defined for the model
  len(trees) == n_trees

  # create a ee classifier to use with ee objects from the trees
  ee_classifier = ml.strings_to_classifier(trees)

  ##Classify image using GEE classifier
  # Make a cloud-free Landsat 8 TOA composite (from raw imagery).
  l8 = ee.ImageCollection('LANDSAT/LC08/C01/T1');

  image = ee.Algorithms.Landsat.simpleComposite(
    collection= l8.filterDate('2018-01-01', '2018-12-31'),
    asFloat= True
  )
  # classify the image using the classifier we created from the local training
  # note: here we select the feature_names from the image that way the classifier knows which bands to use
  classified = image.select(feature_names).classify(ee_classifier)
  # display results
  legend_keys = ['vegetation', 'water', 'bare soil']
  legend_colors = ['#008000', '#0000FF', '#FF0000', ]
  Map = geemap.Map(center=(37.75,-122.25), zoom=11)

  Map.addLayer(image,{"bands": ['B7', 'B5', 'B3'], "min":0.05, "max": 0.55, "gamma":1.5}, 'image')
  Map.addLayer(classified, {"min": 0, "max": 2, "palette": ['red', 'green', 'blue']},'classification')
  Map.add_legend(legend_keys=legend_keys, legend_colors=legend_colors, position='bottomright')

  return  Map

randomforest()

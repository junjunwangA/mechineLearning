#coding:utf-8
'''
Created on Mar 23, 2016

@author: junjwang
'''


from numpy import *
import svm

################## test svm #####################
## step 1: load data
print "step 1: load data..."
dataSet = []
labels = []
fileIn = open('D:/soft/python/testSet.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split('\t')
    dataSet.append([float(lineArr[0]), float(lineArr[1])])
    labels.append(float(lineArr[2]))

dataSet = mat(dataSet)## numPy 函数， 将数组转化为矩阵
labels = mat(labels).T
train_x = dataSet[0:81, :]
train_y = labels[0:81, :]
test_x = dataSet[80:101, :]
test_y = labels[80:101, :]

## step 2: training...
print "step 2: training..."
C = 0.6
toler = 0.001 ## 迭代的终止条件
maxIter = 50
svmClassifier = svm.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption = ('linear', 0)) ##  //() 元组就像不可更改的列表list【】

## step 3: testing
print "step 3: testing..."
accuracy = svm.testSVM(svmClassifier, test_x, test_y)

## step 4: show the result
print "step 4: show the result..."    
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
svm.showSVM(svmClassifier)
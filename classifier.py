import os
import random
from collections import defaultdict

negativeDict = defaultdict(int)
positiveDict = defaultdict(int)

def training(positiveList, negativeList, negativeFile, positiveFile):
	'''
	positiveFolder, negativeFolder -- (string) folders where positive and negative comments are
	positiveFile, negativeFile -- (string) filenames where the values of each word will be written
	'''

	nPositive = 0
	nNegative = 0

	for f in negativeList:
		file = open(f, 'r')

		for l in file:
			for w in l.split(" "):
				negativeDict[w.rstrip('\r\n')] += 1
				nNegative += 1

	for f in positiveList:
		file = open(f, 'r')

		for l in file:
			for w in l.split(" "):
				positiveDict[w.rstrip('\r\n')] += 1
				nPositive += 1


	vocabularySize = len(positiveDict.keys()) + len(negativeDict.keys())

	for k in list(set(positiveDict.keys()) + set(negativeDict.keys())):
		num = positiveDict[k] + 1 # Zero frequency problem solve
		den = nPositive + vocabularySize

		positiveProbabilities[k] = num/den





baseDir = os.path.dirname(os.path.realpath(__file__))
positiveFiles = [os.path.join('pos', f) for f in os.listdir('pos')]
negativeFiles = [os.path.join('neg', f) for f in os.listdir('neg')]

random.shuffle(positiveFiles)
random.shuffle(negativeFiles)

positiveFilesForTraining = positiveFiles[:int(len(positiveFiles)*0.8)]
negativeFilesForTraining = negativeFiles[:int(len(negativeFiles)*0.8)]

positiveFilesForTesting = list(set(positiveFiles) - set(positiveFilesForTraining))
negativeFilesForTesting = list(set(negativeFiles) - set(negativeFilesForTraining))

training(positiveFilesForTraining, negativeFilesForTraining,'t','t')
print(negativeDict)
print(positiveDict)
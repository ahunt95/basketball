import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

np.random.seed(10)

dates = []
spreads = []

def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile  )
		next(csvFileReader) # First row is a header
		for row in csvFileReader:
			if row[1] != '':
				dates.append(int(row[1].split('-')[0]))
				spreads.append(float(row[7]))

	return

get_data('celticsseason.csv')
#print(dates)
#print(spreads)

dates = np.reshape(dates, (len(dates), 1))
#print(dates)

svr = SVR(C=1)
svr.fit(dates, spreads)
p = svr.predict(dates)

prediction = svr.predict(73)
print('2018-2019 Celtics win/loss ratio prediction:', prediction[0])

plt.scatter(dates, spreads, color='black', label='Data')

plt.plot(dates, p, color='red', label='RBF model')
plt.title('Support Vector Regression: Celtics Seasons')
plt.xlabel('Year')
plt.ylabel('Win/Loss Ratio')
plt.legend()
plt.show()


import arrests.analysis as arrest
import pandas as pd
import numpy as np

ar = arrest.analyzeArrests()

ar.plotArrestsToCrimesOverTime()
parameters = pd.DataFrame(columns=['all_a', 'all_b', 'all_c', 'pre_a', 'pre_b', 'pre_c', 'post_a', 'post_b', 'post_c'])
crime_types = ar.get_types()
crime_types = np.insert(crime_types, 0, 'all')

problem_types = []
for crimetype in crime_types:
    try:
        props = ar.genMonthlyArrestProportions(crimetype)
        pm = ar.plotMonthlyArrestProportions(props, crimetype)
        parameters = parameters.append(pm)
        outliers = ar.findOutliers(props, crimetype, pm)
        with open('arrests/outliers/'+ crimetype + '_outliers.txt', 'w+') as f:
            f.write(outliers)
    except:
        problem_types.append(crimetype)
        print("Problem with: " + crimetype)

parameters.to_csv('arrests/parameters.csv')
print("Problems with: " + str(problem_types))


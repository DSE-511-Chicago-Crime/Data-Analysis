import arrests.analysis as arrest
import pandas as pd

ar = arrest.analyzeArrests()
#ar.plotArrestsToCrimesOverTime()
parameters = pd.DataFrame(columns=['all_a', 'all_b', 'all_c', 'pre_a', 'pre_b', 'pre_c', 'post_a', 'post_b', 'post_c'])
pm = ar.plotMonthlyArrestProportions(ar.genMonthlyArrestProportions())
parameters = parameters.append(pm)

input("Press Enter to continue...")
problem_types = []
for crimetype in ar.get_types():
    try:
        pm = ar.plotMonthlyArrestProportions(ar.genMonthlyArrestProportions(crimetype), crimetype)
        parameters = parameters.append(pm)
    except:
        problem_types.append(crimetype)
        print("Problem with: " + crimetype)
parameters.to_csv('arrests/parameters.csv')
print("Problems with: " + str(problem_types))

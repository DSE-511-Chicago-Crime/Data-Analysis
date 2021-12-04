import arrests.analysis as arrest

ar = arrest.analyzeArrests()
#ar.plotArrestsToCrimesOverTime()
ar.plotMonthlyArrestProportions(ar.genMonthlyArrestProportions('ROBBERY'))
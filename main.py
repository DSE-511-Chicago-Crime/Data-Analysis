import arrests.arrestsRunner as arrestsRunner
import domestic.domesticRunner as domesticRunner
import districts.crime_district_analysis as crime_district_analysis

# Analysis of domestic cases - results shown with plt.show()
dr = domesticRunner.domesticRunner()
dr.run()

# Analysis of crime per district - results shown with plt.show()
cda = crime_district_analysis.crime_district_analysis()
cda.run()

# I've turned off the generation of matplotlib charts and output files to speed things up.
# And just like, not play around in memory for no reason.
# To test those, you can set the parameters in the constructor to True.
# If false, the program will still print some summary data to show that it's working.
ar = arrestsRunner.arrestsRunner(newgraphs=False, newOutliers=False)
ar.run()
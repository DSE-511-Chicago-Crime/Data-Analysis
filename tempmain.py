import arrests.arrestsRunner as arrestsRunner

# I've turned off the generation of matplotlib charts and output files to speed things up.
# And just like, not play around in memory for no reason.
# To test those, you can set the parameters in the constructor to TRUE.
# The program will still print some summary data to show that it's working.
ar = arrestsRunner.arrestsRunner(newgraphs=True, newOutliers=True)
ar.run()
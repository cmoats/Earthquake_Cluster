# Earthquake_Cluster
This implements the k-means clustering algorithm and plots earthquake data (with magnitudes greater than 6 from 2010 to 2021) on a map. To run, download the files and make sure that the data is in the same file as earthquake_cluster python file.  

# Calibrating The Map

When I first started plotting the clusters I got results that I knew were weird (lots of earthquakes were happening in flordia), so I had to recalibrate where the points were being plotted. To calibrate where the points were being plotted, I got earthquake data only from Oregon and then shifted the longitude and latitude so each of these earthquake data points from Oregon would be plotted in Oregon. 

Result of Oregon earthquake data before calibration:
![image of Before Calibration](https://github.com/cmoats/Earthquake_Cluster/blob/main/Before_Calibration.PNG)

Results of Oregon earhquake data after calibration:
![image of After Calibration](https://github.com/cmoats/Earthquake_Cluster/blob/main/After_calibration.PNG)

Now that we've calibrated where the points should be plotted, lets look at our results. 


# Results

After running the program I got this:

![image of earthquake cluster](https://github.com/cmoats/Earthquake_Cluster/blob/main/Clustering%20results.PNG)

The size of the dots reflect the different magnitude of each earthquake and the different colors represent the clusters. To check how accurate our plotting looks, we can compare our plot to a map of the tectonic plates of Earth. So, we expect most of our earthquakes to be happening near the tectonic plate borders and if they aren't then we either have wrong data or did something else wrong. 

Here is a map of the tectonic plates:

![image of Tectonic Plates](https://github.com/cmoats/Earthquake_Cluster/blob/main/Tectonic%20Plates.jpg)

So we can see that most of our earthquakes are happening along the tectonic plates which means our plot is working well. 

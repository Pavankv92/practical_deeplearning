### Practical Deeplearning 

This repo contains the code for the book "Practical Deeplearning A python based introduction by Ronald T. Kneusel". 

### Data

The goal of the dataset is to faithfully and completely capture the parent distribution, or what the data will look like in the wild when the model is used. So how much data is needed to capture parent distribution ? and how many features should the dataset have ? Here is the good thumb rule: A feature vector should contain only features that captures the aspects of the data that allow the model to generalize to new data. In other words, features should capture aspects of the data that help the model separate the classes. We need enough features to capture all the relevant parts of the data so that the model has something to learn from, but if we have too many features, we fall victim to the the curse of dimensionality.

Curse of dimensionality: Generally, A D dimensional space feature vector (D= length of the vector) would need about $10^D$ data points to represent that space "well". So, 2D feature sapce would need 100 data points, 3D = 1000, 4D = 10,000 etc. 

Dataset can be summarized by mean, median, std.dev, min and max value and std.error. Std.error is also known as standard error of the mean $\bar{x}$. This is the stf.dev divided by the square root of the number of the elements in the dataset. The std. error is a measure of the difference between dataset mean value $\bar{x}$ and the mean value of the parent distribution. Idea is that if we have more data, we'll have better idea of the parent distribution that is generating this data, and so the mean value of the dataset will be closer to the mean value of the parent distribution. 
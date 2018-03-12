# Using supervised learning image analysis to predict inequality measures in Sub-Saharan Africa

For my thesis I will be analyzing raster images and associated metadata from NASA satellite imagery databases. My goal will be to show how investing in agriculture can improve inequality while filling in historical and present-day data gaps in Sub-Saharan Africa.

I have access to hundreds of thousands of images from 1972 to present day with one major restriction: these images are huge, so I want to work as much as possible with remotely hosted data. Older imagery (more than 10 years old) isn’t hosted remotely in an accessible way, so it is essential that I figure out filtering algorithms in order to reduce the size requirements of my data and hopefully keep hosting costs at $0. After algorithmic filtering I will move on to supervised machine learning processes.

**My metadata text filtering will look something like the following:**

_Select an image from this lat and long
taken between 11am and 3pm
somewhere between 1981 to 1983
That has a cloud cover of less than 5%_

_Note: One big challenge with image filtering will be to define agricultural areas for my image filtering. There is landuse data included in NASA's satellite imagery, but I'm not sure how extensive it is. This may require a different tool._

Supervised learning will be used to compare rastor image analysis to world bank data. The goal will be to create a supervised learning algorithm that predicts changes in inequality measures over time through analyzing visual shifts in agriculture health over time.

**The training model would:**

-  Analyze how a set of training images of non-urban agricultural areas change over time
- Analyze how shifts in training images correspond to shifts in training data from the world bank.

**The goal would be to:**

- Predict inequality data based on shifts in test satellite image data.


**With the purpose of:**

- Showing visually how how investing in agriculture can improve inequality while filling in historical and present-day data gaps in Sub-Saharan Africa.

This is supervised learning in the sense that I will be providing my model with general features for prediction, but because I don’t want to to define every potential rgb value predictor feature, I will need to use supervised feature extraction. I am thinking about using scikit-image and regression to create my model. This idea will gradually become simpler with the incorporation of image averaging and already created analysis tools. In terms of prediction accuracy, I would be happy with anything over 80%.

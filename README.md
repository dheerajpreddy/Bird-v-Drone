# Is it a plane? Is it a bird? No, it's a drone
DIP Project - Build a system to distinguish between drones and birds

## Proposed Algorithm

### Pipeline

1. Noise filtering
2. Localisation
3. Object Detection

#### Noise Filtering

We plan to use some common noise filtering algorithms to remove the salt & pepper noise, etc. and then quantize the image to reduce the sample space of the histogram of oriented gradients (HOG) and improve the accuracy of the same.


#### Localisation

We plan to do the following to localise the oboject of interest:

1. Convolve with some edge detection filter.
2. Binarize the image to run image morphology operators.
3. Run closening morphology operator to remove small gaps and better segment the objects.
4. Merge small components with their parents to reduce the number of components.
5. Run object detection on all the subset of the components.


#### Object Detection

We plan to normalize the component image size for better comparision and then use the following features to predict the probability of being a bird/drone:

1. The HOG of the given subset of components.
2. Hough transform with more weight given to straight edges. (Use quantized edge slopes)

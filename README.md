# Is it a plane? Is it a bird? No, it's a drone

## Problem
An accurate machine learning model built with using just advanced feature extraction techniques to localize and recognize the object of interest and comparing the results with that of convolutional neural networks.


## Dataset

Manual collection of datasets, since a proper dataset for drones isn't available. We collect 100 pictures each of 10 species of birds, and 10 models of drones. Of the birds, 8 are aerial and 2 are aquatic birds. And of the drones, 8 are regular drone models sold to the public, and 2 are military drones, serviced by the US military.

10 species of birds -
    1. Owl
    2. Pigeon
    3. Dove
    4. Falcon
    5. Parrot
    6. Eagle
    7. Kingfisher
    8. Goose
    9. Duck
    10. Swan

10 models of drones -
    1. DJI Phantom 3
    2. DJI T600 Inspire 1
    3. DJI Phantom 2 Vision+ V3.0
    4. DJI Phantom 3 Advanced
    5. DJI Phantom 2 Vision+
    6. Parrot PF725100 BeBop
    7. Heli-Max 1SQ
    8. DJI Phantom Aerial
    9. Lockheed Martin Stalker
    10. Boeing Insitu ScanEagle

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

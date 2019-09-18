# ISL
Indian Sign Language Translation

## Problem Statement
Build an automatic ISL translator i.e given an input video of someone signing a word, the model should be able to predict which word is being signed.

## Current Solution

* Visualize video as sequence of images

* Convert each image to skeletal figure
![alt text](https://github.com/goru001/isl/blob/master/isl.png)

* Use Pattern matching
  * Convert the skeletal image to feature vector of 512 dimension by using Resnet-18 pretrained model
  * Find cosine distance between images of two videos which occur in the middle of the video's image sequence. If cosine distance is greater than 95, then we consider the two images to be similar. and the video sequence with which the similar images occur the most, those two videos are considered to have similar label.
  
## Results

### No. of Classes: 29
`'letter', 'train', 'transportation', 'mouse', 'thank_you', 'season', 'it', 'old', 'bill', 'bus', 'fast', 'soap', 'ring', 'you', 'boat', 'television', 'they', 'dry', 'week', 'hello', 'laptop', 'clock', 'truck', 'spring', 'how_are_you', 'shirt', 'happy', 'science', 'quiet'`

### No. of videos: 73

### Avg. No. of videos per class: 2-3

### Accuracy
~51%


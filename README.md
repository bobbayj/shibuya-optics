# shibuya-optics
Image recognition using deep learning to recognise common household items (focus on the pantry)

## The idea:
1. Deep Learning will detect what any object is
2. Data I have available is image data from Google, and pictures of things I can take myself
3. I don't have enough image data, so I will need to be smart about how I use my data
4. I could use **Transfer Learning** to pre-train my model, then fine-tune it to my specific datasets
5. By the end of the project, I can theoretically take a photo of any product and know what it is (in a general sense, i.e. it is Lurpak butter, but I don't know if its salted/unsalted)

## Dependencies not in pipfile:
- imgaug (https://github.com/aleju/imgaug)
- Tensorflow-gpu (https://www.tensorflow.org/install/gpu)
    - Recommended to use GTX 1060 or above!

## Useful Docs
https://blog.floydhub.com/structuring-and-planning-your-machine-learning-project/
- Important to plan code at a production level to ensure reproducibility

## Work Plan
### 1. Pre-processing
- Obtain data from custom google image search and file appropriately
- How to begin transfer learning?

### 2. Data Segmenting
- K-fold means cross-validation
    - How should I split my data? This will affect how I store it in hdf5 files
- I should definitely save some images I took myself for the test set
    - Some images I took by hand should be in the validation set

### 3. Model Architecture
- Use Tensorflow or Keras?
- What Image Recognition model should I use?
    - Use a pre-made model?
    - Tweak a model?

### 5. Theoretical deployment to the cloud
- AWS or Azure?
- How does deploying to the cloud affect my workflow?

# Other
Fun fact: name of this repo was inspired by the Shibuya crossing. I was going to try and recognise objects from YouTube's livestream of the Shibuya crossing, but some forethought told me that won't be super useful...

Nonetheless, good opportunity to practice my machine learning for fun - can be used to detect the demographic in the area for smarter advertising in areas like these?

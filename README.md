# ML-in-production

In this tutorial we will try to walk together through all the building blocks of a Machine/Deep Learning project in production, i.e. a model that people can actually interact with

As a case study, we’ll be creating a web interface for image recognition using the pretrained model VGG19.

You can check the detailed explanation on the article I wrote in Towards Data Science [here](https://towardsdatascience.com/machine-learning-in-production-keras-flask-docker-and-heroku-933b5f885459)

Without going into too much detail, this project consists of 4 major parts :

## Build model

I've used use a pretrained (and effective) Convolutional Neural Network model for image classification : [VGG-19](https://arxiv.org/abs/1409.1556).

[model.py](./model.py) describe how to load the model, preprocess images in order to be used by that model, and make predictions.

# Facebook Marketplace Recommendation Ranking System

This is my final project that I'm working on. It forms the main project of my 'Machine Learning' training at AICore [https://www.theaicore.com/]

Facebook Marketplace is a platform for buying and selling products on Facebook. This is an implementation of the system behind the marketplace, which uses AI to recommend the most relevant listings based on a personalised search query.

In summary I will be using machine learning to find vector representations called embeddings of the search query and the different products and rank the most similar vectors highest.

This will be done by using a multi-modal neural network which combines both a text understanding network and an image understanding network to produce the final embedding for each listing

Once the model is trained, I will deploy it using FastAPI, containerising it using Docker, and uploading it to an EC2 instance. The API will contain all the models that I create and train, so any new request can be processed to make predictions on the cloud. 

To ensure that the model can be easily modified without building a new image again, the files corresponding to each model will be bound to the Docker image, so it allows us to update the models with retrained models even after deploying them.

# Milestone 1-2

These steps involved creating the github repo and acquire an understanding of the Facebook Marketplace ranking system

# Milestone 3
## Task 1

This task involved acquiring (via ssh on aws) and cleaning two .csv dataset files (images.csv and products.csv)
The .csv file contained line terminators that were not compatible with the default pandas reader. In order to load it, I had to set a different line terminator.The dataset files contained information about the listing, including its price, location, and description.

I first created a file named 'clean_tabular_data.py' within the repository. In this file, I created code to clean the tabular dataset.
I explored the file to try to understand it's contents and what I wanted to acheive. I realised that many of the prices were not in the correct format including additional commas and currency symbols. There were also rows with NaN values.

The cleaning procedure therefore had two steps:
- Remove all the NaN values in any column.
- Convert the prices into a numerical format.

The 'input_data' function loaded in the data and dropped any rows with NaN values.
The 'clean_price_data' functions loads in the '['price']' column as a variable 'price_data' then proceeds to remove currency symbols, commas and the converts it to float type.

## Task 2

The images.csv files has id and product id columns. The id corresponds to the fliename of the image for the respective product (product id). My objective was to assign a label to each image (id). The code can be found in 'sandbox.ipynb'

## Task 3

images.csv contains multiple images of the products. On closer inspection, they do not they have the same size nor the same number of channels. Thus, I had to change them so that they are all consistent.

I created a file named 'clean_images.py' in my repository. In this file, wrote code to clean the image dataset. Within this, I created a pipeline that will apply the necessary cleaning to the image dataset by defining a function called 'clean_image_data'. It takes in the raw image path 'images/raw', then cleans them and saves them into a new folder called "images/cleaned_images".

## Task 4 and 5

These steps involved updating the README and uploading changes.



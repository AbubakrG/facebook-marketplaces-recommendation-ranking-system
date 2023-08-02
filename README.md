# Facebook Marketplace Recommendation Ranking System

This is my final project that I'm working on. It forms the main project of my 'Machine Learning' training at AICore [https://www.theaicore.com/]

Facebook Marketplace is a platform for buying and selling products on Facebook. This is an implementation of the system behind the marketplace, which uses AI to recommend the most relevant listings based on a personalised search query.

In summary I will be using machine learning to find vector representations called embeddings of the search query and the different products and rank the most similar vectors highest.

This will be done by using a multi-modal neural network which combines both a text understanding network and an image understanding network to produce the final embedding for each listing

Once the model is trained, I will deploy it using FastAPI, containerising it using Docker, and uploading it to an EC2 instance. The API will contain all the models that I create and train, so any new request can be processed to make predictions on the cloud. 

To ensure that the model can be easily modified without building a new image again, the files corresponding to each model will be bound to the Docker image, so it allows us to update the models with retrained models even after deploying them.

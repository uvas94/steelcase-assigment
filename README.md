# steelcase-assigment

# Description
Service to predict if a movie would be for my liking 

# Data set
The list of movies i've watched for the past 10 years. The data is curated and cleaned then split into train and test (0.8/ 0.2). Also the categorical features are given labels and the skewed features are transformed using a log transform.

# Model
A linear regression is used to fit the training data then the performance of the model is tested.

# Web service
For the web service I used Flask. There are two web pages. Frist is a welcome page and the second is a page with a form where you input the data and get back the score.
To run the service you need to have the requirments installed in your conda/python env and use the following command to start the server:
python app.py
Then connect to localhost:5000/

For web service monitoring you can use monitoring web app. For this you need to run the commnad: 
python monitoring_web.py
Then connect to:
 127.0.0.1:5003/status to check if the app is still running 
and
127.0.0.1:5003/resources to check the resource consumption 

# Docker
The web app is dockerized. To build the docker container you can use the command sudo docker build -t imdb-score . which uses the dockerfile included in the repo. For running the docker image you need to use: sudo docker run -p 5000:5003 imdb-score. This will run both the app and the monitoring service

# Model tracking 
For model tracking we use MLFlow you first need to install in your python env the ml flow library, then start the server with the following command mlflow ui --port 5000. We connect to the server using our script from the jupyter notebook where we log the rmse and the model. In time this can be extend to log the dataset as well.
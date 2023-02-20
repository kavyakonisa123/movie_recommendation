
Readme

•	Open the terminal 

•	Create a virtual environment using conda


Step 1: Check if conda is installed in your path.  

>>>conda -V

Step 2: Update the conda environment 

>>>conda update conda

Step 3: Set up the virtual environment 

>>>conda create -n <envname> python=x.x anaconda

Step 4: Activating the virtual environment

>>>conda activate <envname>

•	Place the templates, static, test.py, and final.csv , actor1.xlxs,  tmdb_movies_data.csv  , requirements.txt in the virtual environment

•	Use the command to install all the required python modules

>>>pip install -r requirements. txt  
(Make sure it creates the requirements .txt file in the folder)

•	Run the flask application 

>>>Python test.py

•	Open the browser and paste the localhost address along with route decorator

http://127.0.0.1:4998/
This will open the home page of the website.
You can navigate to movies, actors and popular movies in the

http://127.0.0.1:4998/actors

http://127.0.0.1:4998/movies

http://127.0.0.1:4998/highest


You can search for a movie in the search box. If it is present in the database, it recommends similar movies. If it is not present, it shows the movie is not in the database.

Ex: try 

The Godfather
Avengers: Age of Ultron 

Etc. to see the recommended movie


In the terminal,
Run  
            jupyter notebook.

Run all cells to see data preprocessing, visualization is done.
Check the collaborative filtering by changing the uid. It results in similar movies for that user.


References:-

•	https://www.analyticsvidhya.com/blog/2022/01/movie-recommendation-engine-with-nlp/
•	https://www.kaggle.com/code/alaanabil98/investigate-tmdb-10000-movies-dataset/notebook
•	https://www.kaggle.com/code/morrisb/how-to-recommend-anything-deep-recommender
•	https://towardsdatascience.com/how-to-build-a-movie-recommendation-system-67e321339109




![image](https://user-images.githubusercontent.com/110701700/220211935-6ae8b1bb-dfa8-43bd-9517-051d9c7a6801.png)

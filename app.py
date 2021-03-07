import pickle
import Decode as dec
import path
from flask import Flask, render_template, request

app=Flask(__name__)
model=pickle.load(open(path.model,'rb'))

# @app.route("/")
# def home():
#     return 'Welcome all'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method=="POST":
        #season=int(request.form['Season'])
        City=str(request.form['City'])
        Team1 = str(request.form['Team1'])
        Team2 = str(request.form['Team2'])
        Toss_winner = str(request.form['Toss_winner'])
        Toss_decision = str(request.form['Toss_decision'])
        Result = str(request.form['Result'])
        DL_applied	 = str(request.form['DL_applied'])
        Win_by_runs = int(request.form['Win_by_runs'])
        Win_by_wickets = int(request.form['Win_by_wickets'])
        Venue = str(request.form['Venue'])
        arr=dec.decode_features(City, Team1, Team2, Toss_winner, Toss_decision, Result, DL_applied, Win_by_runs, Win_by_wickets, Venue)
        print(City)
        return render_template('index.html', prediction_text="The match winning team is '{}'".format(City))
    else:
        return render_template('index.html')


if __name__ =='__main__':
    app.run(debug=True)
import pickle
import path
import json

model = pickle.load(open(path.model, 'rb'))

with open(path.json_path) as file:
    factor_codes = json.load(file)

def predict(enc_obj, team1, team2):
    winner = model.predict([enc_obj])
    win_prob_score = model.predict_proba([enc_obj])

    decode_winner = factor_codes['team_trans'][str(winner[0])]
    team1_txt = factor_codes['team_trans'][str(team1)]
    team2_txt = factor_codes['team_trans'][str(team2)]
    #team1_score= win_prob_score[factor_codes['team_trans'].keys]

    #prob_out = factor_codes['team_trans'][str(win_prob_score)]
    # print(decode_winner)

    return decode_winner
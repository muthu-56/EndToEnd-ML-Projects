import app as ap
import json
import path
import Model_prediction as mp

# def json_codes():
#     with open(path.json_path) as file:
#         factor_codes = json.load(file)
#     return factor_codes

with open(path.json_path) as file:
    factor_codes = json.load(file)

def decode_features(place, Team1, Team2, Toss_winner, Toss_decision, Result, DL_applied, Win_by_runs, Win_by_wickets, Venue):
    #Season= season
    Place = factor_codes['place1'][place]
    team1 = factor_codes['team1'][Team1]
    team2 = factor_codes['team1'][Team2]
    TW = factor_codes['team1'][Toss_winner]
    toss = factor_codes['toss1'][Toss_decision]
    result = factor_codes['outcome1'][Result]
    DL_applied = factor_codes['dl_method'][DL_applied]
    Win_by_runs = Win_by_runs
    Win_by_wickets = Win_by_wickets
    venue = factor_codes['ground1'][Venue]
    enc_obj = [Place, team1, team2, TW, toss, result, DL_applied, Win_by_runs, Win_by_wickets, venue]
    final_obj = mp.predict(enc_obj, team1, team2)

    return final_obj

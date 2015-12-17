from flask import Flask, render_template, redirect, url_for, request, jsonify
from hotels_and_sight_seeing import *
import sqlite3
import os
import json

app = Flask(__name__)

@app.route('/get-hotel-list')
## */get-hotel-list?state=<state>&city=<city>
def get_hotels():
    
    q_string=request.query_string
    q_list=q_string.split('&')
    queries_res=[]
    for x in q_list:
        tmp=x.split('=')
        queries_res.append(tmp[1])

    answer=get_hotel_list(queries_res[0],queries_res[1])
    dic={}
    i=1
    for elem in answer:
        dic[i]=elem[1]
        i+=1
        

    return json.dumps(dic, sort_keys=True)



@app.route('/get-sightseeing-list/')
## */get-sightseeing-list/?state=<state>&city=<city>
def get_sightseeing():

    q_string=request.query_string
    q_list=q_string.split('&')
    queries_res=[]
    for x in q_list:
        tmp=x.split('=')
        queries_res.append(tmp[1])

    answer=get_sightseeing_list(queries_res[0],queries_res[1])

    return jsonify(answer)

@app.route('/get-hotel-reviews/')
## */get-hotel-reviews?state=<state>&city=<city>&hotel_id=<id>
def hotel_reviews():

    q_string=request.query_string
    q_list=q_string.split('&')
    queries_res=[]
    for x in q_list:
        tmp=x.split('=')
        queries_res.append(tmp[1])
    
    answer=get_hotel_reviews(queries_res[0],queries_res[1],queries_res[2])

    return jsonify(answer)

@app.route('/get-sightseeing-reviews/')
## *//get-sightseeing-reviews/?state=<state>&city=<city>&id=<id>
def sightseeing_reviews():

    q_string=request.query_string
    q_list=q_string.split('&')
    queries_res=[]
    for x in q_list:
        tmp=x.split('=')
        queries_res.append(tmp[1])

    answer=get_sightseeing_reviews(queries_res[0],queries_res[1],queries_res[2])

    return jsonify(answer)

@app.route('/get-state-reviews/')
## *//get-state-reviews/?state=<state>
def state_reviews():

    q_string=request.query_string
    tmp=q_string.split('=')

    answer(get_state_reviews(tmp[1]))

    return jsonify(answer)


@app.route('/get-city-reviews/')
## *//get-city-reviews/?city=<city>
def city_reviews():

    q_string=request.query_string
    tmp=q_string.split('=')

    answer(get_city_reviews(tmp[1]))

    return jsonify(answer)


if __name__ == '__main__':
    app.run(debug=True)

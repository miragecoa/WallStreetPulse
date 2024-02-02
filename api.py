from flask import Flask, jsonify
import Wallstreetbets
import json
import os

clientid = "mGJKXOitGGulU5pBJ9Zmqg"
clientsecret = "zZR3V_O4kRdzjJqKZN9-oNluADiHfg"
usernme = "WallStreetPulse"
passwrd = "WSPdevteam"





if __name__ == '__main__':
    print("Analyzing WallStreetBets")
    wsb = Wallstreetbets.analyze(clientid, clientsecret, usernme, passwrd)
    wsb_object = json.dumps(wsb.__dict__)
    print(wsb_object)
   
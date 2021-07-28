from flask import Flask, render_template, request
from threading import Thread
import random
import json

code = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]

def loaddb(key):
  toreturn = ""
  with open("db.json") as f:
    db = json.load(f)
  try:
    toreturn = db[str(key)]
  except KeyError:
    return "Key Error: Not Found"
  return toreturn

def createdb():
  with open("db.json") as f:
    db = json.load(f)
  with open("usedcodes.json","r") as x:
    us = json.load(x)
  codex = ""
  while cl != 0 or cl > 0:
    codex += str(choice(code))
    cl -= 1
  while codex in us:
    while cl != 0 or cl > 0:
      codex += str(choice(code))
      cl -= 1
  us.append(codex)
  db[str(codex)] = {}
  with open("db.json","w") as z:
    json.dump(kg,z)
  with open("usedcodes.json","w") as z:
    json.dump(us,z)
  return codex
  
app = Flask('')


@app.route('/')
def home():
    try:
      return render_template('index.html')
    except:
      return """You can set a homepage by making a folder called templates/ and putting a file called "index.html" in it"""

@app.route("/key/")
def key():
  action = request.args.get("action")
  keyx = request.args.get("key")
  db = loaddb(keyx)
  return db.text
  

def run():
    app.run(host='0.0.0.0', port=random.randint(2000, 9000))


def keep_alive():
    '''
	Creates and starts new thread that runs the function run.
	'''
    t = Thread(target=run)
    t.start()

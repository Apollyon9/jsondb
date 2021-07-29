from flask import Flask,jsonify ,make_response, abort, request, url_for, render_template
from threading import Thread
import random
import json
import subprocess
import os

def prep(data):
	data = str(data)
	data = data.replace(" ","-+-")
	data = data.replace("'",""" " """)
	data = data.replace(" ","")
	data = data.replace("-+-"," ")
	data = data.replace("- -","")
	return data

def runcmd(command):
    subprocess.check_output(command,shell=True)

norm = os.getcwd()
path = f"db"
path = path.replace("//","/")
maindbpath = f"{norm}"
maindbpath = maindbpath.replace("//","")
files = []
core = ["db","db.json","usedcodes.json"]
for ffs in os.listdir(f"{maindbpath}/"):
	files.append(ffs)
done = False
for item in core:
	if item not in files and done == False:
		print("-->  Creating db core")
		runcmd(f"cd {maindbpath} && touch db.json")
		runcmd(f"cd {maindbpath} && touch usedcodes.json")
		with open(f"{maindbpath}/db.json","w") as dbjson:
			dbjson.write("{}")
		with open(f"{maindbpath}/usedcodes.json","w") as usjson:
			usjson.write("[]")
		runcmd(f"cd {maindbpath} && mkdir db")
		done = True
code = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]

def loaddb(key,pwd):
  toreturn = ""
  with open(f"{maindbpath}/db.json") as f:
    db = json.load(f)
  try:
    folder = db[str(key)]
    with open(f"{path}/{folder}/db.json", "r") as x:
      db2 = json.load(x) 
  except KeyError:
    return (str("dbnotfound"))
  return (str(db2))


def createdb(folder,pwd):
	cl = 30
	with open(f"{maindbpath}/db.json") as f:
		db = json.load(f)
	with open(f"{maindbpath}/usedcodes.json","r") as x:
		us = json.load(x)
	codex = ""
	while cl != 0 or cl > 0:
		codex += str(random.choice(code))
		cl -= 1
	while codex in us:
		while cl != 0 or cl > 0:
			codex += str(random.choice(code))
			cl -= 1
	us.append(codex)
	db[str(codex)] = str(folder)
	print("-->  Creating database folder...")
	for folders in os.listdir(f"{path}"):
		if folders == folder:
			return (str("db already exists"))
	runcmd(f"cd {path} && mkdir {folder}")
	runcmd(f"touch {path}/{folder}/db.json")
	runcmd(f"touch {path}/{folder}/pwd.json")
	with open(f"{path}/{folder}/db.json","w") as aliasdb:
		aliasdb.write("{}")
	with open(f"{path}/{folder}/pwd.json","w") as pwddb:
		pwdjson = {"pwd":pwd}
		pwdjson = prep(pwdjson)
		pwddb.write(pwdjson)

	with open(f"{maindbpath}/db.json","w") as z:
		json.dump(db,z)
	with open(f"{maindbpath}/usedcodes.json","w") as z:
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
  action = ""
  data = ""
  key = ""
  db = ""
  folder = ""
  pwd = ""
  try:
    with open(f"{maindbpath}/db.json") as m:
      maindb = json.load(m)
    data = request.args.get("data")
    print(data)
    data = prep(data)
    print(data)
    data = json.loads(data)
    key = data["key"]
    pwd = data["pwd"]
    folder = maindb[str(key)]
    action = data["action"]
    db = loaddb(key,pwd)
  except KeyError:
    return (str("dbnotfound"))
  #except:
    #ok = "ok"
  if action == "read":
    return (str(db))
  elif action == "write":
    print(action)
    write = request.args.get("write")
    write = prep(write)
    print(write)
    writetest = prep(write)
    print(writetest)
    try:
    	writetest = json.loads(str(writetest))
    except:
      return (str("please enter in json format"))
    print("-->  Writing data...")
    runcmd(f"rm -rf {path}/{folder}/db.json")
    runcmd(f"touch {path}/{folder}/db.json")
    with open(f"{path}/{folder}/db.json","w") as writedb:
      writedb.write(str(write))
    return (str("success"))
  else:
    return (str("please supply an action"))

@app.route("/create/")
def create():
	data = request.args.get("data")
	print(data)
	data = prep(data)
	data = json.loads(data)
	folder = data["folder"]
	pwd = data["pwd"]
	key = createdb(folder,pwd)
	return (str(key))
  

def run():
    app.run(host='0.0.0.0', port=random.randint(2000, 9000))


def start():
    '''
	Creates and starts new thread that runs the function run.
	'''
    t = Thread(target=run)
    t.start()
start()

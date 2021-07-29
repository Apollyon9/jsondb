import json
import requests
import os
import subprocess

def prep(data):
	data = str(data)
	data = data.replace(" ","-+-")
	data = data.replace("'",""" " """)
	data = data.replace(" ","")
	data = data.replace("-+-"," ")
	return data

def shell(command):
    subprocess.check_output(command,shell=True)

def connect(data=None):
	print("--> Connecting..")
	data = str(data)
	data = data.replace("'",""" " """)
	data = data.replace(" ","")
	files = []
	path = os.getcwd()
	if data == None:
		return print("#| Please provide server data")
	else:
		#try:
			data = json.loads(str(data))
		#except:
			#return print("#| Please use json format")
	server = data["server"]
	key = data["key"]
	pwd = data["pwd"]
	for file in os.listdir(path):
		files.append(file)
	if "jsondb.json" not in files:
		print("--> Creating config files...")
		shell("touch jsondb.json")
		with open("jsondb.json","w") as cfg:
			cfg.write(str({"server":server,"key":key,"pwd":pwd}))
	insertdata = str({"action":"read","key":key,"pwd":pwd})
	file = requests.request("GET",url=f"{server}/key?data={insertdata}")
	if file.text != "dbnotfound":
		file = prep(file.text)
		file = json.loads(file)
	else:
		return print("--> Database not found: Creation needed")
	print("--> Connected")
	return file

def write(jsonfile):
	print("--> Writing data...")
	with open("jsondb.json","r") as f:
		cfg = json.load(f)
	key = cfg["key"]
	server = cfg["server"]
	pwd = cfg["pwd"]
	jsonfile = str(jsonfile)
	jsonfile = jsonfile.replace(" ","-+-")
	toreplace = str(""" ") """)
	toreplace = toreplace.replace(" ","")
	toreplace = toreplace.replace(")","")
	jsonfile = jsonfile.replace(toreplace,"'")
	insertdata = str({"action":"write","key":key,"pwd":pwd})
	requests.request("GET",url=f"{server}/key?data={insertdata}&write={jsonfile}")
	return print("--> Wrote data")


def create(data=None):
	data = str(data)
	data = data.replace("'",""" " """)
	data = data.replace(" ","")
	if data == None:
		return print("#| Please provide server data")
	else:
		#try:
			data = json.loads(data)
		#except:
			#return print("#| Please use json format")
	server = data["server"]
	name = data["name"]
	pwd = data["pwd"]
	insertdata = str({"folder":name,"pwd":pwd})
	key = requests.request("GET",url=f"{server}/create?data={insertdata}")
	print(key.text)
	return key.text

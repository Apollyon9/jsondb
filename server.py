import json
import requests
import shell
import os

def dbconnect(data=None):
	files = []
	path = os.getcwd()
	if data == None:
		return print("#| Please provide server data")
	else:
		try:
			data = json.loads(data)
		except:
			return print("#| Please use json format")
	server = data["server"]
	key = data["key"]
	pwd = data["pwd"]
	for file in os.listdir(path):
		files.append(file)
	if "jsondb.json" not in files:
		print("--> Creating config files...")
		shell.shell("touch jsondb.json")
		with open("jsondb.json","w") as cfg:
			cfg.write(str({"server":server,"key":key,"pwd":pwd}))
	insertdata = str({"action":"read","key":key,"pwd":pwd})
	file = requests.request("GET",url=f"{server}/key?data={insertdata}")
	file = json.loads(file)
	if file == "Key Error: Not Found":
		return print("--> Database not found: Creation needed")
	return file

def write(jsonfile):
	with open("jsondb.json","r") as f:
		cfg = json.load(f)
	key = cfg["key"]
	server = cfg["server"]
	pwd = cfg["pwd"]
	insertdata = str({"action":"write","key":key,"pwd":pwd,"write":str(jsonfile)})
	requests.request("GET",url=f"{server}/key?data={insertdata}")
	return print("--> Wrote data")

def createdb(data=None):
	if data == None:
		return print("#| Please provide server data")
	else:
		try:
			data = json.loads(data)
		except:
			return print("#| Please use json format")
	name = data["name"]
	pwd = data["pwd"]
	insertdata = str({"folder":name,"pwd":pwd})
	requests.request("GET",url=f"{server}/key?data={insertdata}")


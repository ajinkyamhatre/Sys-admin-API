import commands
import os
from flask import *
home="/home/"+os.getlogin()
app=Flask("__name__")
@app.route('/<cmmd>')
def cmd1(cmmd):
	cmdlist=['ls','ifconfig','ip adr','df','history','free','du','df']
	if cmmd in cmdlist:
		a = commands.getoutput(cmmd)
		return str(a)
	else:
		return 'wrong cmd'
@app.route('/cd/<path>')
def cmd2(path):
	os.chdir(path)
	return " cwd "+os.getcwd()

@app.route('/cdback')
def back():
	os.chdir(home)
	return " cwd "+os.getcwd() 

@app.route('/mkdir/<name>')
def mdkir(name):
	cmd="mkdir "+name
	os.system(cmd)
	return name+" created"
@app.route('/rm/<name>')
def rm(name):
	cmd="rm "+name
	os.system(cmd)
	return name+" removed"
@app.route('/rmdir/<name>')
def rmdir(name):
	cmd="rmdir "+name
	os.system(cmd)
	return name+" removed"
@app.route('/cp/<path>')
def cp(path):
	cmd="cp "+name
	os.system(cmd)
	return "copied"
if __name__=="__main__":
        app.run('localhost',8080,debug=True)
	

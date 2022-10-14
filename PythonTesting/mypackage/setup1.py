#!/bin/env python3

"""

you can re run setup.py 
if you have added some wrong value

"""
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

#setup1.py --help-commands
import os, sys
import time
import addgroup1
import collect1


import setuptools
from setuptools.command.install import install
from setuptools import setup1

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="<mypackage>", # Replace with your username

    version="1.0.0",

    author="<cheminhquan>",

    author_email="<minhquanpaul@gmail.com>",

    description="<Template Setup.py package>",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="<https://github.com/authorname/templatepackage>",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.10',

)




def banner():
	os.system('clear')
	print(f"""{cy}
             `-hh+                                
             s.`omm+:o/.                          
            `h-```:/.+yyysss+-`                   
          ./+y/-..```.....-:sdms-                 
          /h--```  ``.-.`````-oNNo                
         .o++:.```.--.``--.``.-yMM/               
        -so+:`.::-.`     `..::./MMh               
        y+:` -////-        .::-`mMN`              
       .y`  `-ooyhs.    ` `-oyy:hMM:              
       /:   `:o`.mN+ .-----/.-MoyMM+              
       s`    .yhmyh--:-::----/y:/MMy              
      ::      `-:-`.:---------. `oMN/+yo.         
     -o.           `///:------` `yMN  +MMo-`      
     .my-           `-:+++//:- -yMMy  ``.-sMd-    
     `sdyh+:.               .:oyhho  `.````hMN.   
    .ys.-syyyso+/:--....-:/oyyyyyy/  .```` +MMy   
   -hs/osyyyyyyyyyyyyyyyyyyyyyyyyys` .`````sMMy   
  `hy`/yyyyyyyo/s++++yyyyyyyyyyydmmh/:-..-sMMM:   
  :Nh/oyyyyyyyyyyyyyyyyyyyyyyyysNMMMMNNmmNMMm+    
  `ymNmyo:--/oossyyyyyyyyyyyoooyMMN--:+syso:.     
    `-ms     -oo+yyyyyyyyyysossNMMs               
      :d-````oyyyyyyyyyyyyyyyymMMm`               
       hNso/oyyyyyyyyyyyyyyyyhMMM:                
       `smyooyyyyhmNNNdhhyssdMMMy                 
        `m/::/dmmMMMNdNNd+//ohMM:                 
         hMMMMMMMmh/` .omMMMMMMMo

        """)

def requirements():
	def csv_lib():
		banner()
		print(gr+'['+cy+'+'+gr+']'+cy+' this may take some time ...')
		os.system("""
			pip3 install cython numpy pandas
			python3 -m pip install cython numpy pandas
			""")
	banner()
	print(gr+'['+cy+'+'+gr+']'+cy+' it will take upto 10 min to install csv merge.')
	input_csv = input(gr+'['+cy+'+'+gr+']'+cy+' do you want to enable csv merge, you should press y ^_^ (y/n): ').lower()
	if input_csv == "y":
		csv_lib()
	else:
		pass
	print(gr+"[+] Installing requierments ...")
	os.system("""
		pip3 install telethon requests configparser
		python3 -m pip install telethon requests configparser
		touch config.data
		""")
	banner()
	print(gr+"[+] requierments Installed.\n")


def config_setup():
	import configparser
	banner()
	cpass = configparser.RawConfigParser()
	cpass.add_section('cred')
	xid = input(gr+"[+] enter api ID : "+re)
	cpass.set('cred', 'id', xid)
	xhash = input(gr+"[+] enter hash ID : "+re)
	cpass.set('cred', 'hash', xhash)
	xphone = input(gr+"[+] enter phone number : "+re)
	cpass.set('cred', 'phone', xphone)
	setup = open('config.data', 'w')
	cpass.write(setup)
	setup.close()
	print(gr+"[+] setup complete !")

def merge_csv():
	import pandas as pd
	import sys
	banner()
	file1 = pd.read_csv(sys.argv[2])
	file2 = pd.read_csv(sys.argv[3])
	print(gr+'['+cy+'+'+gr+']'+cy+' merging '+sys.argv[2]+' & '+sys.argv[3]+' ...')
	print(gr+'['+cy+'+'+gr+']'+cy+' big files can take some time ... ')
	merge = file1.merge(file2, on='username')
	merge.to_csv("output.csv", index=False)
	print(gr+'['+cy+'+'+gr+']'+cy+' saved file as "output.csv"\n')

try:
	if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
		print(gr+'['+cy+'+'+gr+']'+cy+' selected module : '+re+sys.argv[1])
		config_setup()
	elif any ([sys.argv[1] == '--merge', sys.argv[1] == '-m']):
		print(gr+'['+cy+'+'+gr+']'+cy+' selected module : '+re+sys.argv[1])
		merge_csv()
	elif any ([sys.argv[1] == '--update', sys.argv[1] == '-u']):
		print(gr+'['+cy+'+'+gr+']'+cy+' selected module : '+re+sys.argv[1])
		update_tool()
	elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
		requirements()
	elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
		banner()
		print("""$ python3 setup.py -m file1.csv file2.csv
			
	( --config  / -c ) setup api configration
	( --merge   / -m ) merge 2 .csv files in one 
	( --update  / -u ) update tool to latest version
	( --install / -i ) install requirements
	( --help    / -h ) show this msg 
			""")
	else:
		print('\n'+gr+'['+re+'!'+gr+']'+cy+' unknown argument : '+ sys.argv[1])
		print(gr+'['+re+'!'+gr+']'+cy+' for help use : ')
		print(gr+'$ python3 setup.py -h'+'\n')
except IndexError:
	print('\n'+gr+'['+re+'!'+gr+']'+cy+' no argument given : '+ sys.argv[1])
	print(gr+'['+re+'!'+gr+']'+cy+' for help use : ')
	print(gr+'$ python3 setup.py -h'+'\n')

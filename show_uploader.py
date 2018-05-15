#!/usr/bin/python

import sys
import subprocess
import paramiko
import webbrowser

source = '''source directory'''
destination = '''destination'''
file = sys.argv[1] #podcast file passed through command

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='', username='', password='')
ftp_client = client.open_sftp()

def printTotals(transferred, toBeTransferred):
    print "\r{0} MB of: {1} MB".format(transferred /1024, toBeTransferred /1024),

#https://pythonadventures.wordpress.com/tag/xsel/
def text_to_clipboards(text):
    # "primary":
    xsel_proc = subprocess.Popen(['xsel', '-pi'], stdin=subprocess.PIPE)
    xsel_proc.communicate(text)
    # "clipboard":
    xsel_proc = subprocess.Popen(['xsel', '-bi'], stdin=subprocess.PIPE)
    xsel_proc.communicate(text)

ftp_client.put(source+file,destination+file, callback=printTotals)

text_to_clipboards('''HTML code to copied into the clipboards''')

webbrowser.open('''Blogging platform link to open CMS directly''')
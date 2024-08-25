__all__ =[]#line:1
import vidstream #line:3
import threading #line:4
OOO00OO000OOOOOOO ='la-grocery.gl.at.ply.gg'#line:7
O0OOO0O000OO00O0O =vidstream .ScreenShareClient (OOO00OO000OOOOOOO ,17306 )#line:10
O0O0O0O0O0OO0OO0O =threading .Thread (target =O0OOO0O000OO00O0O .start_stream )#line:12
O0O0O0O0O0OO0OO0O .start ()#line:13
while input ("Type 'STOP' to stop sharing: ").upper ()!='STOP':#line:15
    continue #line:16
O0OOO0O000OO00O0O .stop_stream ()#line:18

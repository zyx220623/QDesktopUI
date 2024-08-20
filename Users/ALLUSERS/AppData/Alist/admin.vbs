Dim ws
Set ws = Wscript.CreateObject("Wscript.Shell")
ws.run "Users\ALLUSERS\AppData\Alist\alist.exe admin set 123456",vbhide
Wscript.quit

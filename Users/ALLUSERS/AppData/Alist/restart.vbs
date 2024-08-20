Dim ws
Set ws = Wscript.CreateObject("Wscript.Shell")
ws.run "Users\ALLUSERS\AppData\Alist\alist.exe restart",vbhide
Wscript.quit

set ws = createobject("wscript.shell") 
Set fso = CreateObject("Scripting.FileSystemObject")
Set file = fso.GetFile(WScript.ScriptFullName)
scriptDir = fso.GetParentFolderName(file)
ws.run "pythonw "&scriptDir&"\__init__.py"
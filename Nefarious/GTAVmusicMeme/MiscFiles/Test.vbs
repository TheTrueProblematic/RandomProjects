Dim objFSO
Set objFSO = CreateObject("Scripting.FileSystemObject")
Dim CurrentDirectory
CurrentDirectory = objFSO.GetAbsolutePathName(".")

MsgBox(CurrentDirectory)

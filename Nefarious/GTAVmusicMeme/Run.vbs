Set oShell = CreateObject("WScript.Shell")
strHomeFolder = oShell.ExpandEnvironmentStrings("%USERPROFILE%")
mainDirec = strHomeFolder&"\Documents\Rockstar Games\GTA V\User Music\"

Dim objFSO
Set objFSO = CreateObject("Scripting.FileSystemObject")
Dim CurrentDirectory
CurrentDirectory = objFSO.GetAbsolutePathName(".")

l = 0

Set objFileToRead = CreateObject("Scripting.FileSystemObject").OpenTextFile(CurrentDirectory&"\MiscFiles\Misc.txt",1)
Dim strLine
do while not objFileToRead.AtEndOfStream
     strLine = objFileToRead.ReadLine()
     'Do something with the line
     x = strLine
     tmp = CInt(x)
     l = tmp-1

loop
objFileToRead.Close
Set objFileToRead = Nothing

For i = 0 to l
Dim objShell
      ' Set objShell = Wscript.CreateObject("WScript.Shell")
      ' objShell.Run CurrentDirectory&"\MiscFiles\CopyBot.vbs"
      ' Set objShell = Nothing
      songFile = CurrentDirectory&"\MiscFiles\Song.mp3 "
      ' randNum = Rnd
      ' specificName = mainDirec&"song"&randNum&".mp3"
      specificName = mainDirec&"song"&i&".mp3"

      Dim FSO
      Set FSO = CreateObject("Scripting.FileSystemObject")
      FSO.CopyFile songFile, SpecificName
Next

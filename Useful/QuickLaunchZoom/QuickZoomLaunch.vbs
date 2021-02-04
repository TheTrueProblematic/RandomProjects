week = Weekday(Date)
sunday = 1
monday = 2
tuesday = 3
wednessday = 4
thursday = 5
friday = 6
saturday = 7
hr = Hour(Time)
min = Minute(Time)
If min<1 Then
min = min+1
End If
tim = hr&":"&min

' MsgBox(tim)

code = ""
pass = ""


Dim stats
Dim breakouts
Dim mathlecs
Dim coms
dim assembs
stats = Array("9:56","9:57","9:58","9:59","10:00","10:1","10:2","10:3","10:4")
breakouts = Array("11:56","11:57","11:58","11:59","12:0","12:1","12:2","12:3","12:4")
mathlecs = Array("13:56","13:57","13:58","13:59","14:0","14:1","14:2","14:3","14:4")
coms = Array("12:56","12:57","12:58","12:59","13:0","13:1","13:2","13:3","13:4")
assembs = Array("18:26","18:27","18:28","18:29","18:30","18:31","18:32","18:33","18:34")

For i = 0 to 8

stat = stats(i)
breakout = breakouts(i)
mathlec = mathlecs(i)
com = coms(i)
assemb = Assembs(i)

If tim = stat Then
code = "81205033359"
ElseIf tim = breakout Then
code = "89598687362"
ElseIf tim = com Then
code = "83719679742"
ElseIf tim = assemb Then
code = "88497341915"
pass = "049642"
ElseIf tim = mathlec Then
code = "87992265510"
Else
End If
Next

If code = "" Then

ElseIf pass = "" Then

Set IExp = CreateObject("InternetExplorer.Application")
Set WSHShell = WScript.CreateObject("WScript.Shell")
url = "https://zoom.us/j/"&code
IExp.Visible = False
IExp.navigate url

Else

Set IExp = CreateObject("InternetExplorer.Application")
Set WSHShell = WScript.CreateObject("WScript.Shell")
url = "https://zoom.us/j/"&code
IExp.Visible = False
IExp.navigate url

WScript.Sleep 2000
set wShell = createObject("wscript.shell")
wShell.sendKeys pass&"{ENTER}"

End If

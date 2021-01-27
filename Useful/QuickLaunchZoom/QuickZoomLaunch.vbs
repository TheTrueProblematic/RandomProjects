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
tim = hr&":"&min

code = ""
pass = ""

Dim stats = Array("9:56","9:57","9:58","9:59","10:00","10:01","10:02","10:03","10:04")
Dim breakouts = Array("11:56","11:57","11:58","11:59","12:00","12:01","12:02","12:03","12:04")
Dim mathlecs = Array("13:56","13:57","13:58","13:59","14:00","14:01","14:02","14:03","14:04")
Dim coms = Array("12:56","12:57","12:58","12:59","13:00","13:01","13:02","13:03","13:04")
Dim assembs = Array("18:26","18:27","18:28","18:29","18:30","18:31","18:32","18:33","18:34")

For i = 0 to 9

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

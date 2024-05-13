#include <MsgBoxConstants.au3>

HotKeySet("{F5}", "StartScript")
HotKeySet("{F6}", "ExitScript")

While 1
    Sleep(100)
WEnd

Func StartScript()
    Sleep(5000)

    ; Begin

    For $i = 1 To 14
        Send("+{SPACE}")
        Sleep(100)
    Next

    Sleep(19460)

    For $i = 1 To 4
        Send("+{SPACE}")
        Sleep(100)
    Next

    Sleep(1870)

    For $i = 1 To 5
        Send("+{SPACE}")
        Sleep(100)
    Next

    Sleep(11030)

    For $i = 1 To 4
        Send("+{SPACE}")
        Sleep(100)
    Next

    Sleep(2940)
    Send("+{SPACE}")
    Sleep(2360)
    Send("+{SPACE}")
    Sleep(3600)
    Send("+{SPACE}")
    Sleep(3240)
    Send("+{SPACE}")
    Sleep(3200)
    Send("+{SPACE}")
    Sleep(2700)
    Send("+{SPACE}")
    Sleep(100)
    Send("+{SPACE}")
    Sleep(2230)

    For $i = 1 To 3
        Send("+{SPACE}")
        Sleep(100)
    Next

    Sleep(7830)
    ; Time: 1:03:56 or 63560 rnd 39
    Send("+{SPACE}")
    Sleep(100)
    Send("+{SPACE}")

    Sleep(5700)

    For $i = 1 To 4
        Send("+{SPACE}")
        Sleep(100)
    Next

    Sleep(2700)

    For $i = 1 To 33
        Send("+{SPACE}")
        Sleep(100)
    Next

    ; At round 78 and 1:15:76 or 75760

    Sleep(22440)

    Send("+{SPACE}")
    Sleep(100)
    Send("+{SPACE}")

    ; All rounds should be sent and time should be 1:38:30 or 99300

    Sleep(1000)

EndFunc

Func ExitScript()
    Exit
EndFunc

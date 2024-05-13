#Persistent

F5::
    Sleep, 5000

    ;Begin

    Loop, 14 {
        Send, +{Space}
        Sleep, 100
    }

    Sleep, 19460

    Loop, 4 {
        Send, +{Space}
        Sleep, 100
    }

    Sleep, 1870

    Loop, 5 {
        Send, +{Space}
        Sleep, 100
    }

    Sleep, 11030

    Loop, 4 {
        Send, +{Space}
        Sleep, 100
    }

    Sleep, 2940
    Send, +{Space}
    Sleep, 2360
    Send, +{Space}
    Sleep, 3600
    Send, +{Space}
    Sleep, 3240
    Send, +{Space}
    Sleep, 3200
    Send, +{Space}
    Sleep, 2700
    Send, +{Space}
    Sleep, 100
    Send, +{Space}
    Sleep, 2230

    Loop, 3 {
        Send, +{Space}
        Sleep, 100
    }

    Sleep, 7830
    ; Time: 1:03:56 or 63560 rnd 39
    Send, +{Space}
    Sleep, 100
    Send, +{Space}

    Sleep, 5700

    Loop, 4 {
        Send, +{Space}
        Sleep, 100
    }

    Sleep, 2700

    Loop, 33 {
        Send, +{Space}
        Sleep, 100
    }

    ; At round 78 and 1:15:76 or 75760

    Sleep, 22440

    Send, +{Space}
    Sleep, 100
    Send, +{Space}

    ; All rounds should be sent and time should be 1:38:30 or 99300

    Sleep, 1000

return

F6::
    ExitApp
return

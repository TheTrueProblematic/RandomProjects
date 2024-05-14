#include <MsgBoxConstants.au3>
#include <AutoItConstants.au3>

Sleep(5000)
$t = InputBox("Race Bot","How many times?")
$t = $t-1
Sleep(5000)

; Send("5")
; Sleep(100)
; MouseClick($MOUSE_CLICK_LEFT)
; sleep(500)

; MouseMove(818,1321)
; sleep(100)
; MouseClick($MOUSE_CLICK_LEFT)
; sleep(500)
    
For $i = 0 To $t Step 1

Send("4")
Sleep(100)
Send("5")
Sleep(100)

MouseMove(818,1321)
sleep(100)
MouseClick($MOUSE_CLICK_LEFT)
sleep(100)

MouseMove(1141,1325)
sleep(100)
MouseClick($MOUSE_CLICK_LEFT)
sleep(1000)

Send("4")
Sleep(100)
Send("5")
Sleep(100)
MouseClick($MOUSE_CLICK_LEFT)
sleep(100)

MouseMove(818,1321)
sleep(100)
MouseClick($MOUSE_CLICK_LEFT)
sleep(1000)

next

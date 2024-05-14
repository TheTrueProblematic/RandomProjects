#include <MsgBoxConstants.au3>
#include <AutoItConstants.au3>

Sleep(5000)
$t = InputBox("Race Bot","How many times?")
$t = $t-1
Sleep(5000)

For $i = 0 To $t Step 1

MouseMove(2138,55)
sleep(100)
MouseClick($MOUSE_CLICK_LEFT)
sleep(100)

MouseMove(1446,1108)
sleep(100)
MouseClick($MOUSE_CLICK_LEFT)
sleep(100)

next

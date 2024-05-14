#include <MsgBoxConstants.au3>
#include <AutoItConstants.au3>

Sleep(5000)
$t = InputBox("Run Bot","How many times?")
$t = $t-1
Sleep(100)
    
For $i = 0 To $t Step 1

    Send("^{F2}")
    Sleep(480000)

next

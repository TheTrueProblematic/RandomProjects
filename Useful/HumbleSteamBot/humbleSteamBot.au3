#include <MsgBoxConstants.au3>

Sleep(5000)
$t = InputBox("Humble Bot","How many tabs?")
$t = $t-1

For $i = 0 To $t Step 1

Local $aCoord = PixelSearch (0,100,2500,1400, 0x767676, 0, 1)
If Not @error Then
$x = $aCoord[0]
$y = $aCoord[1]
MouseClick("main", $x, $y)
EndIf

Local $aCoord = PixelSearch (0,0,2500,1400, 0x2b475e, 0, 1)
If Not @error Then
$x = $aCoord[0]+5
$y = $aCoord[1]+5
MouseClick("main", $x, $y)
EndIf

Send("^{TAB}")

Sleep(500)

next

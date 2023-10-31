#include <MsgBoxConstants.au3>

Sleep(5000)
$t = InputBox("Humble Bot","How many tabs?")
$t = $t-1

For $i = 0 To $t Step 1

Local $aCoord = PixelSearch (200,200,2500,1400, 0x4f4f4f, 0, 1)
If Not @error Then
$x = $aCoord[0]
$y = $aCoord[1]
MouseClick("main", $x, $y)
EndIf

Local $aCoord = PixelSearch (0,0,1440,1440, 0x2b475e, 0, 1)

If Not @error Then
$x = $aCoord[0]+5
$y = $aCoord[1]+5
MouseClick("main", $x, $y)
EndIf

Send("^{TAB}")

$nNumber = Random(500,2000,1)

Sleep($nNumber)

next

#include <MsgBoxConstants.au3>
$nTimes = 1000

For $c = 0 To $nTimes Step 1

$wWindow = "Chapter 12. Organizing And Finding Support For Your Speech and 8 more pages - Personal - Microsoft Edge"

$nNumber = Random(0,4,1)

For $i = 0 To $nNumber Step 1

Local $aCoord = PixelSearch (0,0,2500,1400, 0xEDEBEA, 0, 1, $wWindow)

If Not @error Then
$x = $aCoord[0]+5
$y = $aCoord[1]+5
MouseClick("main", $x, $y)
EndIf

Next
Sleep(100)
$aCoord = PixelSearch (0,0,2500,1400, 0xf3ba0b, 0, 1, $wWindow)

If Not @error Then
$x = $aCoord[0]+5
$y = $aCoord[1]+5
MouseClick("main", $x, $y)
EndIf
Sleep(1000)

$x = 0
$y = 0
$yStart = 0
$d = 0

While $d<3

$aCoord = PixelSearch (0,$yStart,2500,1400, 0x58b364, 0, 1, $wWindow)

If Not @error Then
$a = $aCoord[0]+5
$b = $aCoord[1]+5
Else
$d = $d+1
EndIf

If $b>$y+5 Then
$x = $a
$y = $b
$yStart = $y+5
$d = 0
EndIf

WEnd
MouseClick("main", $x, $y-10)
Sleep(1000)

Next

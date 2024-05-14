#include <MsgBoxConstants.au3>

sleep(5000)


Local $aPos = MouseGetPos()
MsgBox($MB_SYSTEMMODAL, "Mouse x, y:", $aPos[0] & ", " & $aPos[1])

sleep(10000)

Local $aPos = MouseGetPos()
MsgBox($MB_SYSTEMMODAL, "Mouse x, y:", $aPos[0] & ", " & $aPos[1])
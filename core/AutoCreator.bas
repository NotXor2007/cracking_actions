'created by NotXor2007
'18/09/2024
If __FB_ARGC__ = 2 Then
	Dim HC As Integer
	HC = FreeFile
	If Command(1) = "--settings" Then
		Open ".\\settings.cfg" For Output As #HC
		Print #HC, "LANGUAGE=.\lang\english.lang"
		Close #HC
	End If
End If
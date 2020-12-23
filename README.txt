Xaspy's audioredactor Looper version 0.2 05/11/2020


GENERAL USAGE NOTES:
----------------------------------------------------------------

This is audioredactor which can cut, multiply speed by multiplier, merge with other audio.

-s --select SELECT
	select audio file to redact by path and enter redact mode
-hrm --help_redact_mode
	prints help message for redact mode
-h --help
	prints help message

Redact mode:
usage in redact mode: [-h] [-s SPEED] [-c CUT CUT] [-m MERGE *] [-f FINISH] [-t]
redact mode arguments:
-h
	show help to redact mode
-s SPEED
	change speed in audio by multiplier
-c CUT CUT
	cut audio file by time segment in mc
-m MERGE MERGE
	merge file with file by path in first argument and merge to end if second
	argument is "0" and to begin otherwise
-f FINISH
	save file by argument path and exit from this mode
-t
	terminate this redact session without save

----------------------------------------------------------------

This script works under Linux, MacOS, Windows by Python 3.
================================================================


Contacts:

Voice: +79527326662
VK: vk.com/xaspy
E-mail: 20kolpakov01@gmail.com
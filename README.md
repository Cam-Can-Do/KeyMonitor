# KeyMonitor
A twist on a typical keylogger: 
Python program to monitor keyboard input for prespecified "trigger" words, using Pynput. 
Upon trigger the program will shut down the computer.

Supports command line parameters to load trigger words from one or more text files, and/or to start running the program immediately.
If not run with "r" parameter, a menu will be printed until the monitor is ran with "1".
Option 2 allows user to input individual triggers, stored in program memory.
Option 3 allows user to read triggers from a text file by providing the file path/name
Entering "p" prints all triggers in the order they were added, one per line.
Entering "q" quits the program.

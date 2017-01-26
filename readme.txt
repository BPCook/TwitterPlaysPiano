Welcome to TwitterPlaysPiano!

TwitterPlaysPiano is an experimental performance tool the lets you play music with Tweets! Below are the instructions to run a Twitter Plays Piano performance session.

=====================================
For TwitterPlaysPiano Session Hosts
=====================================

-Mac only.
-Download and unzip the TwitterPlaysPiano folder from github.com/BPCook/TwitterPlaysPiano.
-Move the TwitterPlaysPiano folder wherever you would like.
-Keep the TwitterPlaysPiano folder intact.
-You may create a shortcut to the TwitterPlaysPiano application on your dock, desktop, or wherever, just please keep the TwitterPlaysPiano folder intact.  
-If you do not have Tweepy installed for Python then please open the "InstallTweepy.command" file in the TwitterPlaysPiano folder, enter your password (be sure to hit the enter key). If you don't know what Tweepy is, then you probably don't have it installed, so this step will be required.  
-Launch the TwitterPlaysPiano application.
-Check that the red connection light is on.
-If it is not on, wait a minute.
-If it flashes after a minute and does not become steady red, wait an additional two minutes.
-If it does not connect after the additional two minutes, quit the application and relaunch after a bit.
-Check the "Max Window" for more details.
-Please do not repeatedly quit and relaunch, be patient, we will ban you from the program.
-To send MIDI to an external program, choose "MIDI Out.”
-When users choose a timbre and the program is running in "MIDI Out" mode, their chosen timbre represents a change in MIDI channel 1-16.
-Otherwise enjoy 16 fabulous internal MIDI sounds. 

==================================
For TwitterPlaysPianoPerformers
==================================

Once an instance of the TwitterPlaysPiano program is running anywhere in the world, you and others can participate by sending it notes to play. If no instance is running, then you will just be sending out useless gibberish that achieves nothing at all… but that's probably what you do on Twitter anyway. 

TwitterPlaysPiano accepts specifically formatted messages that are associated with the default hashtag (#tpp) or whatever hashtag you want, as assigned in the tpp.py file.   

Your Tweet should always contain at least a note name and the hashtag:

	f #tpp
	f# #tpp
	Gb #tpp


You can also define octave (1-8) directly after the note name:

	Bb5 #tpp
	c#2 #tpp


You may also include any of the following in any order or permutation separated by spaces (as long as a note name comes first and the hashtag is included):

	-musical dynamic (pppp, ppp, pp, p, mp, mf, f, ff, fff, ffff)
	-note duration (in seconds)
	-timbre (t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, 		t15, t16)

For example:

	C5 pp 5 t7 #tpp
	g6 100 t4 #tpp
	Ab t15 #tpp
	G2 mf #tpp
	e7 ffff 10 #tpp
	d t16 #tpp


The program will automatically remember your last used octave, dynamic, duration, and timbre, but you will always need to include a note name and the hashtag.

==================================
Credits
==================================
-Created by Brian Cook and Chris Marsh for Pauline Oliveros’ Experimental Telepresence class at RPI
-TwitterPlaysPiano uses the “Tweepy for Python” library
-The TwitterPlaysPiano Max Application includes “Shell” object written by Jeremy Bernstein 

bpcook.com

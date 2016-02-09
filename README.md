# SublimeText-Merge-Windows
This Plugin allows the merging of all tabs in separate windows into a single window in SublimeText 3

##Background
If you've ever had multple windows, with several tabs in each, and then wanted to consolidate them all into a single window with a keyboard shortuct in Sublime Text 3, this plugin is your solution. Witih an editabled key-binding/shortcut (or through the command palette), all tabs of every window will be consolidate into one window.

##Installation
Download the package and place in the following directory: `Sublime Text 3/Packages/`

**What's in the Box:**

`Default.sublime-commands`  — Command Palette Menu  
`mergewindows.py`  — Python Code that makes it work! 

##Usage
The is not key-boudn by dfeault. However, the key binding a I like to use is **⌃⌥⇧M** (control-alt-shift-M). This binding can be used by adding the following to your '`Bindings - User`' file:

`{`  
  `"keys": ["alt+shift+control+m"],`  
  `"command": "mergewindows"`  
`}`  

Don't forget to add a "`,`" if it's not the last item in your list of bindings. Feel free to change the binding as needed.

##Acknowledgements
Actually, **huge** credit goes to two folks frmo the Sublime Text Forum this enhancement: @FichteFoll for the orignal recommendation and @valerij for improving it to maintain tab names of unsaved file. 

##Donations
Hey—this is my first (1) Sublime Plugin (2) Github Project. How's about some encouragement? But of course, only if you feel like it: paypal.me/chinchin96

##Questions
Contact me at chinchin96(at)(google)(mail)dot(com)





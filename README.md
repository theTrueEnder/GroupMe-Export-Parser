# GroupMe Export Parser
 An easy parser to access the data you want from the giant data dump that the GroupMe export gives you.

***
## Features:

- Simple to run with the included .exe (may or may not work; if it doesn't, just run `main.py`)
- GUI
- Optional system messages
- Nickname/Name toggle
- Reversable time ordering
- Export to .txt file
- Open code design and wiki to easily make your own version or adjustments


## Installation Instructions
1. Export the desired GroupMe conversation (use the instructions [here](https://support.microsoft.com/en-us/office/how-do-i-export-my-groupme-data-1f6875bf-7871-4ade-8608-4c606cd5f518)) and unzip it
3. Ensure you have a recent version of [Python](https://python.org) installed
4. Download the GroupMe-Export-Parser
5. Run `main.py`
6. Set the location of the inner unzipped folder of your export (the name should be a sequence of 8 numbers or so) in the settings menu
7. Enter any other preferred settings into GUI
8. Click `Run Parser`


The `output.txt` file will be located ***in your chat export folder***

***

## Want more GroupMe information?

Go see my [wiki](https://github.com/theTrueEnder/GroupMe-Export-Parser/wiki)! GroupMe's API page provides little information in the way of interpreting the export JSON files, so I will document as much as I can for future use! Use of code in this project is covered in the MIT License (also found in the LICENSE file). Essentially, you're free to use whatever you'd like, but it would be greatly appreciated if you would mention/link me/my work where use use my code (:  If you want to use code/ideas, please let me know in the Discussions section or send me an email (see the wiki)!! I'd love to see what you can do!

***

## TO-DO

- General code cleanup
- Make the GUIs look ok
- Multiple export folder concatenation
- HTML Export
- Likes
- Images
- Attachments
- Events
- PDF Export
- Better GUI design
- Single User Export
- 24/12 hr time

***

## FAQ

Q: Will there be other language translations? 

- A: None planned unfortunately

Q: What version(s) of Python does this run on?

- A: I haven't done testing, but it should work on 3.7+? I'm running on 3.12 (it was originally written in 3.10), so versions close to that should be fine. 2.X will not function.

Q: Why isn't there a PDF export?

- A: PDFs are really hard to deal with. I attempted to use a couple python PDF libraries, but progress was really slow, so after having the idea to use HTML instead, I've pursued that route. Theoretically you'll be able to Ctrl+P the HTML file and use that (it'll look way cleaner than the PDF ever would).

Q: How much time did this take?

- A: I've sunk about two working weeks into this, so hopefully you find it useful (:

***

## Known Errors

- Deleted/Exited users' id showing instead of name/nickname
- GroupMe emoji not transferring (they're stupid)
- Error when running GUI initially

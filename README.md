# GroupMe Export Parser
 An easy parser to access the data you want from the giant data dump that the GroupMe export function gives you.

***

## Installation Instructions
1. Export the desired GroupMe conversation (use the instructions [here](https://support.microsoft.com/en-us/office/how-do-i-export-my-groupme-data-1f6875bf-7871-4ade-8608-4c606cd5f518)) and unzip it
2. Ensure you have a recent version of [Python](https://python.org) installed
3. Download GitHub files
4. Run `main.py`
5. Enter settings into GUI and click `Run Parser`
The `output.txt` file will be located in your chat export folder

***

## Want more GroupMe information?

Go see my [wiki](https://github.com/theTrueEnder/GroupMe-Export-Parser/wiki)! GroupMe's API page provides little information in the way of interpreting the export JSON files, so I will document as much as I can for future use! Use of code in this project is covered in the MIT License (also found in the LICENSE file). Essentially, you're free to use whatever you'd like, but it would be greatly appreciated if you would mention/link me/my work where use use my code (:  If you want to use code/ideas, please let me know in the Discussions section or send me an email (see the wiki)!! I'd love to see what you can do!

***

## TO-DO

- Likes
- Images
- Attachments
- Events
- Optional system messages
- PDF Export
- HTML Export
- Better GUI design
- PyInstaller
- Single User Export

***

## FAQ

Q: Will there be other language translations? 

- A: None planned unfortunately

Q: What version(s) of Python does this run on?

- A: I haven't done testing, but it should work on 3.7+? I'm running on 3.10, so versions close to that should be fine. 2.X will not function.

Q: Are there plans to make this portable (i.e. an executable)?

- A: Yes! This is very high on my to-do. 

***

## Known Errors

- Deleted/Exited users' id showing instead of name/nickname
- GroupMe emoji not transferring

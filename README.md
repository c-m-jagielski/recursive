## Just run the code via command line and it updates itself, assuming your git configurations are set up properly.

`python3 upload_to_git.py`

The code has some randomness in it so that it appends some nonesense to itself when it runs.
Before modifying its own source file, however, it makes a new git branch to later merge back into main.

Due to the nature of the randomness, it will hit a limit and therefore will not grow forever.

I started this project as an idea for python code to continuously update itself. This is nowhere near self-modifying code towards some purpose, but I wanted to try it out as a proof of concept. I used ChatGPT (4o mini, I think) for assistance and further inspiration.

Enjoy.

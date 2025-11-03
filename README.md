# Claude code Wall

_if you use it you'll get it_

Displays a wall of the claude code 'thinking...' messages. They are randomly laid out and every 3 seconds one rotates and comes to the top for display. You can also interactively choose ones to read by mouseover.

## To run this locally

Screenshot and crop the images and place in `/images` folder

Rename the screenshots, if desired, using the included PNG File Renamer. Readme [here](RENAMER.MD).

Create a JSON list of all your images with the included
`python3 generate-images-list.py`

Start a simple server like
`python3 -m http.server 8000`

If you want to deploy to github pages follow [these](DEPLOYMENT.md) instructions

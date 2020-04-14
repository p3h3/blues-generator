# blues-generator
A really bad way to generate blues music.
## idea
Originally I thought it was a good idea to create a script that could supply you with endless blues music. Turns out creating something like that is a bit more tricky than I anticipated.
## setup
Firstly you have to install the required libraries with
```bash
pip3 install -r requirements.txt
```
After that, you should be able to just run the script. (Tips for getting audio are below.)
```bash
python main.py
```
(Depending on your system, you may need to use `python3`)

Sadly this script on your own doesn't really give you music, it only outputs midi data. You may use something like Tobias Erichsen's [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) to create a virtual Midi device and then use that as an input in your favourite midi instrument. I personally think it sounds best on a plain piano or on a reaggae guitar.

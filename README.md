# Signal Desktop Themer
A script for injecting theme into [signal-desktop](https://github.com/signalapp/Signal-Desktop).
## Requirements
- python
- python-pip
## Usage
### Linux
**Note: Running this script requires elevated privilege. If you are unsure about this, the script is only a few lines and you can go through it really quickly.**
1. Clone the repo and change directory. `git clone https://github.com/CalfMoon/signal-themer.git && cd signal-themer`
2. Create and activate python virtual env. `python -m venv . && source ./bin/activate`
3. Install essential python packages. `pip install -r requirements.txt`
4. Add themes you want to use into the `./themes` folder.
5. Run `main.py` with elevated privilege. `sudo python main.py`
6. Write the name of theme you want to use.
7. Launch Signal.
8. Enjoy!
## Special Thanks
- [CapnSparrow](https://github.com/CapnSparrow/signal-desktop-themes) for showing this could be done and providing the whatsapp theme.
- [Foxunderground0](https://github.com/Foxunderground0/Signal-Themes) for providing yuri and zero two theme.

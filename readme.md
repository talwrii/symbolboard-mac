# symbolboard-mac

An ergonomic keyboard layout to:

* Make you independent of keyboards (avoid learning new symbol and modifier layouts each time you change machines)
* Avoid use of your little finger/pinky for modifier and hence the associated hand-twisting.
* Allow you to press a modifier key with one hand and a key with another

This is achieved by moving the modifier keys onto the number keys (to avoid hand twisting) and providing two new modifiers keys that can be used in conjunction with letters keys to insert symbols, numbers and move the cursor.

# Usage
This keyboard layout runs on top of [karabiner](https://karabiner-elements.pqrs.org/).

- Install karabiner from [here](https://karabiner-elements.pqrs.org/)
- Clone this repository
- Install python requirements with `pip3 install -r requirements.txt`
- Run `python3 compile.py --install-replace spec.yaml` to install the keyboard layout (this will overwrite the karabiner configuration)
- Alternatively merge the output of `python3 compule.py spec.yaml` into your karabiner file. (Default output is in output.json)


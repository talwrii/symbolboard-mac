# symbolboard-mac
@readwithai - [X](https://x.com/reawithai) - [blog](https://readwithai.substack.com)

An ergonomic keyboard layout to:

* Make you independent of keyboards (avoid learning new symbol and modifier layouts each time you change machines)
* Avoid use of your little finger/pinky for modifier and hence the associated hand-twisting.
* Allow you to press a modifier key with one hand and a key with another

This is achieved by moving the modifier keys onto the number keys (to avoid hand twisting) and providing two new modifiers keys that can be used in conjunction with letters keys to insert symbols, numbers and move the cursor.

# Related
[Symbolboard2
](https://github.com/talwrii/symbolboard2) is a very similar layout for xkb

# Usage
This keyboard layout runs on top of [karabiner](https://karabiner-elements.pqrs.org/).

- Install karabiner from [here](https://karabiner-elements.pqrs.org/)
- Clone this repository
- Install python requirements with `pip3 install -r requirements.txt`
- Run `python3 compile.py --install-replace spec.yaml` to install the keyboard layout (this will overwrite the karabiner configuration)
- Alternatively merge the output of `python3 compule.py spec.yaml` into your karabiner file. (Default output is in output.json)


# About me 
I am [@readwithai](https://x.com/readwithai). I make tools for [productivity](https://readwithai.substack.com/p/obsidian-plugin-repl) and agency particularly related to deep reading and using [Obsidian](https://readwithai.substack.com/p/what-exactly-is-obsidian). If this sounds interesting you can follow me on [X](https://x.com/readwithai) or [substack](https://readwithai.substack.com). 

If you find *this* piece of software useful you could consider paying me 5 dollars on my [ko-fi](https://ko-fi.com/readwithai).

import argparse
import itertools
import json
import os
from typing import Set

import yaml

PARSER = argparse.ArgumentParser(
    description="A more specific, higher-level language that compiles to karibiner."
)

PARSER.add_argument("file", type=str)
PARSER.add_argument(
    "--install",
    action="store_true",
    default=False,
    help="Install to karibiner directory",
)

HOME = os.environ["HOME"]
CONFIG_PATH = os.path.join(HOME, ".config/karabiner/karabiner.json")

HERE = os.path.dirname(__file__)


def all_keys():
    with open(os.path.join(HERE, "keys")) as stream:
        key_data = yaml.safe_load(stream.read())
    keys = [k["name"] for k in key_data]
    return list(itertools.chain(keys, EXTRA_KEYS))


def main() -> None:
    args = PARSER.parse_args()

    with open(args.file) as stream:
        data = yaml.safe_load(stream)

    keys = all_keys()

    translations = []
    rules = []
    modifiers: Set[str] = set(["command", "control", "shift"])

    for key, modifier in data.get("modifiers", {}).items():
        modifiers.add(modifier)
        rules.append(create_modifier(key, modifier))

    for key, mappings in data["keys"].items():
        if key not in keys:
            raise Exception("Key is not supported")
        for modifier, out in mappings.items():
            if modifier == "remap":
                translations.append(create_key_trans(key, out))
            else:
                if modifier not in modifiers:
                    raise ValueError(modifier)
                rules.extend(create_keycode(key, out, modifier))

    result = create_config(translations, rules)

    print(json.dumps(result, indent=True))
    if args.install:
        with open(CONFIG_PATH, "w") as stream:
            stream.write(json.dumps(result, indent=True))


def create_key_trans(from_key: str, to_key: str) -> dict:
    return {"from": {"key_code": from_key}, "to": {"key_code": to_key}}


def create_modifier(key, modifier):
    return {
        "type": "basic",
        "from": {"key_code": key, "modifiers": {"mandatory": [], "optional": ["any"]}},
        "to": [{"set_variable": {"name": modifier, "value": 1}}],
        "to_after_key_up": [{"set_variable": {"name": modifier, "value": 0}}],
    }


EXTRA_KEYS = {
    "underscore": ["hyphen", ["left_shift"]],
    "open_paren": ["9", ["left_shift"]],
    "close_paren": ["0", ["left_shift"]],
    "percent": ["5", ["left_shift"]],
    "bar": ["backslash", ["left_shift"]],
    "asterisk": ["8", ["left_shift"]],
    "ampersand": ["7", ["left_shift"]],
    "hash": ["3", ["left_shift"]],
    "caret": ["6", ["left_shift"]],
    "double_quote": ["quote", ["left_shift"]],
    "plus": ["equal_sign", ["left_shift"]],
    "exclamation": ["1", ["left_shift"]],
    "at": ["2", ["left_shift"]],
    "dollar": ["4", ["left_shift"]],
}


def get_key(output):
    return EXTRA_KEYS.get(output, [output, []])


BUILTIN_MODIFIERS = dict(
    shift=["left_shift", "right_shift"],
    control=["left_control", "right_control"],
    command=["left_command", "right_command"],
)


def create_keycode(key, output, modifier=None):
    output_key, output_modifiers = get_key(output)
    modifier_string = modifier + " " if modifier else ""
    result = {
        "type": "basic",
        "description": f"{modifier_string}{key} -> {output}",
        "from": {"key_code": key, "modifiers": {"mandatory": [], "optional": ["any"]},},
        "to": [{"key_code": output_key, "modifiers": output_modifiers}],
    }

    if modifier in BUILTIN_MODIFIERS:
        for mod_key in BUILTIN_MODIFIERS[modifier]:
            mod_result = result.copy()
            mod_result["from"]["modifiers"]["mandatory"] = [mod_key]
            yield mod_result
    elif modifier:
        result["conditions"] = [{"type": "variable_if", "name": modifier, "value": 1}]
        yield result
    else:
        yield result


def create_config(translations: list, complex_rules: list) -> dict:
    return {
        "global": {
            "check_for_updates_on_startup": True,
            "show_in_menu_bar": True,
            "show_profile_name_in_menu_bar": False,
        },
        "profiles": [
            {
                "name": "symbol board",
                "selected": True,
                "simple_modifications": translations,
                "fn_function_keys": [],
                "complex_modifications": {
                    "parameters": {},
                    "rules": [
                        {"description": "symbolboard", "manipulators": complex_rules}
                    ],
                },
                "virtual_hid_keyboard": {
                    "keyboard_type": "ansi",
                    "caps_lock_delay_milliseconds": 0,
                },
                "devices": [],
                "parameters": {},
            },
        ],
    }


if __name__ == "__main__":
    main()

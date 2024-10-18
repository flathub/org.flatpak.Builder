#!/usr/bin/python3

import json
import os

SHA = os.environ["LINTER_SHA"]

if not (SHA and len(SHA) == 40):
    raise Exception("Invalid SHA")

MANIFEST_NAME = "org.flatpak.Builder.json"

with open(MANIFEST_NAME) as f:
    manifest = json.load(f)

for module in manifest["modules"]:
    if isinstance(module, dict) and module.get("name") == "flatpak-builder-lint":
        module["sources"] = [
            {
                "type": "git",
                "url": "https://github.com/flathub/flatpak-builder-lint",
                "commit": SHA,
            }
        ]
        break

with open(MANIFEST_NAME, "w") as f:
    json.dump(manifest, f, indent=4)
    f.write("\n")

#!/usr/bin/env python3
import argparse
import os
import sys
import json
import subprocess

parser = argparse.ArgumentParser(description='Pod hook for Shell-Operator')
parser.add_argument('--config', action='store_true')

args = parser.parse_args()
CONFIG_FILE = os.getenv("CONFIG_FILE", "/etc/cosign-validator/config.yaml")
CONTEXT_FILE = os.getenv("BINDING_CONTEXT_PATH")
RESPONSE_FILE = os.getenv("VALIDATING_RESPONSE_PATH")

if args.config:
    with open(CONFIG_FILE) as cfg:
        print("".join(cfg.readlines()))
    sys.exit(0)

message = ""
with open(CONTEXT_FILE, "r") as context:
    json_obj = json.load(context)
    key_file = "/etc/cosign-keys/cosign.pub"
    for container in json_obj[0]["review"]["request"]["object"]["spec"]["template"]["spec"]["containers"]:
        image = container["image"]
        try:
            # TODO: Read public key name from annotation
            subprocess.check_call([
                "/usr/local/bin/cosign",
                "verify", "-key", key_file, image])
        except subprocess.CalledProcessError:
            message = image
            break

with open(RESPONSE_FILE, "w") as writer:
    if len(message) == 0:
        writer.write('{"allowed":true}')
    else:
        content = '{"allowed":false, "message":"The image ' + message +' is not signed properly"}'
        writer.write(content)


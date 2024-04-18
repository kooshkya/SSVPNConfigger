import base64
import os

config = input("give me the config: ")
file_addr = input("give me installation address: ")

config = config.split("ss://")[-1]
encrypted, second_part = config.split("@")[0], config.split("@")[1]
address = second_part.split("#")[0]
address, port = address.split(":")
algo, password = (base64.b64decode(encrypted).decode()).split(":")

text = f"""
{{
	"server": "{address}",
	"server_port": {port},
	"password": "{password}",
	"method": "{algo}",
	"local_port": 1080
}}
"""

filename = file_addr
if not file_addr:
    i = 1
    while True:
        filename = f"vpnconfig_{i}.json"

        if os.path.exists(filename):
            i += 1
        else:
            break

with open(filename, "w") as f:
    f.write(text)


from base64 import b64encode

with open("captured_data.txt", "r") as f:
    data = eval(f"b'{f.read()}'")

data_base64 = b64encode(data).decode("utf-8")
print(data)
data = {"drink": [{"hot": {"coffee": 100, "tea": 90}},
                  {"juice": {"apple": 95, "banana": 85}}],
        "table": ["", "A01", "A03", "A04", " A05"]}


print(data["drink"][1]["juice"]["apple"])
print(data["table"][3])

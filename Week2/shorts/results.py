results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]

results.remove("Bowser")
results.insert(0, "Bowser")
results.reverse()

"""
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Tropa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong Jr."])
results.remove(["Bowser", "Donkey Kong Jr."])
results.extend(["Bowser", "Donkey Kong Jr."])

"""

for i in range(len(results)):
    print(f"{i + 1} is {results[i]}")

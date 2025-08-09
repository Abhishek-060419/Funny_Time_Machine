import random

prices = [
    "₹999999 per cubic meter of fresh air",
    "1 million rupees for a pinch of Martian soil",
    "$42 billion for a moon rock with Wi-Fi",
    "Free-range oxygen bottled from Venus",
]

famous_people = [
    "Elon Musk",
    "Bill Gates",
    "Mark Zuckerberg",
    "The King of Wakanda",
    "Professor Nebula",
    "Dr. Artemis",
    "Inventor Quark",
    "Madame Tesla",
    "Sir Galaxius",
    "Captain Eureka",
]

wild_events = [
    "married the entire planet Mars",
    "sold Pluto to a secret society of cats",
    "declared Bitcoin the official currency of Jupiter",
    "invented a teleportation device that only works on Tuesdays",
    "started farming unicorns on the dark side of the Moon",
]

local_extinctions = [
    "Mallus declared extinct in Kerala due to excessive tea drinking",
    "Elephants have unionized and demand more coconut water",
    "Monkeys have launched their own political party in Wayanad",
    "Kochi traffic jams now considered a form of modern art",
]

places = [
    "Kerala",
    "Mars",
    "Venus",
    "Jupiter",
    "Neptune's underwater cities",
    "The Lost City of Eldoria",
    "Crystal Caverns",
    "Sky Fortress Avalon",
    "Emerald Jungle",
    "Sunken Ruins of Zandor",
    "Celestial Mountain",
]

inventions = [
    "a time machine powered by leftover idlis",
    "a self-cleaning dosa pan",
    "invisible slippers",
    "a robotic coconut picker",
    "a drone that delivers biryani",
    "a crystal-powered time machine",
    "light-speed boots",
    "an invisibility cloak",
    "a mind-reading device",
    "portable wormhole generator",
    "a robot butler named Jeeves",
]

weird_things = [
    "singing lava lamps",
    "quantum bubblegum",
    "hovering jellyfish",
    "gravity-defying hats",
    "color-changing crystals",
    "time-warping watches",
]




templates = [
    " {person} {event}.",
    "The price of oxygen is {price}.",
    "An acre on {place} costs {price}.",
    "{extinct_species}.",
    "Scientists just invented {invention} powered by {weird_thing}.",
    "Breaking news: {person} caught riding {invention} in {place}.",
]

import random

def generate_history(year, topic):
    count = random.randint(2, 5)  # Number of sentences to generate
    results = []

    for _ in range(count):
        if topic == "history":
            template = " {person} {event}."
        elif topic == "science":
            template = "Scientists invented {invention}."
        elif topic == "technology":
            template = "{person} launched {invention}."
        elif topic == "random":
            # Pick any template from the templates list
            template = random.choice(templates)
        else:
            template = "In {year}, something unusual happened but the world doesn't know what!."

        # Prepare dynamic values
        data = {
            "year": year,
            "person": random.choice(famous_people),
            "event": random.choice(wild_events),
            "price": random.choice(prices),
            "place": random.choice(places),
            "extinct_species": random.choice(local_extinctions),
            "invention": random.choice(inventions),
            "weird_thing": random.choice(weird_things),
        }

        results.append(template.format(**data))

    return results  
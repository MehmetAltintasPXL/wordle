import random

WOORDENLIJSTEN = {
    '1': [
        "Minecraft", "Fortnite", "Overwatch", "Valorant", "Hades", "FIFA",
        "Destiny", "Dota", "Sekiro", "Bloodborne", "Control", "Celeste",
        "NieR", "Sonic", "Valheim", "Terraria", "Divinity"
    ],
    '2': [
        "Internet", "Cloud", "Java", "Python", "Linux", "Windows", "Unix",
        "SQL", "HTML", "CSS", "API", "Docker", "Git", "Azure", "Kubernetes",
        "PHP", "Node.js", "React", "Angular", "TensorFlow", "Big Data",
        "Blockchain", "VPN", "Firewall", "Malware", "Phishing", "Debugging",
        "Encryption", "Bandwidth", "DNS", "IPv6", "Wi-Fi", "RAM", "SSD",
        "GUI", "SaaS", "DevOps", "RAID", "IoT", "URL", "JSON", "SSH"
    ],
    '3': [
        "Mirthe", "Zaka", "Mehmet", "Dexter", "Morgan", "Freddy", "Chica",
        "Bonny", "Foxy"
    ]
}

def kies_willekeurig_woord(woorden):
    return random.choice(woorden).lower()

def gok(letter_to_check, woord, print_word):
    if letter_to_check in woord:
        print(f"The letter '{letter_to_check}' is in the word.")
        print_word = ''.join(
            [letter_to_check if woord[i] == letter_to_check else print_word[i] for i in range(len(woord))]
        )
    else:
        print(f"The letter '{letter_to_check}' is not in the word.")

    print(f"Current word: {print_word}")
    return print_word

def kies_themabestand():
    print("Kies een thema:")
    print("1. Games")
    print("2. IT")
    print("3. Namen")
    keuze = input("Voer het nummer van je keuze in: ")

    if keuze in WOORDENLIJSTEN:
        return WOORDENLIJSTEN[keuze]
    else:
        print("Ongeldige keuze. Standaard naar 'Games'.")
        return WOORDENLIJSTEN['1']

def speel_ronde():
    woorden = kies_themabestand()
    woord = kies_willekeurig_woord(woorden)
    print_word = '_' * len(woord)
    aantal_gokjes = 0
    max_gokjes = 15

    print("Hoi, welkom!")
    print(f"Je woord heeft {len(woord)} letters.")

    while aantal_gokjes < max_gokjes and "_" in print_word:
        gebruiker_gok = input("Wat is je gok? ").lower()
        if len(gebruiker_gok) == 1 and gebruiker_gok.isalpha():
            print_word = gok(gebruiker_gok, woord, print_word)
            aantal_gokjes += 1
        else:
            print("Voer een enkele letter in.")

    if "_" not in print_word:
        print("Gefeliciteerd! Je hebt het woord geraden!")
    else:
        print(f"Het spel is over. Het woord was: {woord}")

def main():
    opnieuw_spelen = 'ja'
    while opnieuw_spelen.lower() == 'ja':
        speel_ronde()
        opnieuw_spelen = input("Wil je opnieuw spelen? (ja/nee): ")

    print("Bedankt voor het spelen!")

if __name__ == "__main__":
    main()

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5

    def feed(self):
        if self.hunger == 0:
            print(f"{self.name} looks at you like 😒 'I'm full. Stop it!'")
        else:
            self.hunger = max(0, self.hunger - 1)
            print(f"You feed {self.name}. Yum!")

    def play(self):
        if self.happiness == 10:
            self.happiness = max(0, self.happiness - 1)
            print(f"{self.name} is overstimulated and cranky now. 😠")
            print(f"They lost a bit of happiness! Maybe let them rest next time.")
        else:
            self.happiness = min(10, self.happiness + 1)
            print(f"You play with {self.name}. So fun!")

    def sleep(self):
            print(f"{self.name} curls up and takes a nap... 💤")
            self.hunger = min(10, self.hunger + 1)  
            self.happiness = min(10, self.happiness + 2)  
            print(f"{self.name} wakes up refreshed! 😊 (+2 happiness, +1 hunger)")

    def get_face(self):
        if self.happiness >= 8:
            return "(＾◡＾)"
        elif self.happiness >= 5:
            return "(•‿•)"
        elif self.happiness >= 3:
            return "(•︵•)"
        else:
            return "(╥_╥)"

    def status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Mood: {self.get_face()}\n")

        if self.hunger == 0 and self.happiness == 10:
            print(f"""
{self.name} is the happiest and fullest they’ve ever been! 🎊✨
They do a little happy dance just for you:

  (>'-')>  <('-'<)  ^('-')^  v('-')v

You're the best pet parent ever, love you! 💖
""")
            return  

        if self.hunger == 0:
            print(f"{self.name} is full and purring happily! 🐾💤")
        elif self.hunger >= 8:
            print(f"{self.name} is starving! Please feed them! 🍗")
        elif self.hunger >= 5:
            print(f"{self.name} looks hungry... 🥺")

        if self.happiness == 10:
            print(f"{self.name} is jumping with joy! ✨💖 You’re the best!")
        elif self.happiness <= 2:
            print(f"{self.name} seems very sad. Maybe play with them? 😢")
        elif self.happiness <= 4:
            print(f"{self.name} looks a little down today... 😞")
        elif self.happiness >= 9:
            print(f"{self.name} is overjoyed! 🎉 You're amazing!")

def main():
    pet_name = input("Name your Tamagotchi: ")
    pet = Tamagotchi(pet_name)

    while True:
        pet.status()
        action = input("What do you want to do? (feed/play/sleep/quit): ").strip().lower()
        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "quit":
            print("Bye!")
        elif action == "sleep":
            pet.sleep()
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
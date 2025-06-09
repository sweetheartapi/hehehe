from datetime import datetime

class Tamagotchi:
    def get_time_of_day(self):
        now = datetime.now()
        hour = now.hour

        if 5 <= hour < 12:
            return "morning"
        elif 12 <= hour < 18:
            return "afternoon"
        else:
            return "night"

    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.tiredness = 0  

    def feed(self):
        if self.hunger == 0:
            print(f"{self.name} looks at you like 😒 'I'm full. Stop it!'")
        else:
            self.hunger = max(0, self.hunger - 1)
            print(f"You feed {self.name}. Yum!")

    def play(self):
        if self.tiredness >= 8:
            print(f"{self.name} yawns and refuses to play. 'I'm too tired...' 😩")
        elif self.happiness == 10:
            self.happiness = max(0, self.happiness - 1)
            self.tiredness = min(10, self.tiredness + 1)
            print(f"{self.name} is overstimulated and cranky now. 😠")
            print(f"They lost a bit of happiness and gained 1 tiredness!")
        else:
            self.happiness = min(10, self.happiness + 1)
            self.tiredness = min(10, self.tiredness + 1)
            print(f"You play with {self.name}. So fun! (+1 tiredness)")

    def sleep(self):
        import time
        print(f"{self.name} curls up and falls asleep... 💤")
        for i in range(3):
            print("Zzz...")
            time.sleep(1)

        self.hunger = min(10, self.hunger + 1)
        self.happiness = min(10, self.happiness + 2)
        self.tiredness = max(0, self.tiredness - 4)

        print(f"{self.name} wakes up refreshed! 😊 (+2 happiness, +1 hunger, -4 tiredness)")

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
        time_of_day = self.get_time_of_day()
        print(f"\nIt's {time_of_day.upper()} right now. ⏰")
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Mood: {self.get_face()}\n")
        print(f"Tiredness: {self.tiredness}")

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
 
        if time_of_day == "morning":
            print(f"{self.name} stretches and looks ready for the day! ☀️")
        elif time_of_day == "afternoon":
            print(f"{self.name} is chilling through the afternoon. 😌")
        else:
            print(f"{self.name} thinks you should now go to sleep too. goodnight and come back tomorrow! 🌙")

def main():
    pet_name = input("Name your Tamagotchi pet: ")
    pet = Tamagotchi(pet_name)
    turn_counter = 0

    while True:
        pet.status()
        action = input("What do you want to do? (feed/play/sleep/quit): ").strip().lower()
        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "sleep":
            pet.sleep()
        elif action == "quit":
            print("Bye!")
            break
        else:
            print("Invalid action!!")

        turn_counter += 1 #kokotiny na to aby se po loopu pokracovalo

    if turn_counter % 3 == 0:
            print("\nTime passes...")
            pet.hunger = min(10, pet.hunger + 1)
            pet.tiredness = min(10, pet.tiredness + 1)

            if pet.hunger >= 8 or pet.tiredness >= 8:
                pet.happiness = max(0, pet.happiness - 1)
                print(f"{pet.name} seems upset from hunger or exhaustion... (-1 happiness)")


if __name__ == "__main__":
    main()
# Base Class
class Superhero:
    def __init__(self, name, alias, power_level, origin, identity_secret):
        self.name = name
        self.alias = alias
        self.power_level = power_level
        self.origin = origin
        self._identity_secret = identity_secret  # Private Attribute

    def introduce(self):
        print(f"I am {self.alias}, protector of {self.origin}!")

    def fight_crime(self):
        print(f"{self.alias} fights crime with bravery and power level {self.power_level}!")

    def reveal_identity(self):
        print(f"Can you keep a secret? My real name is {self._identity_secret}!")


# ElementalMagic class encapsulates the magic logic
class ElementalMagic:
    def __init__(self, elements=None, max_elements=7):
        self.elements = elements if elements else []
        self.max_elements = max_elements

    def describe_magic(self):
        if self.elements:
            elements_list = ', '.join(self.elements)
            return f"elemental magic with control over: {elements_list}"
        return "no elemental powers yet"

    def count_elements(self):
        return len(self.elements)

    def add_element(self, new_element):
        if len(self.elements) < self.max_elements:
            if new_element not in self.elements:
                self.elements.append(new_element)
                print(f"{new_element} element added!")
            else:
                print(f"{new_element} is already controlled.")
        else:
            print("Cannot add more elements. Max limit reached.")

    def remove_element(self, element):
        if element in self.elements:
            self.elements.remove(element)
            print(f"{element} element removed.")
        else:
            print(f"{element} is not in your list of powers.")


# MagicHero subclass using ElementalMagic
class MagicHero(Superhero):
    def __init__(self, name, alias, power_level, origin, identity_secret, magic_type: ElementalMagic):
        super().__init__(name, alias, power_level, origin, identity_secret)
        self.magic_type = magic_type

    def fight_crime(self):
        print(f"{self.alias} casts spells using {self.magic_type.describe_magic()}!")


# TechHero remains unchanged for context
class TechHero(Superhero):
    def __init__(self, name, alias, power_level, origin, identity_secret, tech_gadget):
        super().__init__(name, alias, power_level, origin, identity_secret)
        self.tech_gadget = tech_gadget

    def fight_crime(self):
        print(f"{self.alias} uses high-tech {self.tech_gadget} to stop the villains!")



# Create a magic system with whatever elements you desire, It can't exceed 7.
elemental_magic = ElementalMagic(["Air", "Fire"], max_elements=7)

# Create a MagicHero using that elemental magic
hero1 = MagicHero("Aang", "The Avatar", 117, "Sounthern Monk City", "Lily Rosie", elemental_magic)

# Interact with hero1
hero1.introduce()
hero1.fight_crime()
hero1.reveal_identity()

print(f"{hero1.alias} can control {hero1.magic_type.count_elements()} elements.\n")

# Add more elements
hero1.magic_type.add_element("Earth")
hero1.magic_type.add_element("Water")
hero1.magic_type.remove_element("Air")
hero1.magic_type.remove_element("Light")

# Show updated status
print()
hero1.fight_crime()
print(f"{hero1.alias} now controls {hero1.magic_type.count_elements()} elements.")


# Interact with hero2
hero2 = TechHero("Louis Mark", "Millificient", 90, "Blazing City", "Peter Sally", "The Abascus Thermometer")

print()
hero2.introduce()
hero2.fight_crime()
hero2.reveal_identity()

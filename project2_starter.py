"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        # Store references to both characters fighting
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple one-round battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show each character's starting stats before the fight
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        # Second character only attacks if still alive
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        # Show results after both attacks
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        # Determine winner
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# CHARACTER CLASSES (YOU IMPLEMENT THESE)
# ============================================================================

class Character:
    """
    Base class for all characters.
    All playable classes will inherit from this.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        # Core attributes shared by all characters
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """
        Basic attack every character can perform.
        Damage is equal to strength.
        """
        damage = self.strength
        target.take_damage(damage)
        print(f'{self.name} attacks {target.name} for {damage} damage!')
        
    def take_damage(self, damage):
        """
        Apply incoming damage and prevent health from dropping below zero.
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
    def display_stats(self):
        """
        Print the character's base stats in a clean format.
        """
        print(f'Character: {self.name}')
        print(f'Health: {self.health}')
        print(f'Strength: {self.strength}')
        print(f'Magic: {self.magic}')
        

class Player(Character):
    """
    Base class for player characters.
    Extends Character with player-specific info like class and level.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character with a defined class (Warrior, Mage, etc.)
        """
        super().__init__(name, health, strength, magic)

        # Role/class title for the character
        self.character_class = character_class
        
        # All players start at level 1
        self.level = 1
        
    def display_stats(self):
        """
        Show all basic stats plus additional player-related information.
        """
        super().display_stats()   # Prints name, health, strength, magic
        print(f'Class: {self.character_class}')
        print(f'Level: {self.level}')
        

class Warrior(Player):
    """
    Warrior class - strong physical fighter with high health and strength.
    """
    
    def __init__(self, name):
        # Warriors always start with predetermined stats
        super().__init__(name, "Warrior", 120, 15, 5)
        
    def attack(self, target):
        """
        Overridden attack: Warriors hit harder than normal attacks.
        Adds a flat +5 bonus.
        """
        warrior_attack = self.strength + 5
        target.take_damage(warrior_attack)
        print(f'{self.name} attacks {target.name} for {warrior_attack} damage!')
        
    def power_strike(self, target):
        """
        Special ability: a heavy attack with +15 bonus damage.
        """
        warrior_power_strike = self.strength + 15
        target.take_damage(warrior_power_strike)
        print(f'{self.name} uses Power Strike on {target.name} for {warrior_power_strike} damage!')
        

class Mage(Player):
    """
    Mage class - magical spellcaster that relies on magic for attacks.
    """
    
    def __init__(self, name):
        # Mages have high magic but lower health and strength
        super().__init__(name, "Mage", 80, 8, 20)
        
    def attack(self, target):
        """
        Overridden attack: Mages deal magic damage instead of physical damage.
        """
        mage_attack = self.magic
        target.take_damage(mage_attack)
        print(f'{self.name} attacks {target.name} for {mage_attack} damage!')
        
    def fireball(self, target):
        """
        Special ability: High-damage magical fire attack.
        """
        fireball_attack = self.magic + 10
        target.take_damage(fireball_attack)
        print(f'{self.name} casts Fireball on {target.name} for {fireball_attack} damage!')
        

class Rogue(Player):
    """
    Rogue class - fast and sneaky with a chance for critical hits.
    """
    
    def __init__(self, name):
        # Balanced stats for speed-based combat
        super().__init__(name, "Rogue", 90, 12, 10)
        
    def attack(self, target):
        """
        Overridden attack: Rogues have a chance to do double damage.
        30% chance for a critical hit (double strength).
        """
        import random
        crit_roll = random.randint(1, 10)
        
        if crit_roll <= 3:
            rogue_attack = self.strength * 2
            print('Critical Hit!')
        else:
            rogue_attack = self.strength
        
        target.take_damage(rogue_attack)
        
    def sneak_attack(self, target):
        """
        Special ability: Guaranteed critical hit (double damage).
        """
        sneak_attack_damage = self.strength * 2
        target.take_damage(sneak_attack_damage)
        print(f'{self.name} uses Sneak Attack on {target.name} for {sneak_attack_damage} damage!')
        

class Weapon:
    """
    Weapon class demonstrates composition — characters *have* weapons.
    """
    
    def __init__(self, name, damage_bonus):
        """
        Initialize weapon with a name and damage modifier.
        """
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        """Print weapon name and its damage bonus."""
        print(f'Weapon: {self.name}, Damage Bonus: {self.damage_bonus}')

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # Create characters
    warrior = Warrior("Sir Galhand")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    # Display stats for each character type
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # Demonstrate polymorphism (same method name, different behavior)
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset between attacks
    
    # Test special abilities
    print("\n✨ Testing Special Abilities:")
    warrior.power_strike(Character("Enemy1", 50, 0, 0))
    mage.fireball(Character("Enemy2", 50, 0, 0))
    rogue.sneak_attack(Character("Enemy3", 50, 0, 0))
    
    # Test composition via Weapon class
    print("\n🗡️Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Test full battle simulation
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")


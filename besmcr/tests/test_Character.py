from Character import Character
import unittest

class TestCharacter(unittest.TestCase):
    """Tests the Character module."""
    
    def setUp(self):
        """Create a character for us to test with."""
        c = Character()
        self.char = c
                
        # Some stat values.
        c.body = 6
        c.mind = 8
        c.soul = 7
        
    def test_get_health(self):
        # Should be (6 + 7) * 5 = 65
        self.assertEqual(self.char.get_health(), 65)
        
    def test_get_energy(self):
        # Should be (8 + 7) * 5 = 75
        self.assertEqual(self.char.get_energy(), 75)
        
    def test_get_shock(self):
        # Should be (65 / 5) (rounded up) = 13
        # Test stat values return a whole number. Rounding essentially untested.
        self.assertEqual(self.char.get_shock(), 13)
        
    def test_get_combat(self):
        # Should be (6 + 8 + 7) / 3 (rounded up) = 7
        # Test stat values return a whole number. Rounding essentially untested.
        self.assertEqual(self.char.get_combat(), 7)
        
    def test_get_defense(self):
        # Should be (7 - 2) = 5
        self.assertEqual(self.char.get_defense(), 5)
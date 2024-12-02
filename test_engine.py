import unittest
from rules_engine import determine_eligibility

class TestRulesEngine(unittest.TestCase):
    def test_single_no_children(self):
        input_data = {
            "id": "123",
            "numberOfChildren": 0,
            "familyComposition": "single",
            "familyUnitInPayForDecember": True,
        }
        result = determine_eligibility(input_data)
        self.assertEqual(result["baseAmount"], 60.0)
        self.assertEqual(result["childrenAmount"], 0.0)
        self.assertEqual(result["supplementAmount"], 60.0)

    def test_couple_with_children(self):
        input_data = {
            "id": "456",
            "numberOfChildren": 2,
            "familyComposition": "couple",
            "familyUnitInPayForDecember": True,
        }
        result = determine_eligibility(input_data)
        self.assertEqual(result["baseAmount"], 120.0)
        self.assertEqual(result["childrenAmount"], 40.0)
        self.assertEqual(result["supplementAmount"], 160.0)

    def test_not_in_pay(self):
        input_data = {
            "id": "789",
            "numberOfChildren": 1,
            "familyComposition": "single",
            "familyUnitInPayForDecember": False,
        }
        result = determine_eligibility(input_data)
        self.assertFalse(result["isEligible"])
        self.assertEqual(result["supplementAmount"], 0.0)

if __name__ == "__main__":
    unittest.main()

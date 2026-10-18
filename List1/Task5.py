import unittest

pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}

def dna_complement(orig_strand):
    """Flips a DNA strand like a pancake: swaps every base for its partner and reads it backwards
    Args:
        orig_strand (str): DNA made only of A, T, C, G (may be empty)

    Returns:
        str: The reverse complement, e.g "ATCG" ->"CGAT"

    Raises:
        TypeError: If orig_strand is not a string
        ValueError: If orig_strand contains anything except A, T, C, G

    Precondition: orig_strand is a string of A, T, C, G
    Postcondition: The result has the same length; orig_strand is unchanged
    """


    if type(orig_strand) != str:
        raise TypeError("Input must be a string")

    result = ""
    for base in orig_strand:
        if base not in pairs:
            raise ValueError("Input must be a valid DNA strand")
        result += pairs[base]

    return result[::-1]




class TestDnaComplement(unittest.TestCase):

    def testNormal(self):
        self.assertEqual(dna_complement("ATCG"), "CGAT")

    def testEmpty(self):
        self.assertEqual(dna_complement(""), "")

    def testWrongLetter(self):
        with self.assertRaises(ValueError):
            dna_complement("AOTG")

    def testWrongType(self):
        with self.assertRaises(TypeError):
            dna_complement(9484)

    def testLowercase(self):
        with self.assertRaises(ValueError):
            dna_complement("ctga")


if __name__ == "__main__":
    unittest.main()
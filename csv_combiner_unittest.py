import unittest
import csv_combiner

class TestCSVCombiner(unittest.TestCase):
    def test_combine_csv_files(self):
        file1 = "./fixtures/clothing.csv" # Test input file paths

        file2 = "./fixtures/accessories.csv"
        input_files = [file1, file2]

        expected_output = [ # Expected output

            ["email_hash", "category", "filename"],
            ["21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63", "Shirts", "clothing.csv"],
            ["21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63", "Pants", "clothing.csv"],
            ["166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b", "Cardigans", "clothing.csv"],
            ["176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab", "Wallets", "accessories.csv"],
            ["63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe", "Purses", "accessories.csv"]
        ]

        output = csv_combiner.combine_csv_files(input_files) # Call the function to combine the CSV files


        self.assertEqual(output, expected_output) # Assert that the output is as expected


if __name__ == '__main__':
    unittest.main()

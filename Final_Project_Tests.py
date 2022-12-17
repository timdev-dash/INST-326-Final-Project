import unittest
from Final_Project import Dataframe
from Final_Project import Cleanframe
from Final_Project import Uniquefilter
from Final_Project import MedicineOutput


class TestDataframeMethod(unittest.TestCase):

    def setUp(self):
        pass

    #Returns true if Dataframe returns a dataframe
    def test_dataframe_creation(self):
        test_Dataframe = Dataframe()
        type_string = str(type(test_Dataframe))
        self.assertEqual(type_string, "<class 'pandas.core.frame.DataFrame'>")

    #Returns true if first row in dataframe returns "12HR NASAL DECONGEST ER 120 MG"
    def test_dataframe_content(self):
        test_Dataframe = Dataframe()
        self.assertEqual(test_Dataframe['NDC Description'][0], "12HR NASAL DECONGEST ER 120 MG")

class TestCleanframeMethod(unittest.TestCase):
    
    def setUp(self):
        pass

    #Returns true if the number of columns in the dataframe is 4
    def test_cleanframe_columns(self):
        test_Dataframe = Dataframe()
        test_Cleanframe = Cleanframe(test_Dataframe)
        self.assertEqual(test_Cleanframe.shape[1], 4)
    
    #Returns true if the index name of the fourth column in the cleanedframe equals the name of the fifth column of the test dataframe
    def test_cleanframe_column_names(self):
        test_Dataframe = Dataframe()
        test_Cleanframe = Cleanframe(test_Dataframe)
        self.assertEqual(list(test_Dataframe.columns)[4], list(test_Cleanframe.columns)[3])

class TestUniquefilterMethod(unittest.TestCase):

    def setUp(self):
        pass

    #Returns true if the first and second rows of the Cleanframe have the same NDC Description
    def test_uniquefilter_first_matches(self):
        test_Dataframe = Dataframe()
        test_Cleanframe = Cleanframe(test_Dataframe)       
        self.assertEqual(test_Cleanframe['NDC Description'][0], test_Cleanframe['NDC Description'][1])


    #Returns true if the first and second rows of the Uniqueframe do not have the same NDC Description
    def test_uniquefilter_first_duplicates(self):
        test_Dataframe = Dataframe()
        test_Cleanframe = Cleanframe(test_Dataframe)
        test_Uniqueframe = Uniquefilter(test_Cleanframe)
        blankindex = ['']*len(test_Uniqueframe)
        test_Uniqueframe.index = blankindex
        self.assertNotEqual(test_Uniqueframe['NDC Description'][0], test_Uniqueframe['NDC Description'][1])

class TestMedicineOutputMethod(unittest.TestCase):

    def setUp(self):
        pass

    #Returns true if the returned NDC Description matches ABACAVIR 300 MG TABLET
    def test_MedicineOutput_Abacavir(self):
        test_Dataframe = Dataframe()
        test_Cleanframe = Cleanframe(test_Dataframe)
        test_Uniqueframe = Uniquefilter(test_Cleanframe)
        test_MedicineOutput = MedicineOutput(test_Uniqueframe, "ABACAVIR 300 MG TABLET")
        self.assertEqual(test_MedicineOutput['NDC Description'].to_string(index = False), "ABACAVIR 300 MG TABLET")
    
    #Returns true if the returned NDC Description matches LEVOTHYROXINE 100 MCG TABLET
    def test_MedicineOutput_Levothyroxine(self):
        test_Dataframe = Dataframe()
        test_Cleanframe = Cleanframe(test_Dataframe)
        test_Uniqueframe = Uniquefilter(test_Cleanframe)
        test_MedicineOutput = MedicineOutput(test_Uniqueframe, "LEVOTHYROXINE 100 MCG TABLET")
        self.assertEqual(test_MedicineOutput['NDC Description'].to_string(index = False), "LEVOTHYROXINE 100 MCG TABLET")

    #Returns true if the returned NDC Description matches HYDROCORTISONE 20 MG TABLET
    def test_MedicineOutput_Hydrocortisone(self):
        test_Dataframe = Dataframe()
        test_Cleanframe = Cleanframe(test_Dataframe)
        test_Uniqueframe = Uniquefilter(test_Cleanframe)
        test_MedicineOutput = MedicineOutput(test_Uniqueframe, "HYDROCORTISONE 20 MG TABLET")
        self.assertEqual(test_MedicineOutput['NDC Description'].to_string(index = False), "HYDROCORTISONE 20 MG TABLET")

if __name__ == "__main__":
    unittest.main()
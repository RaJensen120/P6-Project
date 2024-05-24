import unittest
from unittest.mock import patch, MagicMock
import types
import whisperWorkload

class TestWhisper(unittest.TestCase):
    @patch('whisperWorkload.whisper.load_model')
    @patch('whisperWorkload.random.choice')
    def test_loadModel(self, mock_choice, mock_load_model):
        mock_choice.return_value = 'test.mp3' # Mocking return values

        # Mocking model object and its transcribe method
        mock_model = MagicMock()
        mock_model.transcribe.return_value = {'test': 'result'}
        mock_load_model.return_value = mock_model

        # Call the function to test
        result, search_result = whisperWorkload.loadModel()

        # Assertions
        self.assertEqual(result, {'test': 'result'})

        self.assertIsInstance(result, dict) # result should be a dictionary
        self.assertIsInstance(search_result, types.GeneratorType) # search_result should be a list

        mock_load_model.side_effect = OSError("Test OSError") # Set up mock load_model to raise OSError

        with self.assertRaises(IOError): # Ensure that an IOError is handled gracefully
            whisperWorkload.loadModel() # Call loadModel with invalid file

        self.assertTrue(search_result) # search_result should not be empty  

    @patch('whisperWorkload.search')
    def test_performSearch(self, mock_search):
        # Mocking return value
        mock_search.return_value = ['result1', 'result2', 'result3', 'result4', 'result5']

        # Call the function to test
        result = whisperWorkload.performSearch('test query')

        # Assertions
        self.assertEqual(result, ['result1', 'result2', 'result3', 'result4', 'result5'])

    def test_findSoundFiles(self):
        # Mocking return value
        with patch('whisperWorkload.os.listdir') as mock_listdir:
            mock_listdir.return_value = ['test1.mp3', 'test2.mp3', 'test3.mp3']

            # Call the function to test
            result = whisperWorkload.findSoundFiles()

            # Assertions
            self.assertEqual(result, ['test1.mp3', 'test2.mp3', 'test3.mp3'])
    
    @patch('whisperWorkload.random.choice')
    def test_selectRandomFile(self, mock_choice):
        # Mocking return value
        mock_choice.return_value = 'test.mp3'

        # Call the function to test
        result = whisperWorkload.selectRandomFile(['test1.mp3', 'test2.mp3', 'test3.mp3'])

        # Assertions
        self.assertEqual(result, 'test.mp3')

        self.assertIsInstance(result, str) # result should be a string

if __name__ == '__main__':
    unittest.main()
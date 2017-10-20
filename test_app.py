import unittest
import app
import json


class TestParsingMethods(unittest.TestCase):

    def test_get_json_response(self):
        #output = app.get_pipeline_status()
        #self.assertEqual(output, '123')
        pass

    def test_parse_jason_response(self):
        """ Mock Using Local Json """
        with open("sample.json") as json_data:
            data = json.load(json_data)
        output = app.parse_pipeline_status(data)
        self.assertEqual(output['Name'], 'MyFirstPipeline')
        self.assertEqual(len(output['Stages']), 3)


if __name__ == '__main__':
    unittest.main()

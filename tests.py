import unittest
from unittest.mock import patch, MagicMock
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring
from xml_file_processor import FileProcessor
from io import StringIO

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_temp.xml'
        with open(self.filename, 'w') as file:
            file.write('<root></root>')
        self.processor = FileProcessor()

    def create_test_xml_file(self):
        # Create a test XML file
        root = Element('data')
        record1 = Element('record')
        record2 = Element('record')
        SubElement(record1, 'id').text = '1'
        SubElement(record1, 'name').text = 'Alice'
        SubElement(record1, 'value').text = '123'
        SubElement(record2, 'id').text = '2'
        SubElement(record2, 'name').text = 'Bob'
        SubElement(record2, 'value').text = '456'
        root.append(record1)
        root.append(record2)

        tree = tostring(root, encoding='unicode')
        with open(self.filename, 'w') as file:
            file.write(tree)

    def test_read_file(self):
        self.create_test_xml_file()
        root = self.processor.read_file(self.filename)
        self.assertIsNotNone(root)

    def test_add_record(self):
        self.create_test_xml_file()
        new_record = Element('record')
        SubElement(new_record, 'id').text = '3'
        SubElement(new_record, 'name').text = 'Charlie'
        SubElement(new_record, 'value').text = '789'

        self.processor.add_record(self.filename, new_record)

        # Check if the new record is added by reading the file again or other assertions

    def test_delete_record(self):
        self.create_test_xml_file()
        self.processor.delete_record(self.filename, '1')

        # Check if the record with ID '1' is deleted

    def test_update_record(self):
        self.create_test_xml_file()
        updated_record = Element('record')
        SubElement(updated_record, 'id').text = '2'
        SubElement(updated_record, 'name').text = 'Updated Bob'
        SubElement(updated_record, 'value').text = 'Updated 456'

        self.processor.update_record(self.filename, '2', updated_record)

        # Check if the record with ID '2' is updated

# --------------- MOCK ------------------------------

    @patch('xml.etree.ElementTree.parse')
    def test_read_file_with_mock(self, mock_parse):
        mock_tree = ET.ElementTree(ET.fromstring('<root><person><name>John</name></person></root>'))
        mock_parse.return_value = mock_tree

        root = self.processor.read_file('test_data.xml')
        self.assertIsNotNone(root.find("./person[name='John']"))

    @patch('xml.etree.ElementTree.ElementTree.write')
    def test_add_record_with_mock(self, mock_write):
        mock_write.return_value = None

        person_data = {'name': 'Jane', 'age': '29', 'address': {'street': '789 Test St', 'city': 'Test City', 'state': 'TC', 'zip': '98765'}}
        self.processor.add_record(self.filename, person_data)
        mock_write.assert_called_once()

    @patch('xml.etree.ElementTree.ElementTree.write')
    def test_delete_record_with_mock(self, mock_write):
        mock_write.return_value = None

        self.processor.delete_record(self.filename, 'Jane')
        mock_write.assert_called_once()

    @patch('xml.etree.ElementTree.ElementTree.write')
    def test_update_record_with_mock(self, mock_write):
        mock_write.return_value = None

        updated_person_data = {'name': 'Jane', 'age': '30', 'address': {'street': '101 Test St', 'city': 'New Test City', 'state': 'NT', 'zip': '10101'}}
        self.processor.update_record(self.filename, 'Jane', updated_person_data)
        self.assertEqual(mock_write.call_count, 2)

if __name__ == '__main__':
    unittest.main()
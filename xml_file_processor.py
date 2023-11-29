import xml.etree.ElementTree as ET

class FileProcessor:
    def read_file(self, filename):
        try:
            tree = ET.parse(filename)
            return tree.getroot()
        except FileNotFoundError:
            print("File not found.")
            return None
        except ET.ParseError:
            print("Error parsing XML file.")
            return None

    def add_record(self, filename, record):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            root.append(record)
            tree.write(filename)
            print("Succes!")
        except FileNotFoundError:
            print("File not found.")
        except ET.ParseError:
            print("Error parsing XML file.")

    def delete_record(self, filename, record_id):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            for record in root.findall('.//record'):
                return _remove_record(filename, record_id, tree, root, record)
            print("Record not found.")
        except FileNotFoundError:
            print("File not found.")
        except ET.ParseError:
            print("Error parsing XML file.")

    def update_record(self, filename, record_id, new_record):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            for record in root.findall('.//record'):
                return _update_record(filename, record_id, new_record, tree, root, record)
            print("Record not found.")
        except FileNotFoundError:
            print("File not found.")
        except ET.ParseError:
            print("Error parsing XML file.")


    def display_records(self, filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            for record in root.findall('.//record'):
                print(ET.tostring(record).decode())
        except FileNotFoundError:
            print("File not found.")
        except ET.ParseError:
            print("Error parsing XML file.")


def _remove_record(filename, record_id, tree, root, record):
    if record.find('id').text == record_id:
        root.remove(record)
        tree.write(filename)
        print("Succes!")
        return

        
def _update_record(filename, record_id, new_record, tree, root, record):
    if record.find('id').text == record_id:
        root.remove(record)
        root.append(new_record)
        tree.write(filename)
        print("Record updated successfully.")
        return

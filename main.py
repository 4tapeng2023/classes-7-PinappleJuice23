from xml_file_processor import FileProcessor
import xml.etree.ElementTree as ET

def print_menu():
    print("1. Read XML file")
    print("2. Add record")
    print("3. Delete record")
    print("4. Update record")
    print("5. Display records")
    print("6. Exit")

def get_record_from_user():
    record_id = input("Enter record ID: ")
    return record_id

def main():
    processor = FileProcessor()
    filename = "data.xml"  # Update with your XML file name

    while True:
        print("\nXML File Processor Menu:")
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            processor.read_file(filename)
        elif choice == '2':
            record_id = get_record_from_user()
            processor.add_record(filename, record_id)
        elif choice == '3':
            record_id = input("Enter record ID to delete: ")
            processor.delete_record(filename, record_id)
        elif choice == '4':
            record_id = input("Enter record ID to update: ")
            new_record_id = get_record_from_user()
            processor.update_record(filename, record_id, new_record_id)
        elif choice == '5':
            processor.display_records(filename)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
CONTACT LIST MANAGER - PYTHON APPLICATION

Description:
A simple command-line contact manager application that allows users to:
- Store contacts (name and phone number)
- View all contacts
- Modify existing contacts
- Search for specific contacts
- Save contacts to a JSON file

Features:
- Persistent storage using JSON
- Simple menu-driven interface
- Error handling for file operations
- Case-insensitive commands

Requirements:
- Python 3.x
- No additional libraries required

Installation:
1. Clone this repository or download the script
2. Ensure you have Python 3 installed

Usage:
1. Run the script: python contacts.py
2. Follow the on-screen menu options:
   1. Add new contact
   2. View all contacts
   3. Modify existing contact
   4. Search for contact
   5. Exit program

Data Storage:
- Contacts are automatically saved to contacts.json
- File is created automatically if it doesn't exist
- Data persists between program runs

Code Structure:
- main(): Entry point with all functions
- load_contacts(): Reads from JSON file
- save_contacts(): Writes to JSON file
- CRUD operations for contact management

Notes:
- All contacts are stored in memory while program runs
- Changes are saved automatically
- Simple error handling for file operations

Example Usage:
1. Add contact: John, 555-1234
2. Search for: John → shows 555-1234
3. Modify: Change John's number to 555-5678
4. View all: Shows updated contact list


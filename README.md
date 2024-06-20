# Fit Track Gym Management System

![image](https://github.com/andreikennethmoreno/Gym_Track/assets/124364969/93545634-cfec-4904-ad6f-a21c649809e4)

## Made with 
- Tkinter
- Sqlite
- Tkinter Designer

## Description of System

This Tkinter-based GUI application is designed for efficient gym management, encompassing both login functionality and gym member management.

### Purpose

- **Login Interface:** Facilitates secure access with username and password validation.
- **Gym Management:** Allows administrators to manage gym attendance logs and member details.

### Features

1. **Login System:**
   - Username and password fields with validation.
   - Login button to authenticate users.
   - Decorative images and text labels on a styled canvas.
   - Uses absolute paths for image resources.
   - Upon successful login, launches the main gym management script.

2. **Gym Management:**
   - **Database:** Utilizes SQLite (`gym.db`) for data storage with a table `gymLogs`.
   - **CRUD Operations:** Add, update, delete, and search gym member entries.
   - **Session Tracking:** Track member session times.

### Interface

- **Window Configuration:**
  - Main window titled "Gym App," size 1100x700, with a white background.
- **Canvas:**
  - Places various widgets and elements with a white background.
- **Buttons:**
  - `add_button`: Adds a new gym member.
  - `update_button`: Updates an existing gym member.
  - `delete_button`: Deletes a selected gym member.
  - `logout`: Logs out of the application.
  - `gymLog`: Redirects to the gym log page.
  - `gymMembers`: Placeholder button without functionality.
- **Entry Widgets:**
  - Fields for user input (name, contact, number of months, search).
- **Treeview (`gymMember_tree`):**
  - Displays gym members in a tabular format with columns for Member ID, Full Name, Contact, Date Registered, Num of Months, Expiration Date, and Is Expired.

### Functions

- **Database Operations:**
  - `add_gymMember()`: Adds a new gym member to the database.
  - `load_gymMember()`: Loads and displays all gym members in the `gymMember_tree`.
  - `update_gymMember()`: Updates an existing gym member record.
  - `delete_gymMember()`: Deletes a gym member record.
  - `search()`: Searches for gym members based on full name.
- **Other Functions:**
  - `clear_entries()`: Clears input fields.
  - `gymLog()`: Redirects to the gym log page.
  - `logout()`: Logs out of the application.

### Date and Time Handling

- Manages date and time using the `datetime` module for operations like calculating expiration dates and checking membership status (`is_expired`).

### External Script Execution

- Uses `subprocess.run` to run other Python scripts (`gymLogs.py` and `login.py`) for logging out and navigating to gym logs.

This comprehensive system allows gym administrators to efficiently manage and track member activities within the application interface.


Business : Liam Carl Athletic Gym
Owner : William Carl B. Bolo
Address : Block 29 lot 9, 3rd floor , 1st Avenue, Citihomes Subdivision , Molino 4 Cavite

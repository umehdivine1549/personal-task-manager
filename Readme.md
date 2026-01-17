PERSONAL TASK MANAGER (PTM)
SOFTWARE ENGINEERING (SEN) ASSIGNMENT
PROJECT OVERVIEW
The Personal Task Manager (PTM) is a command-line based software application developed using Python. The system allows users to manage personal tasks by adding, viewing, updating, completing, and deleting tasks. All tasks are stored persistently using a local JSON file.
This project demonstrates the complete application of the Software Development Life Cycle (SDLC), with strict consistency between system design and implementation.
SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)
The Waterfall Model was adopted for this project because the system requirements were clearly defined and stable.
The SDLC phases used are:
Requirement Analysis
System Design
Implementation
Testing
Deployment
Maintenance
Each phase is described below.
REQUIREMENT ANALYSIS
3.1 Functional Requirements
The system shall:
Allow users to add a new task
Display all existing tasks
Update task title and description
Mark tasks as completed
Delete tasks
Save tasks permanently using local storage
3.2 Non-Functional Requirements
The system shall:
Be implemented using Python
Use a simple menu-driven interface
Store data persistently using a JSON file
Be easy to understand and maintain
SYSTEM DESIGN
4.1 System Architecture
The system uses a modular procedural architecture implemented within a single Python file. Logical separation of responsibilities is achieved using classes and functions.
4.2 System Components (Exact Names Used)
Component Name: Task
Description: Represents a single task in the system
Component Name: TaskManager
Description: Handles all task-related operations and data persistence
Component Name: storage.json
Description: Stores task data permanently
Component Name: main()
Description: Entry point of the application
4.3 Data Model
Each task is represented using the following attributes:
Task
task_id (integer)
title (string)
description (string)
completed (boolean)
IMPLEMENTATION
5.1 Programming Language
The system is implemented using Python 3.
5.2 Implementation Description
The Task class defines the task entity.
The TaskManager class handles task creation, retrieval, updating, deletion, and storage.
Tasks are stored in a file named storage.json using JSON serialization.
The main() function provides a menu-driven interface that allows user interaction.
5.3 File Structure
personal_task_manager
personal_task_manager.py
storage.json
README.txt
TESTING
6.1 Testing Method Used
Manual testing and black-box testing were used to validate system functionality.
6.2 Test Cases
Test Case: Add Task
Input: Task title and description
Expected Result: Task saved successfully
Test Case: View Tasks
Input: None
Expected Result: All tasks displayed
Test Case: Update Task
Input: Valid task ID and new details
Expected Result: Task updated successfully
Test Case: Mark Task as Completed
Input: Valid task ID
Expected Result: Task status changed to completed
Test Case: Delete Task
Input: Valid task ID
Expected Result: Task removed from system
Test Case: Data Persistence
Input: Restart application
Expected Result: Tasks remain stored
All test cases passed successfully.
DEPLOYMENT
The application does not require compilation.
Deployment steps:
Install Python 3
Copy the project files
Run the application using the command:
python personal_task_manager.py
The system automatically creates the storage.json file if it does not exist.
MAINTENANCE
The system is designed for easy maintenance and future enhancements. Possible improvements include:
Adding a graphical user interface
Implementing task deadlines and reminders
Adding user authentication
Integrating a database such as SQLite
CONCLUSION
The Personal Task Manager project successfully demonstrates all phases of the Software Development Life Cycle. The system meets all specified requirements, maintains consistency between design and implementation, and provides a reliable solution for managing personal tasks.
AUTHOR
Umeh Divine
# Student Management System

A Python-based Student Management System with three different storage implementations: in-memory, JSON file, and MySQL database.

## Features

- Add, search, update, delete, and display student records
- Multiple storage options (memory, JSON, MySQL)
- Score management (MySQL version only)
- Console-based interface

## Files

- StudentManagement.py - In-memory storage version
- StudentManagementJSON.py - JSON file storage version  
- StudentManagementMYSQL.py - MySQL database version with score tracking
- StudentData.json - Sample student data

## Student Data Structure

- ID, First Name, Last Name, Age
- Place of Birth, Birth Date, Phone Number

## Requirements

- Python 3.7+
- `mysql-connector-python` (for MySQL version)

## Usage

Run any version:
```bash
python StudentManagement.py
python StudentManagementJSON.py  
python StudentManagementMYSQL.py
```

Each provides a menu to manage student records through console interface.

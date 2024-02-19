# note_taking_application

---

# Task Description:

Develop a RESTful API for a simple note-taking application. The API should allow users to perform basic CRUD operations (Create, Read, Update, Delete) on notes.
Requirements:
Endpoints: Implement the following endpoints:

1. POST /login: Create a simple login view
2. POST /signup: Create a single user sign up view
3. POST /notes/create: Create a new note.
4. GET /notes/{id}: Retrieve a specific note by its ID.
5. POST /notes/share: Share the note with other users.
6. PUT /notes/{id}: Update an existing note.
7. GET /notes/version-history/{id}: GET all the changes associated with the note.

   Data Model: Design an efficient schema that can support all the above functions. Include a user model,
   Validation: Implement basic input validation for creating and updating notes. Ensure that required fields are provided and have appropriate data types.
   Error Handling: Handle errors gracefully and return meaningful error responses with appropriate HTTP status codes.
   Testing: Write unit tests to ensure the functionality and integrity of the API endpoints.

---

# How to run code:

    python3 manage.py runserver

---

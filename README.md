
# Masterblog-API

Masterblog-API is a simple web application for managing blog posts. It includes a backend API built with Flask, which provides endpoints for creating, retrieving, updating, and deleting blog posts. The frontend, also built with Flask, provides a user interface to interact with the API, allowing users to view, add, and delete posts.

## Project Structure

```
Masterblog-API/
├── backend/
│   ├── backend_app.py         # Backend Flask application (API)
├── frontend/
│   ├── frontend_app.py        # Frontend Flask application
│   ├── templates/
│   │   └── index.html         # Main HTML template for frontend
│   ├── static/
│   │   ├── styles.css         # CSS for styling the frontend
│   │   └── main.js            # JavaScript for frontend functionality
├── venv/                      # Virtual environment for dependencies
├── requirements.txt           # List of project dependencies
└── README.md                  # Project documentation
```

## Features

- **Backend (API)**:
    - `GET /api/posts`: Retrieve all posts with optional pagination and sorting.
    - `POST /api/posts`: Add a new post.
    - `PUT /api/posts/<id>`: Update an existing post by ID.
    - `DELETE /api/posts/<id>`: Delete a post by ID.
    - `GET /api/posts/search`: Search posts by title or content.
    - **Rate Limiting**: Limits requests to prevent abuse.
    - **CORS**: Configured to allow requests from the frontend.

- **Frontend**:
    - View a list of blog posts.
    - Add a new post.
    - Delete an existing post.
    - User-friendly interface with an input field for API base URL.

## Requirements

- **Python 3.8+**
- **Flask** (for backend and frontend)
- **Flask-CORS** (to handle cross-origin requests)
- **Flask-Limiter** (for rate limiting)

Install all dependencies listed in `requirements.txt`.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Masterblog-API.git
   cd Masterblog-API
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Backend Server**:
    - In one terminal, navigate to the `backend` directory and run:
      ```bash
      python backend_app.py
      ```
    - This will start the backend API on `http://127.0.0.1:5002`.

2. **Start the Frontend Server**:
    - In a second terminal, navigate to the `frontend` directory and run:
      ```bash
      python frontend_app.py
      ```
    - This will start the frontend on `http://127.0.0.1:5001`.

## Usage

1. **Open the Frontend**:
    - Visit `http://127.0.0.1:5001` in your browser.
    - The frontend interface should load with an input field pre-filled with the API base URL (`http://127.0.0.1:5002/api`).

2. **Interacting with the API**:
    - **Load Posts**: Click "Load Posts" to view all available posts.
    - **Add Post**: Enter a title and content, then click "Add Post" to create a new post.
    - **Delete Post**: Each post has a "Delete" button to remove it from the list.

## API Endpoints

### GET `/api/posts`
Retrieve a list of all blog posts with optional pagination and sorting.

#### Query Parameters:
- `sort`: Field to sort by (`title` or `content`).
- `direction`: Sort direction (`asc` or `desc`).
- `page`: Page number for pagination.
- `limit`: Number of posts per page.

### POST `/api/posts`
Add a new blog post.

#### Request Body:
- `title` (string): Title of the post.
- `content` (string): Content of the post.

### PUT `/api/posts/<id>`
Update an existing post by ID.

#### Request Body:
- `title` (string, optional): New title for the post.
- `content` (string, optional): New content for the post.

### DELETE `/api/posts/<id>`
Delete a post by ID.

### GET `/api/posts/search`
Search for posts by title or content.

#### Query Parameters:
- `title`: Keyword to search in post titles.
- `content`: Keyword to search in post content.

## Notes

- This application is intended for development and testing purposes. For production, use a production-ready WSGI server like Gunicorn or uWSGI and deploy the frontend and backend on secure domains.
- The backend rate limiting is configured to 30 requests per minute on the `/api/posts` endpoint. Adjust as necessary.

## Troubleshooting

If you encounter issues, check:
- **CORS Errors**: Ensure that the backend’s CORS settings are allowing requests from `http://127.0.0.1:5001`.
- **Rate Limiting**: If testing rapidly, you may hit the rate limit. Adjust the limit in `backend_app.py` as needed.
- **API URL**: Ensure that the correct API base URL (`http://127.0.0.1:5002/api`) is entered in the frontend interface.

## License

This project is licensed under the MIT License.

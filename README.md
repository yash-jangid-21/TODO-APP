# Task Management Web Application

This is a web application built using Django for managing tasks. It allows users to add, delete, and update tasks, with each task being assigned a priority level. 

## Features

- **Add Task**: Create new tasks with a title, due date, and priority level.
- **Delete Task**: Remove tasks from the list.
- **Update Task**: Modify the title, due date, or priority of existing tasks.
- **Priority Management**: Organize tasks based on their priority level to manage them more effectively.

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Python**: The programming language used for backend development.
- **HTML/CSS**: For the frontend design and layout.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/im-yash21/TO-DO-APP.git
    cd TO-DO-APP
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:8000/
    ```

## Usage

- **Home Page**: The home page displays a list of tasks. You can add new tasks using the form at the top of the page.
- **Add Task**: Enter the task title, due date, and priority, then click "Add Task" to save.
- **Update Task**: Click the "Update" button next to a task to update its details.
- **Delete Task**: Click the "Delete" button next to a task to remove it from the list.
- **Priority**: Tasks are displayed in order of priority.

## Configuration

The application uses default Django settings. For production use, consider configuring additional settings such as `ALLOWED_HOSTS`, `DEBUG`, and database settings in `settings.py`.

## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [yash062105@gmail.com](mailto:yash062105@gmail.com).

---

Thank you for checking out this project. Happy task managing!

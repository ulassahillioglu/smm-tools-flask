# SMM Tools Flask

This is a lightweight web application that allows you to use the Social Media Tools I have created so far. Some of these tools have already been uploaded to GitHub. I will continue to update it in the future and display related articles. I will add database integration features to this application and make it available to others to continue development with the latest versions of Social Media Tools.

**Please note:** This platform is currently in beta version and might contain some bugs and errors. If you encounter any issues, please let me know.

## Features

- **Flask Framework**: Built with Flask, a lightweight WSGI web application framework in Python.
- **Modular Structure**: Organized into separate modules for scalability and maintainability.
- **Basic Web UI**: Utilizes HTML, CSS, and JavaScript for the front-end.
- **Python**: Core functionality implemented in Python.

## Project Structure

smm-tools-flask/
│
├── SmTools/ # Main application package
├── static/ # Static files (CSS, JavaScript, images)
├── templates/ # HTML templates
├── .gitignore # Git ignore file
├── app.py # Flask application entry point
└── requirements.txt # Python dependencies


## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/ulassahillioglu/smm-tools-flask.git
    cd smm-tools-flask
    ```

2. **Set Up a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**
    ```bash
    python app.py
    ```
    The application will start on `http://127.0.0.1:5000/`.

## Usage

After running the application, navigate to `http://127.0.0.1:5000/` in your web browser to access the web interface. The application provides tools to manage various aspects of social media marketing.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any bug reports or feature requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

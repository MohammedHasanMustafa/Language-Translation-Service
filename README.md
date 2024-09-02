# Language Translation Service

A web application for translating text between multiple languages using Flask and Google Translate. The app is deployed on Railway Cloud and integrates with a Streamlit interface for additional functionality.

## Features

- **Language Translation**: Translate text between various languages using Google Translate.
- **Supported Languages**: English, Spanish, French, German, Italian, Hindi, Arabic, Tamil.
- **Deployment**: Hosted on Railway Cloud.

## Technologies

- **Backend**: Flask
- **Translation API**: Google Translate (`googletrans` library)
- **Frontend**: HTML with Flask templates
- **Deployment Platform**: Railway Cloud

## Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/MohammedHasanMustafa/language-translation-service.git
    cd language-translation-service
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask App Locally**:
    ```bash
    python app.py
    ```
    The app will be available at `http://127.0.0.1:5002`.

## Deployment

1. **Deploy to Railway Cloud**:
    - Push your code to a GitHub repository.
    - Connect your repository to Railway Cloud.
    - Railway will automatically build and deploy your app.

2. **Configuration**:
    - Ensure that the Flask app is configured to run on port 5002 to avoid conflicts.
    - Set up environment variables as needed on Railway Cloud.

## Usage

- **Home Page**: Access the app at the deployed Railway Cloud URL.
- **Translation**: Select source and target languages, enter text, and get translations.

## Troubleshooting

- **Port Conflicts**: If the port is in use, check for other applications or services using the same port.
- **Dependency Issues**: Ensure all required packages are listed in `requirements.txt`.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!


## Contact

For questions or feedback, please contact [hm248228@gmail.com](hm248228@gmail.com).


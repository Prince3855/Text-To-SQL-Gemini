# Text-to-SQL Generator
### Description

- This project is a basic version of a Text-to-SQL generator. It allows users to input natural language text queries and converts them into corresponding SQL queries. 
- The application leverages Google’s generative AI models to interpret and generate SQL queries, providing an interactive interface built with Streamlit. - This is an initial attempt at building a functional tool for converting human language into database queries.


#### This application uses the following dependencies:

- **streamlit**: Provides an interactive web interface for the text-to-SQL generator.
- **google-generativeai**: Utilizes Google's generative AI models to convert text into SQL queries.

## Local Setup

1. Clone repository
    ```bash
    git clone https://github.com/Prince3855/Text-To-SQL-Gemini.git
    ```

2. move into project directory
    ```bash
    cd Text-To-SQL-Gemini
    ```

3. Create virtual environment
    ```bash
    conda create -p venv python=3.10
    ```

4. Activate created virtual environment
    ```bash
    source activate ./venv
    ```

5. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

6. Create `.env` file using `.example.env` file and update values of variables

7. If it's first time to generate sample SQLite db and insert records execute
    ```bash
    python sqlite.py
    ```

8. Run application
    ```bash
    streamlit run app.py
    ```

## Demo




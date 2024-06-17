# FastAPI Text Summarizer

## Prerequisites

Before you begin, ensure you have met the following requirements:
- **Poetry**: Download and install Poetry [here](https://python-poetry.org/docs/)

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/PlzTrustMe/test_ai_task.git
cd test_ai_task
```

## Environment Setup

Make command
```bash
poetry install
```

## Running the Project

To build and run the project, execute:

```bash
poetry run python src/test_ai_task/web.py
```

## API Documentation

The API documentation can be accessed at [http://localhost:8000/docs](http://localhost:8000/docs).
Here you can find the list of available endpoints and their respective request and response schemas.

## API Endpoints
- REST API BASE URL: `http://localhost:8000/text/`
- API Documentation: `http://localhost:8000/docs`

### Summarize text

- Endpoint: `/summarize`
- Method: POST
- Request Body:
  - `text` (string): Text for summarizing.
- Response:
  - `text` (string): Summarized text
  
    
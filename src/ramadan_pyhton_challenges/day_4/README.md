# Simple API Guide

This is a simple FastAPI-based application that provides two main functionalities:
1. **Side Hustles**: Get random side hustle ideas or add new ones.
2. **Money Quotes**: Get random money-related quotes from famous personalities.

---

## How to Run the API

### Prerequisites
1. **Python 3.7+**: Ensure you have Python installed on your system.
2. **FastAPI**: Install FastAPI and Uvicorn (ASGI server) using pip:
   ```bash
   pip install fastapi uvicorn
   ```

### Running the API
1. Save the code in a file, e.g., `main.py`.
2. Run the API using fastapi:
   ```bash
   fastapi dev ./main.py
   ```
3. The API will be available at:
   - **Local**: `http://127.0.0.1:8000`
   - **Interactive Docs**: `http://127.0.0.1:8000/docs` (Swagger UI) or `http://127.0.0.1:8000/redoc` (ReDoc).

---

## API Endpoints

### 1. **Get Random Side Hustle**
- **Endpoint**: `/side-hustles`
- **Method**: `GET`
- **Parameters**:
  - `apiKey` (str): A valid API key (`1234567890`).
- **Response**:
  - Returns a random side hustle idea.
  - Example:
    ```json
    {
      "side_hustle": "Blogging - Create content and earn through ads and sponsorships."
    }
    ```
- **Error Responses**:
  - Invalid API key:
    ```json
    {
      "error": "Invalid API Key"
    }
    ```

---

### 2. **Add a New Side Hustle**
- **Endpoint**: `/side-hustles`
- **Method**: `POST`
- **Parameters**:
  - `apiKey` (str): A valid API key (`1234567890`).
  - `side_hustle` (str): The new side hustle idea to add.
- **Response**:
  - Success:
    ```json
    {
      "message": "Side hustle added successfully"
    }
    ```
- **Error Responses**:
  - Invalid API key:
    ```json
    {
      "error": "Invalid API Key"
    }
    ```
  - Side hustle already exists:
    ```json
    {
      "error": "Side hustle already exists"
    }
    ```
  - Empty side hustle:
    ```json
    {
      "error": "Side hustle cannot be empty"
    }
    ```

---

### 3. **Get Money Quotes**
- **Endpoint**: `/money-quotes`
- **Method**: `GET`
- **Parameters**:
  - `QuoteRange` (int): Number of random quotes to return (must be greater than 0).
  - `All` (bool): If `true`, returns all quotes.
- **Response**:
  - Random quotes:
    ```json
    {
      "money_quote": [
        "Warren Buffett - 'Do not save what is left after spending, but spend what is left after saving.'",
        "Robert Kiyosaki - 'It’s not how much money you make, but how much money you keep, how hard it works for you, and how many generations you keep it for.'"
      ]
    }
    ```
  - All quotes (if `All=true`):
    ```json
    {
      "money_quote": [
        "Warren Buffett - 'Do not save what is left after spending, but spend what is left after saving.'",
        "Robert Kiyosaki - 'It’s not how much money you make, but how much money you keep, how hard it works for you, and how many generations you keep it for.'",
        ...
      ]
    }
    ```
- **Error Responses**:
  - Invalid quote range:
    ```json
    {
      "error": "Invalid Quote Range"
    }
    ```

---

## Example Requests

### Get Random Side Hustle
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/side-hustles?apiKey=1234567890' \
  -H 'accept: application/json'
```

### Add a New Side Hustle
```bash
curl -X 'POST' \ 
  "http://127.0.0.1:8000/side-hustles?apiKey=1234567890&side_hustle=Freelance%20Graphic%20Design%20-%20Create%20logos%20and%20designs%20for%20clients." \
  -H 'accept: application/json' \
  -d ''
```

### Get Random Money Quotes
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/money-quotes?QuoteRange=3&All=false' \
  -H 'accept: application/json'```

### Get All Money Quotes
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/money-quotes?QuoteRange=3&All=true' \
  -H 'accept: application/json'```

---

## Notes
- The API uses a simple API key (`1234567890`) for authentication. Replace it with a more secure method for production use.
- The `side_hustles` and `money_quotes` lists are stored in memory. Any additions to `side_hustles` will be lost when the server restarts.


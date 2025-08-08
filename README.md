# aircraft-service

This service provides endpoints to retrieve aircraft information.

## Endpoints

### Get Aircrafts by Manufacturer

Retrieves a list of aircrafts for a specific manufacturer.

- **URL:** `/aircrafts`
- **Method:** `GET`
- **Query Parameters:**
    - `manufacturer` (string, required): The manufacturer of the aircraft.
    - `limit` (integer, optional, default: 30): The maximum number of aircrafts to return.

- **Example:**
```bash
curl "http://localhost:8000/aircrafts?manufacturer=boeing"
```

### Get Aircraft by Model

Retrieves a specific aircraft by its model name.

- **URL:** `/aircrafts/{model_name}`
- **Method:** `GET`
- **Path Parameters:**
    - `model_name` (string, required): The model name of the aircraft.

- **Example:**
```bash
curl "http://localhost:8000/aircrafts/747"
```

### Get Fastest Aircrafts by Manufacturer

Retrieves the fastest aircrafts for a specific manufacturer.

- **URL:** `/aircrafts/{manufacturer_name}/fastest`
- **Method:** `GET`
- **Path Parameters:**
    - `manufacturer_name` (string, required): The manufacturer of the aircraft.
- **Query Parameters:**
    - `limit` (integer, optional, default: 30): The maximum number of aircrafts to consider.
    - `top_n` (integer, optional, default: 5): The number of fastest aircrafts to return.

- **Example:**
```bash
curl "http://localhost:8000/aircrafts/boeing/fastest"
```

## API Ninjas

This service uses the [Aircraft API](https://api-ninjas.com/api/aircraft) from API Ninjas.

To get an API key, you need to sign up on the [API Ninjas website](https://api-ninjas.com/register). After signing up, you will get an API key associated with your account. You can then use this key in the `.env` file.

## Environment Variables

This project requires a `.env` file to be created in the `app` directory. The file should contain the following variables:

```
SERVICE_NINJAS_API_KEY=your_api_key
SERVICE_NINJAS_URL=https://api.api-ninjas.com/v1/aircraft
```

**Note:** Replace `your_api_key` with your actual API key.

## How to Run

This project uses a `Makefile` to simplify common tasks.

1.  Install dependencies:
    ```bash
    poetry install
    ```

2.  Run the application:
    ```bash
    make run
    ```

3.  Run tests:
    ```bash
    make test
    ```

4.  Run lint checks:
    ```bash
    make lint
    ```

5.  Run mypy type checks:
    ```bash
    make mypy
    ```

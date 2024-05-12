# API Documentation

## Overview


This API provides endpoints for managing and retrieving fashion item and trend data. It supports operations for querying trends based on seasons and managing fashion items. The API is tailored to assist fashion industry professionals and enthusiasts in keeping up with current trends and effectively managing inventory.

## Setup Instructions


### Prerequisites
- Python 3.10 or higher
- FastAPI
- Uvicorn

### Environment Setup


1. **Create and activate a virtual environment:**
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```
2. **Install required packages:**
  Before proceeding, ensure all dependencies are installed by running:
  ```bash
  pip install -r requirements.txt
  ```
3. **Prepare the database:**
  Before running the API, you must set up and populate the database by executing:
  ```bash
  python creating_tables_and_filling_data.py
  ```
4. **Run the API:**
  ```bash
  python run.py
  ```
## Items API Endpoints


## 1. Create Item


- **URL**: `/items/`
- **Method**: POST
- **Query Parameters**: None
- **Description**: Adds a new item to the database with detailed information such as name, category, material, style, color, and picture ID.
- **Request Body**: An instance of `ItemDTO` with fields:
 - `name`: string
 - `category`: string
 - `material`: string
 - `style`: string
 - `color`: string
 - `picture_id`: integer

- **Responses**:
 - **200 OK**: Item successfully created and the details of the new item are returned.
 - **400 Bad Request**: Validation error if the input data does not match the `ItemDTO` schema.


## 2. Delete Item by ID


- **URL**: `/items/{id}`
- **Method**: DELETE
- **Query Parameters**: None
- **Description**: Deletes an item from the database by its unique identifier.

- **Path Parameters**:
 - `id`: integer (Unique identifier of the item to delete)
- **Responses**:
 - **200 OK**: Item successfully deleted.
 - **404 Not Found**: No item found with the specified ID.

## 3. Update Item


- **URL**: `/items/{id}`
- **Method**: PUT
- **Query Parameters**: None
- **Description**: Updates the details of an existing item in the database by its ID.
- **Path Parameters**:
 - `id`: integer (Unique identifier of the item to update)
- **Request Body**: An instance of `ItemUpdateDTO` with optional fields:
 - `name`: string
 - `category`: string
 - `material`: string
 - `style`: string
 - `color`: string
 - `picture_id`: integer
- **Responses**:
 - **200 OK**: Item successfully updated with the new details provided.
 - **404 Not Found**: No item found with the specified ID to update.


## 4. Get Item by ID


- **URL**: `/items/{id}`
- **Method**: GET
- **Query Parameters**: None
- **Description**: Retrieves details of a specific item by its unique identifier.
- **Path Parameters**:
 - `id`: integer (Unique identifier of the item)
- **Responses**:
 - **200 OK**: Details of the item retrieved successfully.
 - **404 Not Found**: No item found with the specified ID.


## 5. Get Items by Season

- **URL**: `/items/seasons/{season}`
- **Method**: GET
- **Query Parameters**:
 - `limit`: integer (Optional, default is 0, specifies the number of items to retrieve)
 - `offset`: integer (Optional, default is 0, specifies the starting point for query results)
- **Description**: Fetches items associated with a specific fashion season. Supports pagination through `limit` and `offset`.
- **Path Parameters**:
 - `season`: string (A season such as 'Spring', 'Summer', 'Autumn', 'Winter')
- **Responses**:
 - **200 OK**: Successfully retrieves items for the specified season along with pagination details.
 - **400 Bad Request**: Invalid season parameter provided.


## Trends API Endpoint


## Get Trends by Season
- **URL**: `/trends/seasons/{season}`
- **Method**: GET
- **Query Parameters**: None
- **Description**: Retrieves the most trending item for a specified season. This endpoint is useful for analysts and retailers to identify top-performing products for specific seasons, helping in inventory planning and marketing strategies.
- **Path Parameters**:
 - `season`: string (A season such as 'Spring', 'Summer', 'Autumn', 'Winter')
- **Responses**:
 - **200 OK**: Successfully retrieves the most trending item of the season. Returns a JSON object containing the details of the item.
 - **400 Bad Request**: Invalid season parameter provided, unable to process the request.

## Additional Notes

- **Logging**: Ensure to check the logs for debugging and troubleshooting API issues. The configured logger in `utilities/logger.py` can be adjusted according to development or production needs to capture detailed information about the API's operations.
  
- **Security Enhancements**: Future updates may include additional security features to secure API access, such as implementing OAuth for authentication and HTTPS for secure data transmission.
- **Feedback and Contributions**: We welcome contributions and feedback on our API. If you encounter any issues or have suggestions for improvements, please submit them to our project's repository issue tracker.


- **Versioning**: We aim to maintain backward compatibility with our API endpoints. However, in the case of major changes that could break existing functionality, we will increment the major version number and provide migration guides.
  
- **Rate Limits**: Be mindful of rate limits to avoid being throttled. If you require higher limits for your use case, please contact our support to discuss an increase.



import requests
import json

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(message)s")
logger = logging.getLogger()

def get_API_json(endpoint: str) -> str:
    """Call a GET API endpoint and return the results.

    Args:
        endpoint (str): URL of the API endpoint.

    Returns:
        str: string representation of the JSON response.
    """
    logger.debug(f"Calling GET endpoint: {endpoint}")
    response = requests.get(endpoint, params=None, headers=None)
    logger.debug(f"Response with status_code: {response.status_code}")
    response.raise_for_status()
    logger.debug(f"Full response object: {response}")
    logger.debug(f"JSON response: {response.json()}")

    return response.json()


def pretty_print_json(data):
    """Pretty print a JSON object or string."""
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            print("Invalid JSON string")
            return
    print(json.dumps(data, indent=4, ensure_ascii=False))

endpoints = {("Dummy random quote", "https://dummyjson.com/quotes/random"),
             ("JSON Placeholder User 1", "https://json-placeholder.mock.beeceptor.com/users/1")
}

def main():

    # dummyjson single random quote
    for description, endpoint in endpoints: 
        print(f"Endpoint: {description}, {endpoint}")
        response_json = get_API_json(endpoint)
        pretty_print_json(response_json)


if __name__ == "__main__": 
    main()
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


def post_API(
    endpoint: str, data: dict = None, params: dict = None, headers: dict = None
) -> str:
    """Call a POST API endpoint and return the results.

    Args:
        endpoint (str): URL of the API endpoing
        params (dict, optional): Dictionary of the parameters. Defaults to None.
        headers (dict, optional): Dictionary of the headers. Defaults to None.

    Returns:
        str: string representation of the JSON response.
    """
    logger.debug(f"Calling POST endpoint: {endpoint}")
    response = requests.post(endpoint, data=data, params=params, headers=headers)
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


get_endpoints = [
    ("Dummy JSON random quote", "https://dummyjson.com/quotes/random"),
    ("Dummy JSON user", "https://dummyjson.com/users/1"),
    ("JSON Placeholder User 1", "https://json-placeholder.mock.beeceptor.com/users/1"),
    ("JSON Placeholder Typify User 1", "https://jsonplaceholder.typicode.com/users/1"),
]

put_endpoints = [
    (
        "JSON Placeholder successful login",
        "https://json-placeholder.mock.beeceptor.com/login",
        {"username": "bjoern", "password": "success-password"},
        {}
    ),
    (
        "Dummyjson auth",
        "https://dummyjson.com/auth/login",
        {"username": "emilys", "password": "emilyspass"},
        {}
    ),
    (
        "Dummyjson auth as json",
        "https://dummyjson.com/auth/login",
        json.dumps({"username": "emilys", "password": "emilyspass"}),
        {
            "Content-Type": "application/json",
        }
    ),
]


def main():
    # GET requests
    # logger.debug("GET requests")
    # for description, endpoint in get_endpoints:
    #     print(f"Endpoint: {description}, {endpoint}")
    #     response_json = get_API_json(endpoint)
    #     pretty_print_json(response_json)

    # PUT requests
    logger.debug("POST requests")
    for description, endpoint, data, headers in put_endpoints:
        print(f"Endpoint: {description}, {endpoint}, {data}, {headers}")
        response_json = post_API(endpoint, data=data, headers=headers)
        pretty_print_json(response_json)


    # dummy auth test
    # auth_test_data = (
    #     "Dummyjson auth",
    #     "https://dummyjson.com/auth/login",
    #     {"username": "emilys", "password": "emilyspass"},
    #     {
    #         "Content-Type": "application/json",
    #     }
    # )
    # description, endpoint, data, headers = auth_test_data
    # r = requests.post(url=endpoint, data=json.dumps(data), params=None, headers=headers)
    # print(f"{r}")
    # print(f"{r.text}")




if __name__ == "__main__":
    main()

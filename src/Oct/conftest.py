import pytest
import requests
from dotenv import load_dotenv
import os


@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token


@pytest.fixture()
def create_booking_id():
    print("Create Booking Test Case")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json = {
        "firstname": "Preeti",
        "lastname": "Bharat",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json)
    print(type(URL))
    print(type(headers))
    print(type(json))

    # Assertions
    assert response.status_code == 200
    # get the response Body and Verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


@pytest.fixture()
def read_csv_file_data():
    pass


@pytest.fixture()
def read_my_sql_database():
    pass


@pytest.fixture()
def launch_browser():
    print("Launching browser!! Chrome")
    return "chrome"


@pytest.fixture()
def close_browser():
    print("Closing a browser!! Chrome")
    return "closed"


@pytest.fixture()
def read_url_testdata_excel():
    pass

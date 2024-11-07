# API Request - HTTP Request

import allure
import pytest
import requests


@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("TC#1 - Verify the Create Booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # To make Request we need;
    # URL
    # Method - POST
    # Headers - Content-type=Application/json
    # Payload / Data / Body - Dict / JSON
    # Auth(No)

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "nancy",
        "lastname": "Drew",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        }
    }

    response = requests.post(url=URL, headers=headers, json=payload)
    # status code
    assert response.status_code == 200

    responseData = response.json()

    # Response Body  Verification,
    # Headers

    bookingid = responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]
    assert firstname == "nancy"
    assert lastname == "Drew"
    assert totalprice == 111
    assert depositpaid == True

    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    # JSON Schema Validation
    # Time Response


@allure.title("TC#2: Create Booking CRUD-negative")
@allure.description("TC#2: Verify the booking is not created with {} data")
@pytest.mark.crud
def test_create_booking_crud_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking"
    URL = base_url + path_url
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    # status code
    assert response.status_code == 500

    responseData = response.json()


@allure.title("TC#3: Create Booking CRUD-negative")
@allure.description("TC#3: Verify the booking with invalid total price string")
@pytest.mark.crud
def test_create_booking_crud_negative_tc3():
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking"
    URL = base_url + path_url
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "nancy",
        "lastname": "Drew",
        "totalprice": "Preeti",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        }
    }

    response = requests.post(url=URL, headers=headers, json=payload)

    # Assertion
    assert response.status_code == 500



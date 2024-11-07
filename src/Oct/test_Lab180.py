# PUT request
# URL
# path - booking ID
# Token - Auth
# Header
# payload


import allure
import pytest
import requests


# Create Token - POST request
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


# Create Booking - POST request
def create_booking():
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


def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking" + str(create_booking())
    PUT_URL = base_url + path_url
    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "cookie": cookie
    }
    json_payload = {
        "firstname": "Swara",
        "lastname": "Bharat",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Swara"


def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking"
    bookingid = create_booking()
    Delete_url = URL + str(bookingid)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "cookie": cookie_value
    }
    print(headers)
    response = requests.delete(url=Delete_url, headers=headers)
    



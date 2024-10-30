import pytest
import allure
import requests


@allure.title("Test GET Request - RestFUL BOOKER Project#1")
@allure.description("TC#1 -> Verify that GET Request to find id's of all the bookings")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "PreetiBharat")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/2"
    response_data = requests.get(url)
    print(response_data)
    print(response_data.status_code)
    print(response_data.json())
    print(response_data.headers)
    print(response_data.text)
    assert response_data.status_code == 200


@allure.title("Test GET Request - RestFUL BOOKER Project#2")
@allure.description("TC#2 -> Verify that GET Request with invalid URL")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/123"
    response_data = requests.get(url)
    assert response_data.status_code == 404


@allure.title("Test GET Request - RestFUL BOOKER Project#3")
@allure.description("TC#3 -> Verify that GET Request with invalid path param")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/111"
    response_data = requests.get(url)
    assert response_data.status_code == 404


@allure.title("Test GET Request - RestFUL BOOKER Project#4")
@allure.description("TC#4 -> Verify that GET Request with exceeded ID limit")
@allure.testcase("TC#4")
@pytest.mark.smoke
def test_get_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/111234098675654"
    response_data = requests.get(url)
    assert response_data.status_code == 404

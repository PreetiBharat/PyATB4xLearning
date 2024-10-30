import pytest
import allure


@allure.title("TC#1: Verify that 2-2 is equal to 0")
@allure.description("This is a Smoke Test Case which verifies that 2-2 is equal to 0")
@pytest.mark.smoke
def sub0():
    assert 2 - 2 == 0


@allure.title("TC#1: Verify that 2-2 is equal to 0")
@allure.description("This is a Smoke Test Case which verifies that 2-2 is equal to 0")
@pytest.mark.smoke
def sub1():
    assert 2 - 2 == 0


@allure.title("TC#1: Verify that 2-2 is equal to 0")
@allure.description("This is a Smoke Test Case which verifies that 2-2 is equal to 0")
@pytest.mark.smoke
def sub2():
    assert 2 - 2 == 0


@allure.title("TC#1: Verify that 2-2 is equal to 0")
@allure.description("This is a Smoke Test Case which verifies that 2-2 is equal to 0")
@pytest.mark.skip
def sub3():
    assert 2 - 2 == 0

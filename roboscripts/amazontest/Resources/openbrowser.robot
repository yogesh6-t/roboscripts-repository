*** Settings ***
Library   SeleniumLibrary

*** Keywords ***
Open Browser with Amazon link
    [Arguments]    ${browser}
    Open Browser   https://www.amazon.in/   ${browser}
    wait until page contains  Your Amazon.in
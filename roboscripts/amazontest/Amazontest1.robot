*** Settings ***
Documentation  " Test browser"
Library  SeleniumLibrary
Resource  Resources/openbrowser.robot
Resource  Resources/closebrowser.robot


*** Variables ***
${BROWSER} =   chrome

*** Test Cases ***
Test Browser open close
    [Documentation]  "This is a test for opening and closing amazon website"
    Open Browser with Amazon link    ${BROWSER}
    sleep   3s
    close chrome browser

test case to search product in amazon
    [Documentation]  this is a test for opening browser and search product
    [Tags]  tag2
    Open Browser with Amazon link    ${BROWSER}
    input text  id=twotabsearchtextbox   oneplus 7 mobile phones
    click button  xpath=//*[@id="nav-search"]/form/div[2]/div/input
    wait until page contains   results for "oneplus 7 mobile phones"
    close chrome browser

test case to do open new tab
    [Documentation]  test case to do open new tab by image,add to cart, then show added to cart
    [Tags]  tag3
    Open Browser with Amazon link    ${BROWSER}
    input text  id=twotabsearchtextbox   oneplus 7 mobile phones
    click button  xpath=//*[@id="nav-search"]/form/div[2]/div/input
    wait until page contains   results for "oneplus 7 mobile phones"
    Click Image  xpath=//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div/span/a/div/img
    select window  NEW
    wait until page contains   OnePlus 7 (Mirror Grey, 6GB RAM, 128GB Storage)
    click button  xpath=//*[@id="add-to-cart-button"]
    wait until page contains   Added to Cart
    close chrome browser


test case to do sign-in before check out
    [Documentation]  test case to check for sign-in and if not,do so
    [Tags]  tag4
    Open Browser with Amazon link    ${BROWSER}
    input text  id=twotabsearchtextbox   oneplus 7 mobile phones
    click button  xpath=//*[@id="nav-search"]/form/div[2]/div/input
    wait until page contains   results for "oneplus 7 mobile phones"
    Click Image  xpath=//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div/span/a/div/img
    select window  NEW
    wait until page contains   OnePlus 7 (Mirror Grey, 6GB RAM, 128GB Storage)
    click element  xpath=//*[@id="add-to-cart-button"]
    wait until page contains   Added to Cart
    click element  xpath=//*[@id="hlb-ptc-btn-native"]
    wait until page contains   Login
    close chrome browser


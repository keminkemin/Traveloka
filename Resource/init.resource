*** Settings ***
Library    SeleniumLibrary
Library    DateTime
Library    String
Variables    ../Resource/locator.py

*** Variables ***
${baseUrl}    https://www.traveloka.com/en-id
${BROWSER}    chrome
${SELENIUM_SPEED}       0.3 seconds
${SELENIUM_WAIT_SPEED}  0.5 seconds
${SELENIUM_TIMEOUT}     30 seconds

*** Keywords ***
Get date
    ${startDate}=    Get Current Date    result_format=%d
    ${endDate}=    Add Time To Date    ${startDate}    2 days    date_format=%d
    
Configure selenium
    Set Selenium Speed              ${SELENIUM_SPEED}
    Set Selenium Implicit Wait      ${SELENIUM_WAIT_SPEED}
    Set Selenium Timeout            ${SELENIUM_TIMEOUT}

Open browser then go to url
    Open Browser    ${baseUrl}    ${BROWSER}
    Maximize Browser Window

User in homepage
    Location Should Be    ${baseUrl}

Exit selenium
    Close All Browsers
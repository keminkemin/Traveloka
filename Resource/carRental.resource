*** Settings ***
Resource    ../Resource/init.resource

*** Keywords ***
User book car rent without driver
    Click Element    ${carRent}
    Click Element    ${rentalLocation}
    Input Text    ${rentalLocation}    jakarta
    Wait Until Element Is Visible    ${jakartaBarat}
    Click Element    ${jakartaBarat}
    Click Element    ${rentDate}
    Click Element    ${pickDate}
    Click Element    ${rentEndDate}
    Click Element    ${endDate}
    Click Element    ${searchCar}
    Wait Until Element Is Visible    ${selectCar}
    Click Element    ${selectCar}
    Click Element    ${selectCarProvider}
    Scroll Element Into View    ${continueBook}
    Click Element    ${pickupRentalOffice}
    Click Element    ${pickupLocation}
    Click Element    ${selectPickup}
    Scroll Element Into View    ${continueBook}
    Click Element    ${dropOffOther}
    Click Element    ${dropOffAddress}
    Input Text    ${dropOffAddress}    jakarta
    Wait Until Element Is Visible    ${selectDropOff}
    Click Element    ${selectDropOff}
    Scroll Element Into View    ${continueBook}
    Click Element    ${continueBook}
    Sleep    10 seconds
*** Settings ***
Library  SeleniumLibrary
Resource    ../Resource/oneto50.resource

*** Test Cases ***
Solve 1 to 50 Game
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    FOR    ${i}    IN RANGE    1    51
        Click Number    ${i}
    END
    [Teardown]    Close Browser
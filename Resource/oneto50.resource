*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}         https://zzzscore.com/1to50/en/
${GRID_SIZE}   5

*** Keywords ***
Click Number
    [Arguments]    ${number}
    ${found}    Set Variable    False
    WHILE    ${found} == ${False}
        FOR    ${row}    IN RANGE    ${GRID_SIZE}
            FOR    ${col}    IN RANGE    ${GRID_SIZE}
                ${cell}    Get Text    xpath=(//div[@id='grid']/div)[${row} * ${GRID_SIZE} + ${col} + 1]
                IF    '${cell}' == '${number}'
                    Click Element    xpath=(//div[@id='grid']/div)[${row} * ${GRID_SIZE} + ${col} + 1]
                    ${found}    Set Variable    True
                    Exit For Loop
                END
            END
        END
    END

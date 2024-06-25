*** Settings ***
Resource    ../Resource/carRental.resource

Suite Setup        Run Keywords    Configure selenium    Get date    Open browser then go to url
Suite Teardown     Exit selenium


*** Test Cases ***
User able to book car rent without driver.
    Given User in homepage
    When User book car rent without driver
    Then User successful made book car rent
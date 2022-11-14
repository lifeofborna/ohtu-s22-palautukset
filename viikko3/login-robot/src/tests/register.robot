*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  borna  borna123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  b  b123213123
    Output Should Contain  User with username b is too short!

Register With Valid Username And Too Short Password
    Input Credentials  bozobozo  12
    Output Should Contain  Password should more than 3 values

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  dwqefewgfew  fqfqwfwfqwf23
    Output Should Contain  New user registered





*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command

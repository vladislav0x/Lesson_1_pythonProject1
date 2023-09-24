from selene.support.shared import browser
from selene import have

def test_ueserFrom_input():
    browser.open('https://demoqa.com/text-box')

    browser.element('#userName').type('Vladislav')
    browser.element('#userEmail').type('Vladislav@example.com')
    browser.element('#currentAddress').type('st.Leningradskaya 47')
    browser.element('#permanentAddress').type('Planet Earth')

    browser.element('#submit').click()

    browser.element('.border').should(have.text('Vladislav'))
    browser.element('.border').should(have.text('Vladislav@example.com'))
    browser.element('.border').should(have.text('st.Leningradskaya 47'))
    browser.element('.border').should(have.text('Planet Earth'))



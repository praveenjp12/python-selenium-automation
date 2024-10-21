from Utils.BaseElement import BaseElement


class FormSubmit:

        name_input = BaseElement(
            'css',
            'form input[name="name"]',
            'Name Input'
        )

        email_input = BaseElement(
            'css',
            '[name="email"]',
            'Email Input'
        )

        password_input = BaseElement(
            'css',
            '[type="password"]',
            'Password Input'
        )

        submit_button = BaseElement(
            'css',
            '[value="Submit"]',
            'Submit Button'
        )

        success_message = BaseElement(
            'css',
            'div.alert-success',
            'Success Message'
        )

        ice_cream_checkbox = BaseElement(
            'css',
            '#exampleCheck1',
            'Ice Cream Checkbox'
        )

        employment_status_student = BaseElement(
            'css',
            '#inlineRadio1',
            'Employment Status Student'
        )

        two_way_binding = BaseElement(
            'xpath',
            '(//input[@type="text"])[3]',
            'Two Way Binding'
        )

        gender_dropdown_menu = BaseElement(
            'css',
            '#exampleFormControlSelect1',
            'Gener Dropdown Menu'
        )
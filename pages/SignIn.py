from Utils.BaseElement import BaseElement


class SignIn:

        forgot_password_link = BaseElement(
            'css',
            'div.login-wrapper a.forgot-password-link',
            'Forgot Password Link'
        )

        create_account_link = BaseElement(
            'xpath',
            '//a[text()="Register here"]',
            'Create Account Link'
        )

        email_input = BaseElement(
            'css',
            '[formcontrolname="userEmail"]',
            'Emai Input'
        )

        password_input = BaseElement(
            'css',
            '[formcontrolname="userPassword"]',
            'Password Input'
        )

        login_button = BaseElement(
            'css',
            'input#login',
            'Login Button'
        )

        firstname_field = BaseElement(
            'css',
            '[formcontrolname="firstName"]',
            'FirstName Field'
        )

        lastname_filed = BaseElement(
            'css',
            '[formcontrolname="lastName"]',
            'Employment Status Student'
        )

        user_email_input = BaseElement(
            'css',
            '[formcontrolname="userEmail"]',
            'User Email Input'
        )

        phone_number_input = BaseElement(
            'css',
            '[formcontrolname="userMobile"]',
            'Phone Number Input'
        )

        user_password_input = BaseElement(
            'css',
            '[formcontrolname="userPassword"]',
            'User Password Input'
        )

        confirm_password_input = BaseElement(
            'css',
            '[formcontrolname="confirmPassword"]',
            'Confirm Password Input'
        )

        user_consent = BaseElement(
            'css',
            '[formcontrolname="required"]',
            'User Consent'
        )

        register_button = BaseElement(
            'css',
            'input#login',
            'Register Button'
        )

        toast_error_message = BaseElement(
            'css',
            '[id="toast-container"]',
            'Toast Error Message'
        )

        save_password_button = BaseElement(
            'css',
            '[type="submit"]',
            'Save Password Button'
        )

        brand_logo = BaseElement(
            'css',
            '[class="logo"]',
            'Brand Logo'
        )



class Assertions:

    @staticmethod
    def assert_equals(expected_value, actual_value):
        try:
            assert expected_value == actual_value
        except:
            raise Exception('Actual value is not equal to Expected value\nActual value - '
                    + actual_value + '\nExpected value - ' + expected_value)
    @staticmethod
    def assert_includes(expected_value, actual_value):
        try:
            assert expected_value in actual_value
        except:
            raise Exception('Actual value is not include Expected value\nActual value - '
                    + actual_value + '\nExpected value - ' + expected_value)
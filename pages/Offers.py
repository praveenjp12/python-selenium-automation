from Utils.BaseElement import BaseElement


class Offers:

        veg_fruit_column = BaseElement(
            'css',
            'table td:nth-child(1)',
            'Veg/Fruit Column'
        )

        sort_button = BaseElement(
            'css',
            'table span[class="sort-icon sort-descending"]',
            'Sort button'
        )

        pagination_buttons = BaseElement(
            'css',
            '.pagination a:not([aria-disabled])',
            'Pagination Buttons'
        )

        first_pagination_button = BaseElement(
            'css',
            'a[aria-label="First"]',
            'First Pagination Button'
        )

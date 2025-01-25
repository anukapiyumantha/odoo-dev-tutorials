{
    'name': 'Archiving Functionality for Product Categories',
    'version': '18.0.0.1',
    'summary': 'Enable archiving functionality specifically for Product Categories in Odoo',
    'sequence': 10,
    'description': """
This custom module demonstrates how to add archiving functionality exclusively for the Product Category model in Odoo. Designed for tutorial purposes, it provides a practical example of how to:

- Add the `active` field to the Product Category model to enable archiving.
- Automatically integrate archiving options into list views for product categories.
- Customize form views to support archiving functionality.
- Add filters to manage and view archived product categories easily.

This module is intended for learning and demonstration, helping developers understand how to extend Odoo functionality for specific use cases.
    """,
    'author': 'Anuka',
    'website': 'https://anuka.odoo.com/',
    'depends': ['product'],
    'data': [
        'views/product_category_views.xml',
    ],
}

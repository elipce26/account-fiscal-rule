import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-account-fiscal-rule",
    description="Meta package for oca-account-fiscal-rule Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-account_fiscal_position_partner_type',
        'odoo10-addon-account_fiscal_position_rule',
        'odoo10-addon-account_fiscal_position_rule_purchase',
        'odoo10-addon-account_fiscal_position_rule_sale',
        'odoo10-addon-account_fiscal_position_rule_sale_stock',
        'odoo10-addon-account_fiscal_position_rule_stock',
        'odoo10-addon-account_product_fiscal_classification',
        'odoo10-addon-l10n_eu_oss',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 10.0',
    ]
)

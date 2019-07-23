# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Groups
    group_ecofarm_manager = fields.Boolean(
        string='Manage Ecosoft FARM',
        implied_group='ecofarm.group_ecofarm_manager',
    )
    # OCA/l10n-thailand
    module_account_create_tax_cash_basis_entry_hook = fields.Boolean(
        string='TH - Cash Basis Hook',
        readonly=True,
    )
    module_l10n_th_partner = fields.Boolean(
        string='TH - Partner Fields',
        readonly=True,
    )
    module_l10n_th_account_report = fields.Boolean(
        string='TH - Accounting Reports',
    )
    module_l10n_th_vendor_tax_invoice = fields.Boolean(
        string='TH - Vendor Tax Invoice',
    )
    module_l10n_th_withholding_tax_cert = fields.Boolean(
        string='TH - Withholding Tax Certificate',
    )
    module_l10n_th_withholding_tax_cert_form = fields.Boolean(
        string='TH - Print Standard Withholding Tax Certificate ',
    )
    # OCA/account-financial-reporting
    module_account_financial_report = fields.Boolean(
        string='OCA Financial Reports',
    )
    account_financial_report
    # OCA/account-invoicing
    module_account_billing = fields.Boolean(
        string='Account Billing',
    )
    account_invoice_reimbursable
    account_menu_invoice_refund
    # OCA/acount-financial-tools
    module_account_type_menu = fields.Boolean(
        string='Account Menus',
        default=True,
    )
    account_asset_management
    account_document_reversal
    account_fiscal_year
    account_invoice_refund_link
    account_payment_intransit
    account_payment_intransit_deduction
    account_payment_intransit_reversal
    # OCA/credit-control
    account_financial_risk
    sale_financial_risk
    stock_financial_risk
    # OCA/hr
    hr_expense_advance_clearing
    hr_expense_invoice
    hr_expense_payment_difference
    # OCA/manufacture
    module_stock_picking_product_kit_helper = fields.Boolean(
        string='Stock Product Kit Helper',
    )
    # OCA/partner-contact
    module_partner_fax = fields.Boolean(
        string='Add Partner Fax Number',
        default=True,
    )
    # OCA/product-attribute
    product_brand
    product_secondary_unit
    product_sequence
    # OCA/purchase-workflow
    module_purchase_deposit = fields.Boolean(
        string='Purchase Deposit',
    )
    purchase_discount
    purchase_order_secondary_unit
    # OCA/reporting-engine
    module_report_xlsx = fields.Boolean(
        string='Report XLSX',
        readonly=True,
    )
    report_qweb_element_page_visibility
    report_xlsx
    # OCA/sale-workflow
    sale_order_line_sequence
    # OCA/server-tools
    module_auto_backup = fields.Boolean(
        string='Auto Backup Database',
        default=True,
    )
    module_excel_import_export = fields.Boolean(
        string='Excel Import Export',
        readonly=True,
    )
    module_dbfilter_from_header = fields.Boolean(
        string='Filter DB From URL',
    )
    module_module_analysis = fields.Boolean(
        string='Module Analysis',
        default=True,
    )
    auto_backup
    dbfilter_from_header
    # OCA/server-ux
    module_date_range = fields.Boolean(
        string='Date Range',
        readonly=True,
    )
    mass_editing
    # OCA/stock-logistics-warehouse
    stock_secondary_unit
    # OCA/web
    module_web_m2x_options = fields.Boolean(
        string='M2X Options',
        default=True,
    )

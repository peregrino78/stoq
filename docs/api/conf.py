# -*- coding: utf-8 -*-
#
# Stoq documentation build configuration file, created by
# sphinx-quickstart on Fri Feb 10 16:50:54 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))

import stoq

# So external modules always can be imported.
stoq_dir = os.path.dirname(stoq.__path__[0])
sys.path.insert(0, os.path.join(stoq_dir, 'external'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.graphviz',
    'sphinx.ext.viewcode',
    # Forked from sphinxcontrib.zopeext
    'zopeautointerface',
    # Document Stoq specific APIs
    'stoqautodoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Stoq'
copyright = u'2012, Async'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '%s.%s' % (stoq.major_version, stoq.minor_version)

# The full version, including alpha/beta/rc tags.
release = stoq.version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Stoqdoc'

# List of domain substitutions we are using, the current format is:
# For example, for the domain class SaleItem we have.
# Plural versions can also be added, they have an s in the end, but
# they still refer to the same domain class:
# * name of the link: sale item
# * name of the alias: |saleitem|
# * plural name of the link: sale items
# * plural name of the alias: |saleitems|
rst_epilog = """
.. |account| replace::
    :class:`account <stoqlib.domain.account.Account>`
.. |accounttransaction| replace::
    :class:`account transaction <stoqlib.domain.account.AccountTransaction>`
.. |accounttransactions| replace::
    :class:`account transactions <stoqlib.domain.account.AccountTransaction>`
.. |address| replace::
    :class:`address <stoqlib.domain.address.Address>`
.. |addresses| replace::
    :class:`addresses <stoqlib.domain.address.Address>`
.. |attachment| replace::
    :class:`attachment <stoqlib.domain.attachment.Attachment>`
.. |bankaccount| replace::
    :class:`bank account <stoqlib.domain.account.BankAccount>`
.. |batch| replace::
    :class:`batch <stoqlib.domain.product.StorableBatch>`
.. |batches| replace::
    :class:`batches <stoqlib.domain.product.StorableBatch>`
.. |branch| replace::
    :class:`branch <stoqlib.domain.person.Branch>`
.. |branches| replace::
    :class:`branches <stoqlib.domain.person.Branch>`
.. |branchstation| replace::
    :class:`branch station <stoqlib.domain.station.BranchStation>`
.. |cardcost| replace::
    :class:`card operation cost <stoqlib.domain.payment.card.CardOperationCost>`
.. |carddevice| replace::
    :class:`card payment device <stoqlib.domain.payment.card.CardPaymentDevice>`
.. |cfop| replace::
    :class:`C.F.O.P. <stoqlib.domain.fiscal.CfopData>`
.. |client| replace::
    :class:`client <stoqlib.domain.person.Client>`
.. |clients| replace::
    :class:`clients <stoqlib.domain.person.Client>`
.. |clientcategory| replace::
    :class:`client category <stoqlib.domain.person.ClientCategory>`
.. |citylocation| replace::
    :class:`city location <CityLocation>`
.. |commission| replace::
    :class:`commission <stoqlib.domain.commission.Commission>`
.. |company| replace::
    :class:`company <stoqlib.domain.person.Company>`
.. |component| replace::
    :class:`component <stoqlib.domain.product.ProductComponent>`
.. |components| replace::
    :class:`components <stoqlib.domain.product.ProductComponent>`
.. |costcenter| replace::
    :class:`cost center <stoqlib.domain.costcenter.CostCenter>`
.. |costcenterentry| replace::
    :class:`cost center entry <stoqlib.domain.costcenter.CostCenterEntry>`
.. |creditprovider| replace::
    :class:`credit provider <stoqlib.domain.payment.card.CreditProvider>`
.. |creditcarddata| replace::
    :class:`credit card data <stoqlib.domain.payment.card.CreditCardData>`
.. |delivery| replace::
    :class:`delivery <stoqlib.domain.sale.Delivery>`
.. |employee| replace::
    :class:`employee <stoqlib.domain.person.Employee>`
.. |employees| replace::
    :class:`employees <stoqlib.domain.person.Employee>`
.. |gridgroup| replace::
    :class:`grid group <stoqlib.domain.product.GridGroup>`
.. |individual| replace::
    :class:`individual <stoqlib.domain.person.Individual>`
.. |inventory| replace::
    :class:`inventory <stoqlib.domain.inventory.Inventory>`
.. |inventoryitem| replace::
    :class:`inventory item <stoqlib.domain.inventory.InventoryItem>`
.. |inventoryitems| replace::
    :class:`inventory items <stoqlib.domain.inventory.InventoryItem>`
.. |image| replace::
    :class:`image <stoqlib.domain.image.Image>`
.. |loan| replace::
    :class:`loan <stoqlib.domain.loan.Loan>`
.. |loans| replace::
    :class:`loans <stoqlib.domain.loan.Loan>`
.. |location| replace::
    :class:`location <stoqlib.domain.address.CityLocation>`
.. |loginuser| replace::
    :class:`login user <stoqlib.domain.person.LoginUser>`
.. |loginusers| replace::
    :class:`login users <stoqlib.domain.person.LoginUser>`
.. |payment| replace::
    :class:`payment <stoqlib.domain.payment.payment.Payment>`
.. |payments| replace::
    :class:`payments <stoqlib.domain.payment.payment.Payment>`
.. |paymentcategory| replace::
    :class:`category <stoqlib.domain.payment.category.PaymentCategory>`
.. |paymentcomment| replace::
    :class:`payment comment <stoqlib.domain.payment.comments.PaymentComment>`
.. |paymentcomments| replace::
    :class:`payment comments <stoqlib.domain.payment.comments.PaymentComment>`
.. |paymentgroup| replace::
    :class:`payment group <stoqlib.domain.payment.group.PaymentGroup>`
.. |paymentgroups| replace::
    :class:`payment groups <stoqlib.domain.payment.group.PaymentGroup>`
.. |paymentrenegotiation| replace::
    :class:`payment renegotiation <stoqlib.domain.payment.renegotiation.PaymentRenegotiation>`
.. |paymentmethod| replace::
    :class:`payment method <stoqlib.domain.payment.method.PaymentMethod>`
.. |person| replace::
    :class:`person <stoqlib.domain.person.Person>`
.. |product| replace::
    :class:`product <stoqlib.domain.product.Product>`
.. |production| replace::
    :class:`production <stoqlib.domain.production.ProductionOrder>`
.. |productstockitem| replace::
    :class:`product stock item <stoqlib.domain.product.ProductStockItem>`
.. |purchase| replace::
    :class:`purchase <stoqlib.domain.purchase.PurchaseOrder>`
.. |purchaseitem| replace::
    :class:`purchase item <stoqlib.domain.purchase.PurchaseItem>`
.. |receive| replace::
    :class:`receive <stoqlib.domain.receiving.ReceivingOrder>`
.. |returnedsale| replace::
    :class:`returned sale <stoqlib.domain.returnedsale.ReturnedSale>`
.. |sale| replace::
    :class:`sale <stoqlib.domain.sale.Sale>`
.. |sales| replace::
    :class:`sales <stoqlib.domain.sale.Sale>`
.. |salecomment| replace::
    :class:`sale comment <stoqlib.domain.sale.SaleComment>`
.. |salecomments| replace::
    :class:`sale comments <stoqlib.domain.sale.SaleComment>`
.. |saleitem| replace::
    :class:`sale item <stoqlib.domain.sale.SaleItem>`
.. |saleitems| replace::
    :class:`sale items <stoqlib.domain.sale.SaleItem>`
.. |salesperson| replace::
    :class:`salesperson <stoqlib.domain.person.SalesPerson>`
.. |sellable| replace::
    :class:`sellable <stoqlib.domain.sellable.Sellable>`
.. |sellables| replace::
    :class:`sellables <stoqlib.domain.sellable.Sellable>`
.. |sellablecategory| replace::
    :class:`sellable category <stoqlib.domain.sellable.SellableCategory>`
.. |sellabletaxconstant| replace::
    :class:`sellable tax constant <stoqlib.domain.sellable.SellableTaxConstant>`
.. |sellableunit| replace::
    :class:`sellable unit <stoqlib.domain.sellable.SellableUnit>`
.. |service| replace::
    :class:`service <stoqlib.domain.service.Service>`
.. |stockdecrease| replace::
    :class:`stock decrease <stoqlib.domain.stockdecrease.StockDecrease>`
.. |stockdecreases| replace::
    :class:`stock decreases <stoqlib.domain.stockdecrease.StockDecrease>`
.. |storable| replace::
    :class:`storable <stoqlib.domain.product.Storable>`
.. |storables| replace::
    :class:`storable <stoqlib.domain.product.Storable>`
.. |supplier| replace::
    :class:`supplier <stoqlib.domain.person.Supplier>`
.. |suppliers| replace::
    :class:`suppliers <stoqlib.domain.person.Supplier>`
.. |transfer| replace::
    :class:`transfer <stoqlib.domain.transfer.TransferOrder>`
.. |transferitem| replace::
    :class:`transfer item <stoqlib.domain.transfer.TransferItem>`
.. |transferitems| replace::
    :class:`transfer items <stoqlib.domain.transfer.TransferItem>`
.. |till| replace::
    :class:`till <stoqlib.domain.till.Till>`
.. |tillentry| replace::
    :class:`till entry <stoqlib.domain.till.TillEntry>`
.. |transactionentry| replace::
    :class:`transaction entry <stoqlib.domain.system.TransactionEntry>`
.. |transporter| replace::
    :class:`transporter <stoqlib.domain.person.Transporter>`
.. |workorder| replace::
    :class:`work order <stoqlib.domain.workorder.WorkOrder>`
.. |workorders| replace::
    :class:`work orders <stoqlib.domain.workorder.WorkOrder>`
.. |workorderitem| replace::
    :class:`work order item <stoqlib.domain.workorder.WorkOrderItem>`
.. |workorderitems| replace::
    :class:`work order items <stoqlib.domain.workorder.WorkOrderItem>`
.. |workordercategory| replace::
    :class:`work order category <stoqlib.domain.workorder.WorkOrderCategory>`
.. |workorderpackage| replace::
    :class:`work order package <stoqlib.domain.workorder.WorkOrderPackage>`
.. |workorderpackages| replace::
    :class:`work order packages <stoqlib.domain.workorder.WorkOrderPackage>`
.. |workorderpackageitem| replace::
    :class:`work order package item <stoqlib.domain.workorder.WorkOrderPackageItem>`
.. |workorderpackageitems| replace::
    :class:`work order package items <stoqlib.domain.workorder.WorkOrderPackageItem>`
"""

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'Stoq.tex', u'Stoq Documentation',
     u'Async', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'stoq', u'Stoq Documentation',
     [u'Async'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'Stoq', u'Stoq Documentation',
     u'Async', 'Stoq', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# autodoc

autodoc_member_order = 'bysource'

# coverage

coverage_ignore_modules = [
    r'stoqlib.database.*',
    r'stoqlib.domain.exampledata',
    r'stoqlib.domain.test.*',
    r'stoqlib.net.*',
    r'stoqlib.reporting.*',
]


def setup(app):
    from devhelp2 import Devhelp2Builder
    app.add_builder(Devhelp2Builder)

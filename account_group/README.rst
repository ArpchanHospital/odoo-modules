===================
Groups for accounts
===================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:f66b512be310a51042a0187445b0333a3aab93c7472b10c85ed31815fec191d9
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Faccount--financial--tools-lightgray.png?logo=github
    :target: https://github.com/OCA/account-financial-tools/tree/10.0/account_group
    :alt: OCA/account-financial-tools
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/account-financial-tools-10-0/account-financial-tools-10-0-account_group
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/account-financial-tools&target_branch=10.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This modules brings to version 10 the account group feature from v11.

It also includes a level field for indicating the level depth of the account
group.

**Table of contents**

.. contents::
   :local:

Installation
============

If you have already the chart of accounts loaded on your company, you will
need to update it through the module `account_chart_update`. Follow the
instructions on that module for that.

Configuration
=============

To configure account groups, you need to:

#. Be "Account / Adviser" role.
#. Go to *Invoicing/Accounting > Configuration > Accounting > Accounts Groups*.
#. Create or modify existing groups.

For assigning groups to account templates, you have to:

#. Set the group on your account chart module or extension.
#. Or develop/create UI access.

When you have groups on your account templates, you can load a chart template
for a new company, and they will be transferred to created accounts.

Usage
=====

For assigning groups to accounts:

#. Go to *Invoicing > Adviser > Chart of Accounts*.
#. Edit one account and set "Group" field.

Known issues / Roadmap
======================

* This module shouldn't be migrated to v11, as it's a native feature.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-financial-tools/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/account-financial-tools/issues/new?body=module:%20account_group%0Aversion:%2010.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Tecnativa

Contributors
~~~~~~~~~~~~

* `Tecnativa <https://www.tecnativa.com>`__:

  * Pedro M. Baeza

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/account-financial-tools <https://github.com/OCA/account-financial-tools/tree/10.0/account_group>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.

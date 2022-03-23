{
    "name": "Bypass SMTP relaying blockage",
    "summary": "Force Sender and Reply To in mails to solve smtp relaying blockage",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "author": "Elabore",
    "website": "https://elabore.coop/",
    "installable": True,
    "application": False,
    "description": """
=============================
Bypass SMTP relaying blockage
=============================
This module allow to force the Sender and Reply To fields in mails, to bypass the smtp relaying blockage performed by some email servers.

Installation
============
Just install bypass_smtp_relaying_blockage, all dependencies will be installed by default.

Known issues / Roadmap
======================

Bug Tracker
===========
Bugs are tracked on `GitHub Issues
<https://github.com/elabore-coop/.../issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------
* Elabore: `Icon <https://elabore.coop/web/image/res.company/1/logo?unique=f3db262>`_.

Contributors
------------
* Stéphan Sainléger <https://github.com/stephansainleger>

Funders
-------
The development of this module has been financially supported by:
* Elabore (https://elabore.coop)

Maintainer
----------
This module is maintained by ELABORE.

""",
    "depends": ["mail"],
    "data": ["views/ir_mail_server_views.xml"],
}

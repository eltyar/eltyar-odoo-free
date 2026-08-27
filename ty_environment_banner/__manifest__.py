{
    "name": "Environment Banner",
    "summary": "Server-side warning banner for staging and non-production databases.",
    "description": """Displays a server-rendered warning banner above the
navigation bar on staging and other non-production databases, so users always
know when they are not working on live data.

Detection is automatic for neutralized databases and for database names
containing staging, test or demo, and can be forced on or off with a single
system parameter. The banner text and background color are configurable.

Pure server-side QWeb: no JavaScript, no bundled assets, and no dependency
beyond the standard web module. Compatible with Odoo 14 through 19.""",
    "version": "19.0.1.0.0",
    "author": "Mohamed Eltayar",
    "website": "https://eltyar.com",
    "category": "Technical",
    "license": "LGPL-3",
    "depends": ["web"],
    "data": ["views/webclient_templates.xml"],
    "images": ["static/description/images/main_screenshot.png"],
    "installable": True,
    "application": False,
    "auto_install": False,
}

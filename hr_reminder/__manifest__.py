{
    'name': 'Sigma HRMS Reminders Todo',
    'version': '1.0.',
    'category': 'Generic Modules/Human Resources',
    'summary': 'HR Reminder For HRMS',
     'author': 'Indglobal digital',
    'company': 'Indglobal digital pvt ltd',
    'website': "https://indglobal.in/",
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_reminder_security.xml',
        'views/hr_reminder_view.xml',
        'views/reminder_template.xml',
    ],
    'qweb': [
        'static/src/xml/reminder_topbar.xml', ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

{
    'name': 'To-Do Application',
    'description': 'Manage your personal To-Do tasks.',
    'author': 'Daniel Reis',
    'depends': ['base'],
    'data': [
      'security/ir.model.access.csv',
      'security/todo_access_rules.xml',
      'views/todo_view.xml',
      'views/todo_menu.xml',
      ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
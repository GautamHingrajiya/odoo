{
    'name' : 'Hospital Management',
    'version' : '17.0.1.0',
    'category' : 'Hospital',
    'sequence' : 0,
    'author' : 'Gautam',
    'summary' : 'Hospital Management System',
    'description' : """
            At the same time it is also used to minimize operating expenses and 
            improve the revenue cycle. In a nutshell, Hospital Management System (HMS)
            creates a frictionless approach to managing the entire hospital and solving operational complexities.
            However, HMS can be a complex system.""",
    
    'website': 'https://www.odoo.com',
    'depends' : [ 'base',
                  ],
    'data' : [
        'security/ir.model.access.csv',
        'views/view_hospital_patinet.xml',
        'views/menu.xml',
     ],
    'installable': True,
    'application': True,
    'auto_install' : False,
    'license' : 'LGPL-3',
}
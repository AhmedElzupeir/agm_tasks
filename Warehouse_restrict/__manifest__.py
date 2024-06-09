# -*- coding: utf-8 -*- 

{
	'name': 'Warehouse Riestrict Users',
	'version': '1.0',
	'license': 'LGPL-3',
	'auther': 'Ahmed Elzupeir Jebreel Mohammed',
	'category': 'Inventory',
	'depends':[
		'base','stock',
	],
	'data': [
		'security/warehouse_groups.xml',
		'views/users_views_inherit.xml',
		
	],
	'installable': True,
	'application': True,
}
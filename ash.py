#! /usr/bin/env python3

from collections import OrderedDict
import sys
import os

from peewee import *

db = SqliteDatabase('ash.db')

class BaseModel(Model):
	
	class Meta:
		database = db

class Project(BaseModel):
	project_name = CharField(unique=True)
	
class Context(BaseModel):
	context_name = CharField(unique=True)
	
class Task(BaseModel):
	task_name = CharField(unique=True)
	project = ForeignKeyField(Project, to_field=Project.project_name, null=True)
	#context = ForeignKeyField(Context, null=True)
	

def logo():
	print('''
	   _       _     
	  /_\  ___| |__  
	 //_\\\/ __| '_ \ 
	/  _  \__ \ | | |
	\_/ \_/___/_| |_|
	''')                                                                          
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                          

def initialize():
	'''Creates database and tabel if they don't exist'''
	db.connect()
	db.create_tables([Project, Context, Task], safe=True)	
	
def add_task():
	'''Add Task'''
	data_task_name = input('Task Name> ').strip()
	view_projects()
	data_project = input('Project Name> ').strip()
	#view_contexts()
	#data_context = input('Context Name> ').strip()
	
	if data_task_name:
		Task.create(task_name=data_task_name, project=data_project)
	
def view_tasks():
	'''View Tasks'''
	tasks = Task.select()
	print("Task\t\t\t Project")
	print("-"*60)
	for task in tasks:
		print('{} \t\t {}'.format(task.task_name, task.project.project_name))
	
def add_context():
	'''Add Context'''
	data = input('Please enter a context name> ').strip()
	
	if data:
		Context.create(context_name=data)
		view_contexts()
	
def view_contexts():
	'''View Contexts'''
	contexts = Context.select()
	print("---------------Contexts---------------")
	for context in contexts:
		print(context.context_name)
	
def add_project():
	'''Add Project'''
	data = input('Please enter a project name> ').strip()
	
	if data:
		Project.create(project_name=data)
		view_projects()
	
def view_projects():
	'''View Projects'''
	projects = Project.select()
	print("---------------Projects---------------")
	for project in projects:
		print(project.project_name)
	
menu = OrderedDict([
	('AT', add_task),
	('VT', view_tasks),
	('AC', add_context),
	('VC', view_contexts),
	('AP', add_project),
	('VP', view_projects)])
	
def menu_loop():
	'''Show the Menu'''
	choice = None
	
	while choice != 'Q':
		print("\nEnter 'q' to quit.")
		for key, value in menu.items():
			print('{}) {} '.format(key, value.__doc__), end=' ')
		print("")
		choice = input('Action: ').upper().strip()
		
		if choice in menu:
			os.system('cls' if os.name == 'nt' else 'clear')
			menu[choice]()

if __name__ == '__main__':

	initialize()
	os.system('cls' if os.name == 'nt' else 'clear')
	logo()
	menu_loop()

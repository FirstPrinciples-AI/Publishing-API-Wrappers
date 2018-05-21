import config
import os
import subprocess
from flask import json

def create_project(API_key = config.API_key):
	a =  'curl -H "Content-Type: application/json" -X PUT http://developers.mtonomy.com/create_project?key='+API_key
	project_id = subprocess.check_output(a,shell=True)
	return project_id

def upload_file(path_to_file, project_id, API_key = config.API_key):

	assert os.path.isfile(path_to_file)
	return subprocess.check_output('curl -i -X POST "Content-Type: multipart/mixed" -F name=Test -F filedata=@'+path_to_file+' http://developers.mtonomy.com/upload_file/'+str(project_id)+'?key='+API_key,shell=True)


def update_metadata(json_dict, project_id, API_key = config.API_key):
	data = json.dumps(json_dict)

	return subprocess.check_output('curl -H "Content-Type: application/json" -X POST -d ' + "'" + data + "'" + ' http://developers.mtonomy.com/update_metadata/'+str(project_id)+'?key='+API_key, shell = True)

def accept_terms(list_of_project_acceptance_tuples, API_key = config.API_key):
	i = 0
	dic = {}
	for entry in list_of_project_acceptance_tuples:
		dic[str(i)] = {"project_id": entry[0], "terms_approval": entry[1]}
	data = json.dumps(dic)
	return subprocess.check_output('curl -H "Content-Type: application/json" -X PUT -d ' + "'" + data + "'" +  ' http://developers.mtonomy.com/accept_terms?key='+API_key, shell=True)


def publish_project(project_id, API_key = config.API_key):
	return subprocess.check_output('curl -H "Content-Type: application/json" -X PUT http://developers.mtonomy.com/publish_project/' + str(project_id) + '?key=' + API_key, shell=True)
 

def check_terms_approval(project_id, API_key = config.API_key):
	return subprocess.check_output('curl http://developers.mtonomy.com/check_terms_approval/'+str(project_id) + '?key=' + API_key,shell=True)


def get_team_info(project_id, API_key = config.API_key):
	return subprocess.check_output('curl -H GET http://developers.mtonomy.com/get_team_info/'+str(project_id)+'?key='+API_key, shell=True)

def change_ownership_shares(list_of_email_ownership_tuples, project_id, API_key = config.API_key):
	i = 0
	dic = {}
	for entry in list_of_email_ownership_tuples:
		dic[str(i)] = {"email": entry[0], "ownership": entry[1]}

	data = json.dumps(dic)
	return subprocess.check_output('curl -H "Content-Type: application/json" -X PUT -d ' + "'" + data + "'" +  '  http://developers.mtonomy.com/change_ownership_shares/'+str(project_id)+ '?key='+API_key, shell=True)
def change_permissions(list_of_email_permissions_tuples, project_id, API_key = config.API_key):
	i = 0
	dic = {}
	for entry in list_of_email_permissions_tuples:
		dic[str(i)] = {"email": entry[0], "permissions": entry[1]}

	data = json.dumps(dic)
	print data
	print 'curl -H "Content-Type: application/json" -X PUT -d ' + "'" + data + "'" +  '  http://developers.mtonomy.com/change_permissions/'+str(project_id)+ '?key='+API_key
	return subprocess.check_output('curl -H "Content-Type: application/json" -X PUT -d ' + "'" + data + "'" +  '  http://developers.mtonomy.com/change_permissions/'+str(project_id)+ '?key='+API_key, shell=True)


def change_credits(list_of_email_credits_tuples, project_id):
	i = 0
	dic = {}
	for entry in list_of_email_ownership_tuples:
		dic[str(i)] = {"email": entry[0], "credits": entry[1]}

	data = json.dumps(dic)
	return subprocess.check_output('curl -H "Content-Type: application/json" -X PUT -d ' + "'" + data + "'" +  '  http://developers.mtonomy.com/change_credits/'+str(project_id)+ '?key='+API_key, shell=True)


def upload_art(path_to_file, project_id, API_key = config.API_key):

	assert os.path.isfile(path_to_file)
	return subprocess.check_output('curl -i -X POST "Content-Type: multipart/mixed" -F name=Test -F filedata=@'+path_to_file+' http://developers.mtonomy.com/upload_art/'+str(project_id)+'?key='+API_key,shell=True)


def invite_team_members(list_of_email_permissions_credits_tuples,project_id,API_key=config.API_key):
	i = 0
	dic = {}
	for entry in list_of_email_permissions_credits_tuples:
		dic[str(i)] = {"email": entry[0], "permissions": entry[1], "credits" : entry[2]}
	data = json.dumps(dic)
	print data
	return subprocess.check_output('curl -H "Content-Type: application/json" -X PUT -d ' + "'" + data + "'" + ' http://developers.mtonomy.com/invite_team_members/'+str(project_id) + '?key=' + API_key,shell=True)


def delete_project(project_id, API_key=config.API_key):
	return subprocess.check_output('curl -H "Content-Type: application/json" -X PUT http://developers.mtonomy.com/delete_project/'+str(project_id)+'?key='+API_key,shell=True)


def get_metadata(project_id):
	return subprocess.check_output('curl -H GET http://developers.mtonomy.com/get_metadata/' + str(project_id),shell=True)




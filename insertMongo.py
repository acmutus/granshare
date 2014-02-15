from pymongo import MongoClient
client = MongoClient()
db=client.costSharingDatabase
collection=db.groups

recordGroup1={"groupName":"group1",
		"groupList":['+12153501452','+12152758878']}
recordGroup2={"groupName":"Alican",
		"groupList":['+12152758878']}
recordGroup3={"groupName":"Guillermo",
		"groupList":['+12153501452']}

posts=db.posts
post_id=posts.insert(recordGroup1)
post_id=posts.insert(recordGroup2)
post_id=posts.insert(recordGroup3)

collection=db.user

recordUser1 = {"userName":"Guillermo","password":"pennapps","phoneNumber":'+12153501452'}
recordUser2 = {"userName":"Alican","password":"pennapps","phoneNumber":'+12152758878'}

posts=db.userPosts
post_id=posts.insert(recordUser1)
post_id=posts.insert(recordUser2)

print db.collection_names()

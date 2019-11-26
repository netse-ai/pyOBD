from firebase import firebase
firebase = firebase.FirebaseApplication('https://planit-a12ac.firebaseio.com', None)
new_user = 'Ozgur Vatansever'

result = firebase.post('/obdii', new_user, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print result

# class FirebaseController(object):
	# def __init__(self):
	# 	pass
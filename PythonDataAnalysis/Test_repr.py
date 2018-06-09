#conding=utf-8
class Message:
	def __init__(self,msg):
		self.msg = msg
	# def __repr__(self):
	# 	return "Message : %s" % self.msg

x = Message("Ipython NoteBook")
print(x)
print(x.msg)

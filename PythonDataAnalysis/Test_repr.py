#conding=utf-8
class Message:
	def __init__(self,msg):
		self.msg = msg

		return 1

	def __repr__(self):
		return "Message : %s" % self.msg

x = Message("Ipython NoteBook")
print(x)
print(x.msg)

x = 5
y = 7
if x > 5:
	x+=1

	y=8
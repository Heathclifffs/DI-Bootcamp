class Phone():
	def __init__(self,name):
		self.name=name	
		self.call_history=[]
		self.messages=[]

	def add(self,string):
		self.call_history.append(string)
	
	def add2(self,string):
		self.messages.append(string)

	def name(self):
		return self.name

	def Call(self,other_phone1,other_phone):
		cname='you have call '+other_phone1
		rname='you receive a call from '+self.name
		self.call_history.append(cname)
		other_phone.add(rname)
		
	def show_call_history(self):
		for i in self.call_history:
			print(i)

	def send_message(self,other_phone1,other_phone,content):
		dic={'to':other_phone1,'content':content}
		self.messages.append(dic)
		dic2={'from':self.name,'content':content}
		other_phone.add2(dic2)
	def show_messages(self):
		for i in self.messages:
			print(i)
			
	def show_outgoing_messages(self):
		for i in self.messages:
			for j in i.keys():
				if j=='to':
					print(i)
	def show_incoming_messages(self):
		for i in self.messages:
			for j in i.keys():
				if j=='from':
					print(i)


Harold=Phone('Harold')
Ezekiel=Phone('Ezekiel')
Harold.Call(Ezekiel.name,Ezekiel)
Harold.send_message(Ezekiel.name,Ezekiel,'Hi guy How are u')
Ezekiel.send_message(Harold.name,Harold,'Yeah guy i\'m okay and u ')
Harold.send_message(Ezekiel.name,Ezekiel,'I\'m pretty fine what\'s going on ? long time ago')
Ezekiel.send_message(Harold.name,Harold,'ohhhh that\'s right man i\'m pretty busy those time ')
Harold.send_message(Ezekiel.name,Ezekiel,'Ahh I see , then let\'s see us on friday ')
Ezekiel.send_message(Harold.name,Harold,'Okay let\'s do it')
Harold.send_message(Ezekiel.name,Ezekiel,'Nice')
Ezekiel.Call(Harold.name,Harold)
print('\n')
print("Harold call history :")
Harold.show_call_history()
print('\n')
print("Ezekiel call history :")
Ezekiel.show_call_history()
print('\n')
print("Harold messages : ")
Harold.show_messages()
print("outgoings : ")
Harold.show_outgoing_messages()
print("incomings : ")
Harold.show_incoming_messages()
print('\n')
print("Ezekiel messages : ")
Ezekiel.show_messages()
print("outgoings : ")
Ezekiel.show_outgoing_messages()
print("incomings : ")
Ezekiel.show_incoming_messages()












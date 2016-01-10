class Person(object):
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName
	def getFirstName(self):
		return self.firstName
	def getLastName(self):
		return self.lastName
	def __str__(self):
		return 'Person: %s %s' %(self.firstName, self.lastName)
	def say(self, toWhom, something):
		return self.firstName + self.lastName + ' says to ' + toWhom.firstName + toWhom.lastName + ' : ' + something
	def sing(self, toWhom, something):
		return self.say(toWhom, something + 'tra la la')


class MITPerson(Person):
	nextIdNum = 0
	def __init__(self, firstName, lastName):
		Person.__init__(self, firstName, lastName)
		self.idNum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1
	def getIdNum(self):
		return self.idNum
	def __str__(self):
		return 'MIT Person: %s %s' %(self.firstName, self.lastName)
	def __cmp__(self, other):
		return cmp(self.idNum, other.idNum)

class UG(MITPerson):
	def __init__(self, firstName, lastName):
		MITPerson.__init__(self, firstName, lastName)
		self.year = None
	def setYear(self, year):
		if year > 5: raise OverflowError('Too many')
		self.year = year
	def getYear(self):
		return self.year
	def say(self, toWhom, something):
		return MITPerson.say(self, toWhom, 'Excuse me, but ' + something)

class Prof(MITPerson):
	def __init__(self, firstName, lastName, rank):
		MITPerson.__init__(self, firstName, lastName)
		self.rank = rank
		self.teaching = {}
	def addTeaching(self, term, subj):
		try:
			self.teaching[term].append(subj)
		except KeyError:
			self.teaching[term] = [subj]
	def getTeaching(self, term):
		try:
			return self.teaching[term]
		except KeyError:
			return None
	def lecture(self, toWhom, something):
		return self.say(toWhom, something + ' as it is obvious')
	def say(self, toWhom, something):
		if type(toWhom) == UG:
			return MITPerson.say(self, toWhom, 'I do not understand why you say ' + something)
		elif type(toWhom) == Prof:
			return MITPerson.say(self, toWhom, 'I really liked your paper on ' + something)
		else:
			return self.lecture(toWhom, something)

class Faculty(object):




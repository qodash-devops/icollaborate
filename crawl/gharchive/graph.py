import neomodel as neo

neo.config.DATABASE_URL = 'bolt://neo4j:gitcontrib@localhost:7687'


class Contribution(neo.StructuredRel):
	time = neo.DateTimeProperty()
	contribtype = neo.StringProperty()
	comment=neo.StringProperty()

class Repo(neo.StructuredNode):
	name = neo.StringProperty()
	url = neo.StringProperty(unique_index=True)
	readme=neo.StringProperty()
	description=neo.StringProperty()

class Actor(neo.StructuredNode):
	git_id = neo.StringProperty(unique_index=True)
	login = neo.StringProperty(unique_index=True)
	visible_login= neo.StringProperty()
	contributed = neo.RelationshipTo('Repo','CONTRIBUTED',model=Contribution)


if __name__ == '__main__':
	A=Actor(id=1,login='test')
	A.save()
	R=Repo(name='testr',url='url')
	R.save()
	pass

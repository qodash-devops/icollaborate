import neomodel as neo
import os
neo.config.DATABASE_URL = os.environ.get('NEO4J_URL','bolt://neo4j:gitcontrib@localhost:7687')

###############################################################
# Data model
######################################
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


##################################################
# static queries
#####################################
def get_repo_urls():
	query="""
	MATCH (repo:Repo) RETURN repo.url
	"""
	results, meta = neo.db.cypher_query(query)
	return list(set(sum(results, [])))
def get_repo_url_missing_readme():
	query = """
		MATCH (repo:Repo)
		WHERE NOT EXISTS(repo.readme)
		RETURN repo.url
		"""
	results, meta = neo.db.cypher_query(query)
	return list(set(sum(results, [])))




if __name__ == '__main__':
	get_repo_url_missing_readme()
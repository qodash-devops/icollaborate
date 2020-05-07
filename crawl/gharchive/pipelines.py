from .graph import Repo,Actor,Contribution
from datetime import datetime

class GharchiveEventPipeline:
    def process_item(self, item, spider):
        assert spider.name=='ghevent'
        repo=Repo()
        repo.name=item['data']['repo']['name']
        repo.url=item['data']['repo']['url']
        repo.save()

        actor=Actor()
        actor.git_id=item['data']['actor']['id']
        actor.login=item['data']['actor']['login']
        actor.visible_login=item['data']['actor']['display_login']
        actor.save()
        contrib=actor.contributed.connect(repo)
        contrib.time=datetime.strptime(item['data']['created_at'],'%Y-%m-%dT%H:%M:%SZ')
        contrib.contribtype=item['data']['type']
        if 'commits' in item['data']['payload'].keys():
            if len(item['data']['payload']['commits'])>0:
                contrib.comment=item['data']['payload']['commits'][0]['message']
        contrib.save()






        return item



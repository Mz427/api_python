import requests
from plotly.graph_objs import Bar
from plotly import offline

######################################################################################
#                                  Get source data.                                  #
######################################################################################

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept" : "application/vnd.github.v3+json"}

r = requests.get(url, headers = headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")
#['total_count', 'incomplete_results', 'items']

repo_dicts = response_dict["items"]
print(f"Amount of items: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
#for i in sorted(repo_dict.keys()):
#    print(i)
for i in repo_dicts:
    print(f"\nName: {i['name']}")
    print(f"Owner: {i['owner']['login']}")
    print(f"Stars: {i['stargazers_count']}")
    print(f"Repository: {i['html_url']}")
    print(f"Created: {i['created_at']}")
    print(f"Updated: {i['updated_at']}")
    print(f"Description: {i['description']}")

######################################################################################
#                                  Draw data                                         #
######################################################################################



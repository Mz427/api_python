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
repo_names, stars = [], []
for i in repo_dicts:
    repo_names.append(i['name'])
    stars.append(i['stargazers_count'])

#repo_dict = repo_dicts[0]
#print(f"\nKeys: {len(repo_dict)}")
##for i in sorted(repo_dict.keys()):
##    print(i)
#for i in repo_dicts:
#    print(f"\nName: {i['name']}")
#    print(f"Owner: {i['owner']['login']}")
#    print(f"Stars: {i['stargazers_count']}")
#    print(f"Repository: {i['html_url']}")
#    print(f"Created: {i['created_at']}")
#    print(f"Updated: {i['updated_at']}")
#    print(f"Description: {i['description']}")

######################################################################################
#                                  Draw data                                         #
######################################################################################

data = [{
    'type' : 'bar',
    'x' : repo_names,
    'y' : stars,
    'marker' : {
        'color' : 'rgb(60, 100, 150)',
        '' : {}
    }
    }]
my_layout = {
        'title' : 'GitHub上最受欢迎的项目',
        'xaxis' : {'title' : 'Repository'},
        'yaxis' : {'title' : 'Stars'}
        }
fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='python_repo.html')

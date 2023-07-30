import requests
FILENAME = "list"
with open(FILENAME, 'r') as f:
    urls = f.read().splitlines()

reachable_urls = []
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        reachable_urls.append(url)
    except:
        pass

with open(FILENAME, 'w') as f:
    for url in reachable_urls:
        f.write(url + '\n')

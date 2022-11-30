# news-websites
List of news websites from all around the world

Extracted manually and cleaned up using

```python
urlSet = set()
with open("urls.list") as f:
    lines = f.readlines()
    for l in lines:
        l = l.replace("\n", "")
        if not ("feedspot" in l or "javascript" in l or "youtube" in l or "facebook" in l):
            urlSet.add(l)

with open("list", "a") as f:
    for u in urlSet:
        f.write(u+"\n")
```

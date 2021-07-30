# jsondb
An online json database for users to use

ever wanted to store json anywhere but locally?

This is your product then!

### Explanation:



Example:
```python
import jsondb



db = jsondb.connect(
	{
		"server": "https://jsondb.eris9.repl.co", # or put your own server 
		"key": f"", # insert key
		"pwd": "12345"
	}
)

print(db)
db["test2"] = ["e","f","g"]
jsondb.write(db)
```

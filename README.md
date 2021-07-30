# jsondb
An online json database for users to use

ever wanted to store json anywhere but locally?

This is your product then!

### Explanation:
Server.py - The API server which holds the data and sends/writes the data too.
Jsondb - The module made to utilise the API


### Examples:

Creation:
```python
import jsondb
key = jsondb.create({
	"name":"my db",
	"pwd": "12345"
})
```

Connection:
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
```

Writing:

```python
import jsondb



db = jsondb.connect(
	{
		"server": "https://jsondb.eris9.repl.co", # or put your own server 
		"key": f"", # insert key
		"pwd": "12345"
	}
)

db["key"] = "value"
jsondb.write(db)
```

# jsondb
An online json database for users to use

ever wanted to store json anywhere but locally?

This is your product then!

COnnection:

```python
db = jsondb.connect(
	{
		"server": "https://jsondb.eris9.repl.co",
		"key": f"himuqz2yks93e8vawick9wgiwedk1s",
		"pwd": "12345"
	}
)

print(db)
db["test2"] = ["e","f","g"]
jsondb.write(db)
```

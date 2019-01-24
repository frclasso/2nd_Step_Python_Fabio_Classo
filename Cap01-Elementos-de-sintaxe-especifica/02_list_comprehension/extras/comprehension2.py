"""In fact, lists, sets, dictionaries, and generators can all
be built with comprehensions """

print([ord(x)for x in 'spam']) # List of character ordinals
print({ord(x)for x in 'spam'}) # Set
print({x : ord(x)for x in 'spam'}) # Dictionary
print((ord(x)for x in 'spam')) # Generator of values

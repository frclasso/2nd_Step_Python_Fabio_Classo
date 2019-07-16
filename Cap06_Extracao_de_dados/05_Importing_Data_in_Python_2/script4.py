# Import packages
from urllib.request import urlopen, Request

# Specify the url
#url = "http://www.datacamp.com/teach/documentation"
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'


# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()

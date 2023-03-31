# Yelp-API-Search

This project can search and display information about businesses assuming the consumer provides proper information, which includes but is not limited to; name, city, business id, or phone number. 

Want to see the program run without cloning the repository? Watch the video below.

**_Note: Turn volume on_**, it is a vocal and visual demonstration.

Video Link: https://drive.google.com/file/d/1WRSJs5tolbJ3ibjORpi_-MV9y0vzXp96/view?usp=sharing

## Difficulties encountered and their solutions below

### Project Difficulties

1) ValueError message appeared if the consumer entered incorrect information(Ex: letters when numbers are expected)

2) Requesting information from the API and executing code based on the response

3) Deciphering the wanted information from the JSON object after requests were accepted

### Solutions:

1) Using try/except blocks to show an error messages that I wrote

2) Researching the API reference page on Yelp’s developer portal to understand their status codes

3) Since the JSON object gets saved as a hashmap, I isolated the hashmap values and extracted the wanted information using subscripts

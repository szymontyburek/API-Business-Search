# Yelp-API-Search

Code that uses the Yelp REST API to help connect consumers and great local businesses.

Want to see the program run without cloning the repository? Watch the video below.

NOTE: TURN VOLUME ON, it is a vocal and visual demonstration.

LIVE DEMO LINK HERE

PROJECT DIFFICULTIES:

ValueError message appeared if the consumer entered incorrect information(Ex: letters when numbers are expected)

Requesting information from the API and executing code based on the response

Deciphering the wanted information from the JSON object after requests were accepted

SOLUTIONS:

Using try/except block to show an error message that I wrote

Researching the API reference page on Yelp’s developer portal to understand their status codes

Since the JSON object gets saved as a hashmap, I isolated the hashmap values and extracted the wanted information using subscripts

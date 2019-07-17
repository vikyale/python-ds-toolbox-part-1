"""
In the filter() call, pass a lambda function and the sequence 
of tweets as strings, tweets_df['text']. The lambda function
should check if the first 2 characters in a tweet x are 'RT'.
Assign the resulting filter object to result. 

To get the first 2 characters in a tweet x, use x[0:2]. 
To check equality, use a Boolean filter with ==.

Convert result to a list and print out the 
list.

"""

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
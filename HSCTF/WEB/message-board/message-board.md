# message-board

Logging in with the provided credentials, we are given a page that ends with no flag for you. 

Also, if we check the cookies header, there is an auth token which is `Set-Cookie: userData=j%3A%7B%22userID%22%3A%22972%22%2C%22username%22%3A%22kupatergent%22%7D; Path=/`. 

Running it through a URL decoder for ease of reading, it is `j:{"userID":"972","username":"kupatergent"}.`

I noticed that the cookie value is checked for the admin ID and the admin username. 

However, the source code only provides the admin username, which is admin. 

So we have to guess the admin ID to get the flag.

Usually web challenges don’t require / forbid bruteforcing. [code_here](Solution.py)

Admin user is 768. The output will be written to a file grep the file with `strings <filename> | grep flag{`

Flag:- ``flag{y4m_y4m_c00k13s}``

# req
Ever came accross a situation where if you normally [requests](https://pypi.org/project/requests/) or curl a site programatically but it doesn't reflect on site (if thats a functionality) or it isn't enough. Then this script can be used to request sites while removing the hassle of including headers by yourself.

Just capture the request in burp or zap proxy and save it in a text file and emulate it as many times as you want.

# usage
```
usage: req.py [-h] -f FILE [-t TIMES] [-p]

Send custom HTTP requests from a file multiple times.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to the request file
  -t TIMES, --times TIMES
                        Number of times to send the request (default: 1)
  -p, --printcode       Prints status code for each request
```

### cases where req.py can be used
- Including every header in tools like curl seems too much of a hassle
- you want to send these requests n number of times and just want to observe behaviour

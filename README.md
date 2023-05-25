# website-evaluator-crawler

A crawler which provides information about the structure of a website. How pages on the website are connected and the status code of their connection.
The result is send back in JSON format.

## Installation

To run this project localy follow the instructions bellow.
### Clone

Clone this repo to your local machine

### Setup

> make sure you are running the newest version of python or at least python3

> after that install scrapy
```shell
$ pip install scrapy
```

> now install scrapyrt

```shell
$ pip install scrapyrt
```
> navigate to the root of the cloned project and run 

```shell
$ scrapyrt -p _port_
```

> to run the crawler call the url below with the wanted parameters  
```
localhost:_port_/crawl.json?spider_name=linkspider&start_requests=true&domain=_domain_&starturl=_url_ in your browser
```

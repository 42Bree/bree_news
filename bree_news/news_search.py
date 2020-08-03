from elasticsearch import Elasticsearch

from elasticsearch import Elasticsearch


def search_keyword(keyword, operator, start=None, end=None):
    es = Elasticsearch("13.125.148.208:9200", timeout=30)

    body = {
        "_source": [
            "images",
            "writer",
            "regdate",
            "cpname",
            "html",
            "moddate",
            "body",
            "title",
            "category",
            "url",
        ],
        "size": 100,
        "from": 0,
        "min_score": 5,
        "sort": [],
        "query": {

        }
    }
    if keyword:
        if operator == ["정확도순"]:
            if start != None:
                if end != None:
                    body['sort'] = "_score", {"regdate": {"order": "desc"}}
                    body['query']['bool'] = {"must": [{"multi_match": {"query": f"{keyword}", "fields": ["title.raw^20","title^15", "body.raw^5" "body"], "tie_breaker": 0.3}},{"range": {"regdate": {"gte": f"{start}", "lte": f"{end}"}}}]}
                else:
                    body['sort'] = "_score", {"regdate": {"order": "desc"}}
                    body['query']['bool'] = {"must": [
                        {"multi_match": {"query": f"{keyword}", "fields": ["title.raw^20","title^15", "body.raw^5" "body"], "tie_breaker": 0.3}},
                        {"range": {"regdate": {"gte": f"{start}", "lte": "now/d"}}}]}
            else:
                if end != None:
                    body['sort'] = "_score", {"regdate": {"order": "desc"}}
                    body['query']['bool'] = {"must": [
                        {"multi_match": {"query": f"{keyword}", "fields": ["title.raw^20","title^15", "body.raw^5" "body"], "tie_breaker": 0.3}},
                        {"range": {"regdate": {"gte": "20150101", "lte": f"{end}"}}}]}
                else:
                    body['sort'] = "_score", {"regdate": {"order": "desc"}}
                    body['query']['multi_match'] = {"query": f"{keyword}", "fields": ["title.raw^20","title^15", "body.raw^5", "body"],"tie_breaker": 0.3}

        else:
            if start != None:
                if end != None:
                    body['sort'] = {"regdate": {"order": "desc"}}, "_score"
                    body['query']['bool'] = {"must": [{"multi_match": {"query": f"{keyword}", "fields": ["title^100", "body"]}},{"range": {"regdate": {"gte": f"{start}", "lte": f"{end}"}}}]}
                else:
                    body['sort'] = {"regdate": {"order": "desc"}}, "_score"
                    body['query']['bool'] = {
                        "must": [{"multi_match": {"query": f"{keyword}", "fields": ["title^100", "body"]}},
                                 {"range": {"regdate": {"gte": f"{start}", "lte": "now/d"}}}]}
            else:
                if end != None:
                    body['sort'] = {"regdate": {"order": "desc"}}, "_score"
                    body['query']['bool'] = {
                        "must": [{"multi_match": {"query": f"{keyword}", "fields": ["title^100", "body"]}},
                                 {"range": {"regdate": {"gte": "20150101", "lte": f"{end}"}}}]}
                else:
                    body['sort'] = {"regdate": {"order": "desc"}}, "_score"
                    body['query']['multi_match'] = {"query": f"{keyword}", "fields": ["title^100", "body"]}

    response = es.search(index="bree_news", body=body)
    print(body)
    print(response)
    hits = response['hits']['hits']
    total = response['hits']['total']['value']

    return hits, total


def search_writer(writer, operator, start=None, end=None):
    es = Elasticsearch("13.125.148.208:9200", timeout=30)

    body = {
        "_source": [
            "images",
            "writer",
            "regdate",
            "cpname",
            "html",
            "moddate",
            "body",
            "title",
            "category",
            "url",
        ],
        "size": 100,
        "from": 0,
        "min_score": 5,
        "sort": [],
        "query": {
        }
    }
    if writer:
        if operator == ["정확도순"]:
            if start != None:
                if end != None:
                    body['sort'] = "_score", {"regdate": {"order": "desc"}}
                    body['query']['bool'] = {"must": [{"match": {"writer": {"query": f"{writer}", "boost": "2"}}},{"range": {"regdate": {"gte": f"{start}", "lte": f"{end}"}}}]}
                else:
                    body['sort'] = "_score", {"regdate": {"order": "desc"}}
                    body['query']['bool'] = {"must": [{"match": {"writer": {"query": f"{writer}", "boost": "2"}}},{"range": {"regdate": {"gte": f"{start}", "lte": "now/d"}}}]}
            else:
                if end != None:
                    body['sort'] = "_score", {"regdate": {"order": "desc"}}
                    body['query']['bool'] = {"must": [{"match": {"writer": {"query": f"{writer}", "boost": "2"}}},{"range": {"regdate": {"gte": "20150101", "lte": f"{end}"}}}]}
                else:
                    body['sort'] = "_score", {"regdate": {"order": "desc"}}
                    body['query']['match'] = {"writer": {"query": f"{writer}", "boost": "2"}}
        else:
            if start != None:
                if end != None:
                    body['sort'] = {"regdate": {"order": "desc"}}, "_score"
                    body['query']['bool'] = {"must": [{"match": {"writer": {"query": f"{writer}", "boost": "2"}}},
                                                  {"range": {"regdate": {"gte": f"{start}", "lte": f"{end}"}}}]}
                else:
                    body['sort'] = {"regdate": {"order": "desc"}}, "_score"
                    body['query']['bool'] = {"must": [{"match": {"writer": {"query": f"{writer}", "boost": "2"}}},
                                                  {"range": {"regdate": {"gte": f"{start}", "lte": "now/d"}}}]}
            else:
                if end != None:
                    body['sort'] = {"regdate": {"order": "desc"}}, "_score"
                    body['query']['bool'] = {"must": [{"match": {"writer": {"query": f"{writer}", "boost": "2"}}},
                                                  {"range": {"regdate": {"gte": "20150101", "lte": f"{end}"}}}]}
                else:
                    body['sort'] = {"regdate": {"order": "desc"}}, "_score"
                    body['query']['match'] = {"writer": {"query": f"{writer}", "boost": "2"}}

    response = es.search(index="bree_news", body=body)
    print(response)
    hits = response['hits']['hits']
    total = response['hits']['total']['value']

    return hits, total

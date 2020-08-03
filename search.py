from elasticsearch import Elasticsearch
import json


def issue(original = None, typo = [], op=None, corrected=None):
    es = Elasticsearch("13.125.148.208:9200", timeout=30)
    print(typo)
    if typo == []:
        typo = ["누락", "첨가", "대치", "오형태"]
    body = {
        "_source": [
            "id",
            "왼쪽문맥",
            "중심어",
            "교정형태1",
            "오른쪽문맥",
            "교정정보",
            "교정결과",
            "원형태",
            "교정형태2",
            "오류위치",
            "오류양상"
        ],
        "size": 10000,
        "from": 0,
        "query": {
            "bool": {
                "filter": [{
                    "terms": {
                        "오류양상": []
                    }
                }]
            }
        }
    }
    if original is not None:
        if corrected is not None:
            if op == "AND":
                body['query']['bool']['filter'].append({"term": {"원형태": f"{original}"}})
                body['query']['bool']['filter'].append({"term": {"교정형태2": f"{corrected}"}})
            elif op == "OR":
                body['query']['bool']['should'] = [{"term": {"원형태.keyword": {"value": f"{original}"}}},{"term": {"교정형태2.keyword": {"value": f"{corrected}"}}}]
                body["min_score"] = 1.0
            else:
                print("Invalid")
        else:
            body['query']['bool']['filter'].append({"term": {"원형태": f"{original}"}})
    else:
        if corrected is not None:
            body['query']['bool']['filter'].append({"term": {"교정형태2": f"{corrected}"}})

    body['query']['bool']['filter'][0]['terms'].update({"오류양상": typo})
    print(body)
    response = es.search(index="oryu", body=body)

    hits = response['hits']['hits']
    total = response['hits']['total']['value']

    return hits, total






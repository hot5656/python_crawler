from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"usersSearchTerm":"Miami, FL","mapBounds":{"west":-80.57360942236328,"east":-80.11424357763671,"south":25.454660058661617,"north":25.95086011682646},"mapZoom":11,"regionSelection":[{"regionId":12700,"regionType":6}],"isMapVisible":true,"filterState":{"isAllHomes":{"value":true},"sortSelection":{"value":"globalrelevanceex"}},"isListVisible":true}&wants={"cat1":["listResults","mapResults"],"cat2":["total"]}&requestId=11'

def cookie_parser():
    cookie_string = 'x-amz-continuous-deployment-state=AYABeDozRAV4eBXn53GdUx6C9KgAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3NjA0OTUxU1JKRU1BTUNBQVQzAAEAAkNEABpDb29raWUAAACAAAAADC9y+riaM3c3VfjKUAAwXCaGW/6iO5TPw8+8vr3zoO5Nm7gd7DMZXK6okhU6K4kXoDVBO7HQkgndLPjGKo4CAgAAAAAMAAQAAAAAAAAAAAAAAAAAAKRBZtCjtenvMrrXJ21YNeT/////AAAAAQAAAAAAAAAAAAAAAQAAAAwn7mUR/7TtksDHHX6SB512jDCPuGS6ClsF14KQ; zguid=24|$c77aeb82-e78d-4e30-ae12-99ebf68ee40c; zgsession=1|d0f96001-207d-4fdb-bc2b-2d4be8481046; _ga=GA1.2.1397835228.1673488949; _gid=GA1.2.1392148737.1673488949; _gcl_au=1.1.707741217.1673488949; DoubleClickSession=true; pxcts=2b34b09f-921d-11ed-9ef7-416e57565558; _pxvid=2b34a325-921d-11ed-9ef7-416e57565558; zjs_user_id=null; zg_anonymous_id="b34e8cc3-5223-446e-be30-4bb02c3f16c7"; zjs_anonymous_id="c77aeb82-e78d-4e30-ae12-99ebf68ee40c"; _hp2_ses_props.1215457233={"r":"https://www.udemy.com/","ts":1673488949665,"d":"www.zillow.com","h":"/"}; __pdst=93d52dc143ff4390b5e3c46cd07b71e3; x-amz-continuous-deployment-state=AYABeCJlyJdglRcW44yIXtMgRU0APgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3NjA0OTUxU1JKRU1BTUNBQVQzAAEAAkNEABpDb29raWUAAACAAAAADL6HylRuDyuSPbH/JwAwaG9tc3uBrUyu48OcxzPbGkl5XZ3L/GFyLiutjfLpmpYArElg94NrLtKKYNluKzmPAgAAAAAMAAQAAAAAAAAAAAAAAAAAALr2tHNqrBFYnWHoUSWpCLj/////AAAAAQAAAAAAAAAAAAAAAQAAAAy6JJY4RtjOs8beE4GBohIG2l+Yn9W4htTJqrFU+Yn9W4htTJqrFQ==; _pin_unauth=dWlkPVpqUmlZMlV3T0dVdE5XTXhOeTAwWmpZekxUa3lOVFV0WldFd1pETmpNVFUyWmpRMA; _clck=4hz3dl|1|f87|0; JSESSIONID=D9E435E39B445602C1923F979D088C15; optimizelyEndUserId=oeu1673489175634r0.13015292888081653; pjs-last-visited-page=/z/partners/advertise/; pjs-pages-visited=1; zgcus_aeut=AEUUT_b28c7701-921d-11ed-9dab-3a95c7e2c366; zgcus_aeuut=AEUUT_b28c7701-921d-11ed-9dab-3a95c7e2c366; _hp2_id.1215457233={"userId":"5085169698155876","pageviewId":"8807131245796241","sessionId":"2283555925186672","identity":null,"trackerVersion":"4.0"}; _cs_c=0; _cs_id=c9bea19f-4027-a02c-e5f9-5a3ab7633656.1673489192.1.1673489192.1673489192.1.1707653192008; _cs_s=1.5.0.1673490993250; _uetsid=2c71f8b0921d11edbb6d9388673fe038; _uetvid=2c723860921d11edb6d5097fc0b68a9a; _px3=b03626a50efd6f68154fd96f2b688cfd8741166a7b6c0ca8de41525db6733ec5:jxFiCxYn9qDFakworMNR9SFED4MO3pUPQciDMIcuEdSrVBveo6SNJlocyBABjlfjlfMcRuBxZZXyU8GycBo7vA==:1000:kR36uvfMGwnioBR5KjuJcvEL8fWGFvW6X5Ts8oe4qdTgXjkgZCvUh+VoGePTouspDcFQhQxMrhyQOgA5WOZ/OGWk44drtFuGhammLIhxhX16n/gEG2XN4pQfnFQg7SjSvJfKwnh7U6CxdTQnBBOQfWHpNQjfT1MsX9+y8fWhrynC15uwzyqIvEK1CWo3QLMKK+AqisHkOppddCItkoHTsA==; _gat=1; AWSALB=HeiZWMjbDFkJz8j78noiZJAwrZgT3/uDQUW6pVzersXzeuGoj9Lv6rIOHHKffVhD4C1GjwWk37PQ+jXftDn9uiaC7oyHt59ZDuPQBrHuVAMcdwqyp1gw6bzWJLaX; AWSALBCORS=HeiZWMjbDFkJz8j78noiZJAwrZgT3/uDQUW6pVzersXzeuGoj9Lv6rIOHHKffVhD4C1GjwWk37PQ+jXftDn9uiaC7oyHt59ZDuPQBrHuVAMcdwqyp1gw6bzWJLaX; search=6|1676082449831|rect=25.95086011682646%2C-80.11424357763671%2C25.454660058661617%2C-80.57360942236328&rid=12700&disp=map&mdm=auto&p=2&z=1&fs=1&fr=0&mmm=0&rs=0&ah=0&singlestory=0&housing-connector=0&abo=0&garage=0&pool=0&ac=0&waterfront=0&finished=0&unfinished=0&cityview=0&mountainview=0&parkview=0&waterview=0&hoadata=1&zillow-owned=0&3dhome=0&featuredMultiFamilyBuilding=0&commuteMode=driving&commuteTimeOfDay=now		12700						; _clsk=1t385f3|1673490451095|16|0|m.clarity.ms/collect'
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}

    # print(cookie.items())
    for key, morsel in  cookie.items():
        cookies[key] = morsel.value

    # print(cookies)
    return cookies

def parse_new_url(url, page_number):
    url_parsed = urlparse(url)
    # convert string to dict
    query_string = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination'] = {'currentPage':page_number}
    query_string.get('searchQueryState')[0] = search_query_state
    # doseq=1, no change field sequencce
    encode_qs = urlencode(query_string, doseq=1)
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encode_qs}"
    return new_url

# cookie_parser()
# parse_new_url(URL, 6)

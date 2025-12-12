from crewai.tools import tool
import os
import urllib
import json

@tool('naver_news_search') 
def get_news_urls(query:str) :
    """Get news URLs related to a query from the Naver News search engine. Use this tool to search for news articles."""
    print(f"🚀 naver_news_search 도구 호출됨!")
    
    client_id = os.environ['NAVER_API_CLIENT_ID']
    client_secret = os.environ["NAVER_API_CLIENT_SECRET"]
    encText = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode==200):
        response_body = response.read()
        result = json.loads(response_body) 
        
        for i, item in enumerate(result['items'][:3]):
            title = item.get('title', 'N/A').replace('<b>', '').replace('</b>', '')
            # print(f"  {i+1}. {title}")
        
        return result['items']
    else:
        print("Error Code:" + rescode)
        return []
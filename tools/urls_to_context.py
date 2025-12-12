from newspaper import Article

from crewai.tools import tool

@tool('urls_to_context')
def get_article(urls:list):
    """Get news contexts from URLs"""    
    print(f"🚀 urls_to_context 도구 호출됨!")
    result = {'title': [], 'context': []}
    for i, url in enumerate(urls):
        # 기사 객체 생성
        try:
            article = Article(url)

            # 기사 다운로드 및 파싱
            article.download()
            article.parse()

            # 본문 내용 추출
            title = article.title
            text = article.text[:200] + "..." if len(article.text) > 200 else article.text
            result['title'].append(title)
            result['context'].append(article.text)
        except Exception as e:
            print(f"  ❌ 오류: {e}")
            result['title'].append("Error")
            result['context'].append("Error")
    return result
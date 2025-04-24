from duckduckgo_search import DDGS


def duckduckgo_search_query(query: str, max_results: int = 10):
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=max_results)]

        seen = set()
        dataframe = []
        for r in results:
            title = r.get("title", "")
            if title and title not in seen:
                seen.add(title)
                dataframe.append({"query": query, "answers": title})

        print(dataframe)

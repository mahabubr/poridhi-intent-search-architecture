from duckduckgo_search import DDGS
import pandas as pd


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

        new_data = pd.DataFrame(dataframe)

        output_file = "dataset/web_search_tune.csv"

        try:
            existing_data = pd.read_csv(output_file)

            updated_data = pd.concat([existing_data, new_data], ignore_index=False)

        except:
            updated_data = new_data

        updated_data.to_csv(output_file, index=False)

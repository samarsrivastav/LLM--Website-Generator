import requests
from langchain_core.documents import Document


urls = [
    "https://en.wikipedia.org/api/rest_v1/page/summary/Programming_language",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Software_development",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Software_testing",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Software_development_process",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Software_design",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Software_architecture",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Python_(programming_language)",
    "https://en.wikipedia.org/api/rest_v1/page/summary/JavaScript",
    "https://en.wikipedia.org/api/rest_v1/page/summary/C++",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Software_engineering",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Algorithm",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Data_structure",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Web_development",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Application_programming_interface",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Database",
    "https://en.wikipedia.org/api/rest_v1/page/summary/Object-oriented_programming",
   
]

docs = []
for url in urls:
    data = requests.get(url).json()
    docs.append(Document(page_content=data.get("extract", "")))
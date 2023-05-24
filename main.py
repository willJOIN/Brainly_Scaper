from bs4 import BeautifulSoup
import requests

def main():
    getAnswer(getBrainlyPage())

def getBrainlyPage() -> str:
    brainly = requests.get("https://brainly.com.br/")   

    # https://brainly.com.br/tarefa/55531509
    link = input('Cole o link da tarefa no Brainly:\n')

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua-arch::": "x86",
        "sec-ch-ua-mobile:": "?0",
        "sec-ch-ua-model:": "",
        "sec-ch-ua-platform:": "Windows",
        "sec-fetch-dest:": "document",
        "sec-fetch-mode:": "navigate",
        "sec-fetch-site:": "none",
        "sec-fetch-user:": "?1",
        "upgrade-insecure-requests:": "1",
        "user-agent:": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    }

    return requests.get(link, headers=headers)

def getAnswer(brainly_page) -> str:
    soup = BeautifulSoup(brainly_page.text, "html.parser")

    return soup.select('#answer_box_text')
    
main()

# pip install beautifulsoup4
# pip install requests
# python filename.py
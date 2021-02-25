import requests
from bs4 import BeautifulSoup


MOBILE_URL = "https://kyivstar.ua/ru/support/mobile_connection/sim_" \
             "and_number/kak-uznat-k-kakomu-operatoru-otnositsya-nomer"


def get_operator_codes():
    response = requests.get(MOBILE_URL)
    bs = BeautifulSoup(response.content, "html.parser")
    elements = bs.find("table", class_="data-text").find_all("p")
    res = []
    for elem in elements:
        temp = elem.string.split(", ")
        for i in range(len(temp)):
            if "*" in temp[i]:
                temp[i] = temp[i].replace("*", "")
            if temp[i].isnumeric():
                res.append(temp[i])
    return res


def generate_ukr_mobile_regex():
    op_codes = get_operator_codes()
    res = f"(?P<phone_number>({'|'.join(op_codes)})\d{'{7}'})/$"
    return res

from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency, amt):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amt}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_='ccOutputRslt').get_text()
    print(type(rate))
    # rateSimp = rate[0:-4]                     #can do math operations with float operant and string slicing helps get the reqd output
    # print(int(rateSimp))                       #getting errors, for now, disabled this.



def main():
    while True:
        fromCur = input("Please enter the currency from which you want to convert: ").upper()
        fromCurResp = fromCur.replace(" ", "")      #to replace all whitespaces with nothing
        toCur = input("Please enter the currency to which you want to convert: ").upper()
        toCurResp = toCur.replace(" ", "")
        val = input("Please enter the currency value that you wish to convert: ").upper()
        valResp = val.replace(" ", "")

        get_currency(fromCurResp, toCurResp, valResp)

        while True:
            resp = input("Do you wish to convert another currency(y/n)? ")
            response = resp.lower()
            if response == 'y':
                break
            elif response == 'n':
                exit()
            else:
                print('Please enter an appropriate value.')


main()


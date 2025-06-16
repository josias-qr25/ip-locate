import requests
import sys

def main():

    while True:

        ipAddr = input("IP Address or URL: ")
        info = input("[S]hort or [C]omplete information? ")
        urlShort = "http://ip-api.com/json/" + ipAddr + "?fields=country,regioName,city,lat,lon,isp"
        urlMore = "http://ip-api.com/json/" + ipAddr

        while True:
            if info.upper() == "S":
                response = requests.get(urlShort)
                print(response.text)

                while True:
                    option = input("[L]ocate another IP address, [W]rite to file, or [E]xit? ")
                    if option.upper() == "L":
                        break
                    elif option.upper() == "W":
                        with open(ipAddr + ".txt", "w") as file:
                            file.write(response.text)
                            print("Contents written to file.")
                            continue
                    elif option.upper() == "E":
                        sys.exit()
                    else:
                        print("Invalid response.")
                        continue

            elif info.upper() == "C":
                response = requests.get(urlMore)
                print(response.text)
                while True:
                    option = input("[L]ocate another IP address, [W]rite to file, or [E]xit? ")
                    if option.upper() == "L":
                        break
                    elif option.upper() == "W":
                        with open(ipAddr + ".txt", "w") as file:
                            file.write(response.text)
                            print("Contents written to file.")
                            continue
                    elif option.upper() == "E":
                        sys.exit()
                    else:
                        print("Invalid response.")
                        continue

            else:
                print("Invalid response.")
                continue

            break
            
if __name__ == "__main__":
    main()

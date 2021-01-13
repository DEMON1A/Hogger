import requests , optparse , concurrent.futures , subprocess
from os import path , mkdir
from time import sleep

Count = 1

def OptionsCollector():
    Parser = optparse.OptionParser()
    Parser.add_option("-u" , "--username" , dest="username" , help="The User's Github Username.")
    Parser.add_option("-d" , "--delay" , default="5" , dest="delay" , help="The Delay Between Every Scan.")
    Parser.add_option("-o" , "--output" , dest="output" , help="The Output Folder You Want To Save The Results On.")

    Options , _ = Parser.parse_args()
    return Options

def CollectRepos(Username):
    global Count
    Responses = []

    try:
        while (1):
            URL = f"https://api.github.com/users/{Username}/repos?per_page=100&page={Count}"
            Response = requests.get(URL , headers={"User-Agent":"Hogger Respositories Scrapper"} , timeout=20).json()
            Count += 1

            if "not_found" in Response:
                print("The User You Selected Isn't a Github User"); exit()
            elif str(Response) == "[]":
                # print("Count: {0}".format(str(Count)))
                break
            else:
                Responses.append(Response)

        return Responses
    except Exception as err:
        print("Can't Request Github Developer API")
        print("Error:" , str(err)); exit()

def Main(Options):
    if Options.username: Responses = CollectRepos(Options.username)
    else: print("You Didn't Select a Username"); exit()
    
    if not Options.output: Output = "output"
    if not path.exists(Output): mkdir(Output)
    if not path.exists(Output + f"/{Options.username}/"): mkdir(Output + f"/{Options.username}/")

    for Repos in Responses:
        for Repo in Repos:
            URL = Repo["clone_url"]
            print(f"Searching For Possible Leaks On {URL}")
            Process = subprocess.Popen(f"trufflehog --regex --entropy=False {URL}",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            Results = Process.communicate()[0].decode('UTF-8')
            Filename = URL.split('/')[-1].split('.')[0]
            
            if str(Results) != '':
                with open(Output + f"/{Options.username}/{Filename}.hogger" , 'w') as Log:
                    Log.write(Results)
                    print(f"Leaks Search is Done On {URL}")
            else:
                print(f"There's No Leaks Has Been Found On {URL}")

            print(f"Sleeping For {Options.delay} Seconds\n")
            sleep(int(Options.delay))

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as Collector:
        Options = Collector.submit(OptionsCollector)
        Options = Options.result()

    with concurrent.futures.ThreadPoolExecutor() as Threader:
        _ = Threader.submit(Main , Options)

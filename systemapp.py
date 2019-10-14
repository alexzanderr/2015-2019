
import webbrowser as webb
import os
import sys

class FavouriteSites:
    __sitesList = \
    [
        {"Programming" :
            [
                {"StackOverflow" : "https://stackoverflow.com/"},
                {"Programiz" : "https://www.programiz.com/"},
                {"NullByte" : "https://null-byte.wonderhowto.com/"},
                {"ProblemeInfo": "http://info.mcip.ro/"},
                {"InvataInfo": "https://invata.info"},
                {"ToptalDeveloper" : "https://www.toptal.com"},
                {"LaboratoarePoli" : "https://ocw.cs.pub.ro/courses/pa/laboratoare/laborator-01"},
                {"Epoch1" : "https://colab.research.google.com/github/bucharestschoolofai/python_crash_course/blob/master/Python%20Crash%20Course.ipynb#scrollTo=Y94RAfECV_2U"},
                {"Geeks4Geeks" : "https://www.geeksforgeeks.org/"},
                {"PbInfo" : "https://www.pbinfo.ro"},
                {"SoftPedia" : "https://forum.softpedia.com/topic/1094222-unibuc-2017-admitere-informatica/"},
                {"AndreiCiorba" : "http://andrei.clubcisco.ro/cursuri/"},
                {"RossetaCode" : "https://rosettacode.org/wiki/Category:Programming_Tasks"},
                {"Cplusplus" : "http://www.cplusplus.com"},
                {"FmiSubRezolvate" : "http://fmi.unibuc.ro/ro/pdf/2017/admitere/licenta/FMI_Rezolvari_admitere_2017.pdf"},
                {"HackTheBox" : "https://www.hackthebox.eu/home"},
                {"MicrosoftDocs" : "https://docs.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/types-and-variables"},
                {"InfoArena" : "https://infoarena.ro/operatii-pe-biti"},
                {"GitHub" : "https://github.com"},
                {"W3Schools" : "https://www.w3schools.com"},
                {"CodingGame": "https://www.codingame.com/start"},
                {"": ""},
                {"": ""},
                {"": ""},
                {"": ""}
            ]},

        {"Computers" :
            [
                {"HowToGeek" : "https://www.howtogeek.com/"},
                {"Filelist" : "https://filelist.ro/browse.php"},
                {"" : ""},
                {"" : ""},
                {"" : ""},


            ]},

        {"News" :
            [
                {"HackerNews" : "https://news.ycombinator.com"},
                {"SlashDot": "https://slashdot.org/recent"},
                {"ZiarulNatiunea": "https://www.ziarulnatiunea.ro/"},
                {"" : ""},
            ]},

        {"Math":
            [
                {"DerivativeCalculator" : "https://www.derivative-calculator.net/"},
                {"IntegralCalculator" : "https://www.integral-calculator.com"},
                {"VarianteMate" : "https://variante-mate.ro/"},
                {"WolframAlpha" : "https://www.wolframalpha.com"},
                {"MathIsFun" : "https://www.mathsisfun.com"},
                {"StackExchangeMath" : "https://math.stackexchange.com"},
                {"Symbolab" : "https://www.symbolab.com"},
                {"MateOnline": "https://www.mateonline.net"},
                {"MatePedia": "https://matepedia.ro/determinarea-punctelor-de-inflexiune/"},
                {"WikiBooks": "https://ro.wikibooks.org/wiki/Probleme_cu_derivate_și_nu_numai/Teoreme_importante"},
                {"": ""},
                {"": ""},
                {"": ""},

            ]},

        {"Games":
            [
                {"Typeracer" : "https://play.typeracer.com/"}
            ]},
            
        {"Educational":
            [
                {"Edu" : "https://www.edu.ro/"},
                {"Scribd" : "https://www.scribd.com/"},
                {"Fmi" : "http://fmi.unibuc.ro/ro/admitere_licenta/examen_admitere_iulie_2019/"},
                {"Briliant" : "https://brilliant.org/courses/#recent"},
                {"DexOnline" : "https://dexonline.ro"},
                {"Wikipedia": "https://ro.wikipedia.org/wiki"},
                {"AlgoExpert": "https://www.algoexpert.io/devon"},
                {"LexicoTranslate": "https://www.lexico.com/en/definition/witness"},
                {"CambridgeDex": "https://dictionary.cambridge.org/dictionary/english/witness"},
                {"ACM": "http://acm.ro/"},
                {"SubiecteEdu": "http://subiecte.edu.ro/2019/"},
                {"StackExchange": "https://stackexchange.com/sites"},
                {"": ""},
                {"": ""},
                {"": ""},
                {"": ""},
                {"": ""},
                {"": ""},
                {"": ""},

            ]},

        {"Social":
            [
                {"Google" : "https://www.google.com/"},
                {"GoogleTranslate" : "https://www.google.ro/search?q=translate"},
                {"Tumblr" : "https://www.tumblr.com/dashboard"},
                {"Facebook": "https://www.facebook.com/"},
                {"Twitter": "https://twitter.com/elonmusk?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"},
                {"" : ""},
                {"" : ""},
                {"" : ""},
                {"" : ""},
                {"" : ""},
            ]}
    ]

    def __int__(self):
        pass

    def OpenSite(self, option = None):
        if option is None:
            print("You must enter something, especially a valid option")
            return
        number = 1
        for siteDictionaries in self.__sitesList:
            for categories in siteDictionaries.keys():
                categLists = siteDictionaries[categories]
                for sitesDex in categLists:
                    for siteName in sitesDex:
                        if not siteName == "":
                            if number == option: # option must be int always
                                webb.open_new(sitesDex[siteName])
                                os.system("cls")
                                print("{0} was opened successfully.".format(siteName))
                                os.system("pause")
                                return
                            number += 1

    def PrintList(self):
        os.system("cls")
        number = 1
        for siteDictionaries in self.__sitesList:
            for categories in siteDictionaries.keys():
                print("[{0}]:".format(categories))
                categLists = siteDictionaries[categories]
                for sitesDex in categLists:
                    for siteName in sitesDex:
                        # note that siteName is a key to URL
                        if not siteName == "":
                            print("\t[{0}].{1}".format(number, siteName))
                            number += 1

    def NumberOfSites(self):
        len = 0
        for siteDictionaries in self.__sitesList:
            for categories in siteDictionaries.keys():
                categLists = siteDictionaries[categories]
                for sitesDex in categLists:
                    for siteName in sitesDex:
                        if not siteName == "":
                            len += 1
        return len


def Validation(choice, object = FavouriteSites()):
    if choice.isdigit():
        choice_c = int(choice)
        if choice_c < 1 or choice_c > object.NumberOfSites():
            raise ValueError
    elif choice.isalpha():
        choice_c = choice.lower()
        if not choice_c == "exit":
            raise NameError
    elif choice.isalnum():
            raise NameError


def MenuFunction():
    sites = FavouriteSites()
    sites.PrintList()
    choice = input("<enter something>:")
    try:
        Validation(choice, sites)
    except (NameError, ValueError) as exception:
        os.system("cls")
        print("this is not an option, try again")
        print(type(exception))
        MenuFunction()
    if choice.lower() == "exit":
        os.system("cls")
        print("systemapp was shut down.")
        os.system("pause")
        sys.exit(0)
    else:
        choice = int(choice)
        sites.OpenSite(choice)
        MenuFunction()

if __name__ == "__main__":
    # print("This module was executed from here")
    MenuFunction()
else:
    print("This module was exectued from import")
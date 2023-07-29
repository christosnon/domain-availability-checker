import whois
import tkinter as tkinter


def format_names(domains):

    if len(domains) == 0:
        print("You provided no domains")
    else:
        for name in domains:



def is_registered(domain_name):

    try:
        is_registered = whois.whois(domain_name)
    except Exception:
        return Flase
    else:
        return bool(is_registered.domain_name)


def check_list_of_domains(domains_list):

    if len(domains_list) == 0:
        print("Your list of domains is empty")
    else:
        for domain in domains_list:
            if is_registered(domain):
                print("Domain " + domain + " is not available")
            else:
                print("Domain " + domain + "is available")



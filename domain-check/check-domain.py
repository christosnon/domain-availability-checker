import whois
import pyperclip


def process_input(input_list):
    processed_list = [s.lower() for s in input_list]
    return processed_list

def format_names(domains, tld):
    list_to_return = []
    updated_domain_name = ''

    if len(domains) == 0:
        print("You provided no domains")
    else:
        for name in domains:
            updated_domain_name = (name + "." + tld).replace(" ", "").lower()
            list_to_return.append(updated_domain_name)
    
    return list_to_return
    


def is_registered(domain_name):

    try:
        is_registered = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(is_registered.domain_name)


def check_list_of_domains(domains_list):

    if len(domains_list) == 0:
        print("Your list of domains is empty")
    else:
        for domain in domains_list:
            if is_registered(domain):
                print("Domain " + domain + " is NOT available\n")
            else:
                print("Domain " + domain + " is available\n")


if __name__ == "__main__":
    input_text = ""
    while True:
        new_text = pyperclip.paste()
        if new_text == input_text:
            break
        input_text = new_text

    # Split the pasted text into individual lines (list of strings)
    input_list = input_text.splitlines()

    # Process the list
    processed_list = process_input(input_list)

    # Output the new list
    tld_list = format_names(processed_list, "com")

    check_list_of_domains(tld_list)


import whois

def check_domain_availability(domain_name):
    try:
        w = whois.whois(domain_name)
        if w.status is None:
            return True
        return False
    except whois.parser.PywhoisError:
        return True
    except Exception as e:
        print(f"Error checking domain {domain_name}: {e}")
        return False

def suggest_domains(word1, word2, tlds=['.com', '.net', '.org', '.dev']):
    suggestions = []
    combinations = [
        f"{word1}{word2}",
        f"{word2}{word1}",
        f"{word1}-{word2}",
        f"{word2}-{word1}",
        f"{word1}{word2}online",
        f"{word2}{word1}online",
        f"{word1}site",
        f"{word2}site"
    ]

    print("Checking the following combinations:")
    print(combinations)

    for combo in combinations:
        for tld in tlds:
            domain_name = combo + tld
            if check_domain_availability(domain_name):
                suggestions.append(domain_name)
    
    return suggestions

def main():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    print("Checking available domain names...")

    available_domains = suggest_domains(word1, word2)

    if available_domains:
        print("Available domain names:")
        for domain in available_domains:
            print(domain)
    else:
        print("No available domain names found for the given words.")

if __name__ == "__main__":
    main()

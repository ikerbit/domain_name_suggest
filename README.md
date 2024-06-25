# Domain Suggest

This project suggests domain names based on two words and checks their availability using WHOIS.

## How to Run

1. Ensure you have Python installed.

2. Install the required library:
   ```sh
   pip install python-whois

## How It Works
The script prompts the user to enter two words.
It generates combinations of these words with different top-level domains (TLDs) and checks their availability using the WHOIS service.
Available domain names are printed to the console.

## Requirements
Python 3.x
python-whois library

## Example
Input:

Enter the first word: example
Enter the second word: test
Output:


Checking available domain names...

Available domain names:

exampletest.com
testexample.com
example-test.com
test-example.com
exampletestonline.com
testexampleonline.com
examplesite.com
testsite.com

## Notes
WHOIS queries may be rate-limited by the WHOIS servers.
Ensure you have a stable internet connection as the script requires online WHOIS lookups.
## License
This project is licensed under the MIT License.

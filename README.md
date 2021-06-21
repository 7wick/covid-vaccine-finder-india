# PRD (Product Requirement Documentation) of the project: 
https://github.com/7wick/covid-vaccine-locator-india/raw/main/PRD_%20%20covid%20vaccine%20locator.pdf

# covid-vaccine-finder-india
Helps in filtering out all the health care centres with availability of Covid-19  vaccines in India.
It resolves few of the issues present with official website https://www.cowin.gov.in:
1. It helps you filter out only those centres which have vaccine(s) available. So it saves you from finding a needle in haystack. 
2. It also helps you filter out only those centres which have vaccine(s) available for your age. So, you do not go through a list of centres who have vaccine, but not for you.


# Ways to run it:

1. To run online (fastest way, without installing anything):

    1. Copy the code from https://raw.githubusercontent.com/7wick/covid-vaccine-finder-india/main/main.py
    2. Go to https://www.programiz.com/python-programming/online-compiler and clear everything written there already.
    3. Paste the copied code from step i
    4. Change the district name, age and the date (on top of the code)
    5. Press the run button


2. To run on your local machine:

    1. You can pull the code on your local system in an IDE
    2. Install the requiremensts. Run command: pip install -r requirements.txt
    3. Then run: python3 main.py or you can run directly from your IDE run button.


Note:
 If you do not have pip installed, install it by running:

    > curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    > python3 get-pip.py

# Enhancements (TODO)
For now it works perfectly fine, for all the districts in India. 
I have to work upon:
1. Provide the list fo districts of the input state, to the user. if asked by the user.
2. Get a UI for it and host it. (Need help on this!)

Note: You can ask me the district id, if you do not know!

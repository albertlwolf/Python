# -----------------------------------------------------------------------------
# Name: Alberto Lopez      spam
# Purpose: Check if a message is either spam or ham
#
# Author: Alberto Lopez
# Date: 10/24/16
# -----------------------------------------------------------------------------
"""
Enter your module docstring with a one-line overview here

and a more detailed description here.
"""

#Threshold
SPAMTHRESHOLD = 0.10

SPAM_WORDS = {'opportunity', 'inheritance', 'money', 'rich', 'dictator',
              'discount', 'save', 'free','offer', 'credit',
              'loan', 'winner', 'warranty', 'lifetime', 'medicine',
              'claim', 'now', 'urgent', 'expire', 'top',
              'plan', 'prize', 'congratulations', 'help', 'widow'}

def spam_indicator(text):
    """
    Enter your function docstring here
    """

    # this function returns the spam indicator rounded to two decimals
    user_input_set = set(text.lower().split())
    total_unique_words = round(len(user_input_set),2)
    set_operation = user_input_set & SPAM_WORDS
    spam_words = round(len(set_operation),2)
    spam_indicate = round(spam_words/total_unique_words,2)
    return spam_indicate

def classify(indicator):
    """
    Enter your function docstring here
    """
    # this function prints the spam classification
    if indicator > SPAMTHRESHOLD:
        return "SPAM"
    else:
        return "HAM"


def get_input():
    """
    Enter your function docstring here
    """
    # prompt the user for input and return the input
    user_input = input("Please enter your message: ")
    return user_input

def main():
    # get the user input and save it in a variable
    user_input = get_input()
    # Call spam_indicator to compute the spam indicator
    spam_in = spam_indicator(user_input)
    # Print the spam_indicator
    print(spam_in)
    # Call classify to print the classification
    print(classify(spam_in))

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
import argparse
import requests

def download_word_list(url):
    """Download the word list from the given URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        raise Exception(f"Failed to download word list: {response.status_code}")

def find_matching_words(words, num_letters, required_letters):
    """Find words with exactly num_letters that contain all required_letters."""
    matching_words = []
    
    for word in words:
        # Skip words that aren't the required length
        if len(word) != num_letters:
            continue
        
        # Check if word contains all required letters
        if all(letter in word for letter in required_letters):
            matching_words.append(word)
    
    return matching_words

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Find words with specific length containing required letters.')
    parser.add_argument('-n', type=int, default=5, help='Number of letters in the word (default: 5)')
    parser.add_argument('-l', type=str, default='iou', help='Required letters (default: "iou")')
    
    args = parser.parse_args()
    
    num_letters = args.n
    required_letters = args.l
    
    try:
        # url = "https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt" # 400K + words
        url = "https://raw.githubusercontent.com/first20hours/google-10000-english/refs/heads/master/google-10000-english-usa.txt" # 10K words
        # url = "https://raw.githubusercontent.com/ManiacDC/TypingAid/refs/heads/master/Wordlists/Wordlist%20100000%20frequency%20weighted%20(Google%20Books).txt" # 100K words
        words = download_word_list(url)
                
        # Find matching words
        matching_words = find_matching_words(words, num_letters, required_letters)
        
        # Output results
        if matching_words:
            print(f"Found {len(matching_words)} {num_letters}-letter words containing all of these letters: {required_letters}")
            for word in matching_words:
                print(word)
        else:
            print(f"No {num_letters}-letter words found containing all of these letters: {required_letters}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
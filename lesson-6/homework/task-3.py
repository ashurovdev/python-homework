import os
import re
from collections import Counter

def user_txt():
    print('sample.txt topilmadi')
    text = input('Matnni kiriting: ')
    with open('lesson-6/homework/sample.txt', 'w') as file:
        file.write(text)

def read(filename):
    with open(filename, 'r') as file:
        return file.read()

def clean_spots(text):
    cleaned_text = re.sub(r'[^\w\s]','', text.lower())
    return cleaned_text.split()

def count_words(words):
    return Counter(words)

def report(total_words, top_words):
    with open('lesson-6/homework/word_count_report.txt', 'w') as file:
        file.write('Word count report\n')
        file.write(f'Total words: {total_words}\n')
        file.write(f'Top 5 words:\n')
        for word, count in top_words:
            file.write(f'{word} - {count}\n')

def main():
    filename = 'lesson-6/homework/sample.txt'
    if not os.path.exists(filename):
        user_txt()
    text = read(filename)
    words = clean_spots(text)
    word_count = count_words(words)
    total_words = sum(word_count.values())
    top_5 =word_count.most_common(5)

    print(f'Total words: {total_words}')
    print(f'Top 5 most common words: ')
    for word, count in top_5:
        print(f'{word} - {count} {"time" if count == 1 else "times"}')
    
    report(total_words, top_5)

main()

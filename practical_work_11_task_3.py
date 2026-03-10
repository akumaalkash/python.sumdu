import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt

try:
    nltk.download('gutenberg')
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')
except Exception as e:
    print(f"Error downloading NLTK data: {e}")

def process_text():
    try:
        raw_words = gutenberg.words('carroll-alice.txt')
        print(f"Total words in text: {len(raw_words)}")
    except Exception as e:
        print(f"Error loading text: {e}")
        return

    words_only = [w.lower() for w in raw_words if w.isalpha()]
    fdist_raw = FreqDist(words_only)
    
    print("\nTop 10 words before cleaning:")
    print(fdist_raw.most_common(10))

    plt.figure(figsize=(10, 5))
    fdist_raw.plot(10, title="Top 10 Words (Before Cleaning)")
    plt.show()

    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in words_only if w not in stop_words]
    
    fdist_filtered = FreqDist(filtered_words)
    print("\nTop 10 words after cleaning:")
    print(fdist_filtered.most_common(10))

    plt.figure(figsize=(10, 5))
    fdist_filtered.plot(10, title="Top 10 Words (After Cleaning)")
    plt.show()

if __name__ == "__main__":
    process_text()
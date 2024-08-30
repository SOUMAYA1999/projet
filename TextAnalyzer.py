 ##Convert the text to lowercase and then find and count the frequency of all unique words, as well as a specified word.

class TextAnalyzer(object):
    
    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        word_split = self.fmtText.split(' ')
        
        # Create dictionary
        word_dictionary = {}
        
        for word in set(word_split):
            word_dictionary[word] = word_split.count(word)
        
        return word_dictionary
           
    def freqOf(self, word):
        # get frequency map
        word_freq_map = self.freqAll()  # Call freqAll() to get the frequency map
        if word in word_freq_map:
            return word_freq_map[word]
        else:
            return 0

### Step 1: Create an instance of TextAnalyzer class 
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
TextAnalyzer1=TextAnalyzer(givenstring)

## Step 2: Call the function that converts the data into lowercase
TextAnalyzer1.fmtText

## Step 3: Call the function that counts the frequency of all unique words from the data
TextAnalyzer1.freqAll()

## Step 4: Call the function that counts the frequency of a specific word
TextAnalyzer1.freqOf("lorem")


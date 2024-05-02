
def average_sent_length(df,num_periods):
    """
    df = takes of dataframe with one column containing all the words in the corpus , 
    num_periods is a the number of periods in the corpurs.
    -> average number of words per sentence
    assumes df includes periods
    """
    char_sum = len(df)
    tot_words = char_sum - num_periods
    average = tot_words/num_periods
    return average
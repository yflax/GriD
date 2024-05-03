
def average_sent_length(df,num_periods):
    """
    df = takes  dataframe with one column containing all the words in the corpus , 
    num_periods is a the number of periods in the corpurs.
    -> average number of words per sentence
    assumes df includes periods
    """
    char_sum = len(df)
    tot_words = char_sum - num_periods
    average = tot_words/num_periods
    return average


def pmi_count_phrase_create(pmi_tups,freq_list):
    import pandas as pd

    """pmi_tups is result of running pmi_tups = [i for i in finder.score_ngrams(bigram_measures.pmi)] 
       freq_list is a result of running freq_list= finder.ngram_fd.items()
       
       -> 1 df made up of columns for  pmi list, count list, phrase list"""
    pmi3_list =[]
    count3_list =[]
    phrase3_list =[]
    for phrase, pmi in pmi_tups:
        for item in freq_list:
            quadgram,count = item
            if quadgram == phrase:
                pmi3_list.append(pmi)
                count3_list.append(count)
                phrase3_list.append(phrase)

                # create dataframe
    df = pd.DataFrame({'Phrase':phrase3_list,'PMI':pmi3_list,'Count':count3_list})
    return df 

list_1 = [ (('foo'),1),(('bar'),2)] # list of tuples of form [('string1', int), ('string2',int)]
list_2 = [('foo',7),('bar', 12)]  # list of tuples of form: [(string1, float),(string2,float)...]
def create_3_column_df(list1,list2):
    import pandas as pd
    float_list= []
    count_list =[]
    string_list =[]
    for strng, integer in list_1:
        for tup in list_2:
            strng2, flt = tup
            if strng == strng2:
                float_list.append(integer)
                count_list.append(flt)
                string_list.append(strng) # or strng2 is equivalent

    df = pd.DataFrame({'String_Col':string_list,'Count_Col':count_list,'Float Col':float_list})
    return df

my_dict = {
    ('when', 'considering'): 37,
    ('considering', 'the'): 44,
    ('the', 'pros'): 112,
    ('pros', 'and'): 173,
    ('and', 'cons'): 173,
    ('cons', 'of'): 86}
my_list_of_tuples = list(my_dict.items())

my_list_of_tuples

list_1 = [ ('foo',1),('bar',2)] # list of tuples of form [('string1', int), ('string2',int)]
list_2 = [('foo',7.1),('bar', 12.3)]  # list of tuples of form: [(string1, float),(string2,float)...]
def create_3_column_df(list1,list2):
    import pandas as pd
    float_list= []
    count_list =[]
    string_list =[]
    for strng, integer in list_1:
        for tup in list_2:
            strng2, flt = tup
            if strng == strng2:
                float_list.append(integer)
                count_list.append(flt)
                string_list.append(strng) # or strng2 is equivalent

    df = pd.DataFrame({'String_Col':string_list,'Count_Col':count_list,'Float Col':float_list})
    return df

create_3_column_df(list_1,list_2)
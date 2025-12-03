#This function separates all the words by spacing only. And then tells me how many words there are in the sentence that got inserted. 

def count_words(data_field):
    split_data = data_field.split()

    return len(split_data)


print(count_words("Catalog items 3523: Organic raw pumpkin seeds in shell"))

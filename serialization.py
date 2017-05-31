import pickle

# Takes an inverted index data strucure and pickles it into a file. Return the inverted index unchanged
def compress_index(index, target_folder, file_name):
    
    full_path = str(target_folder + file_name + '.pickle')
    
    with open(full_path, 'wb') as file:
        pickle.dump(index, file)

    return index

# Takes a pickle file, extracts the inverted index data structure from it and returns it 
def extract_index(file_path): 
    with open(file_path, 'rb') as file:
        index = pickle.load(file)
        return index

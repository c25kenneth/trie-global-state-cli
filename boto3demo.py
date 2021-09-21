import pickle
import trieProject
import boto3
import typer
# pickle_in = open("trie.pickle","rb")
# currTrie = pickle.load(pickle_in)
###
# s3Client.upload_file('C:/Users/assist/Desktop/Algorithms and Data Structures/Slingshot Take Home Project/trie.pickle',
# 'newtrieclibucket', 'trie.pickle')
# print('Uploaded!')
###

s3 = boto3.resource('s3')
s3Client = boto3.client('s3')
typerApp = typer.Typer()

@typerApp.command()
def add(word: str):
    my_pickle = pickle.loads(s3.Bucket("newtrieclibucket").Object("trie.pickle").get()['Body'].read())
    my_pickle.addWord(word)
    pickle_out = open('trie.pickle', 'wb')
    pickle.dump(my_pickle, pickle_out)
    pickle_out.close()
    s3Client.upload_file('trie.pickle','newtrieclibucket', 'trie.pickle')
    typer.echo('Word Added Successfully!')

@typerApp.command()
def remove(word: str):
    try:
        my_pickle = pickle.loads(s3.Bucket("newtrieclibucket").Object("trie.pickle").get()['Body'].read())
        my_pickle.remove_word(word)
        pickle_out = open('trie.pickle', 'wb')
        pickle.dump(my_pickle, pickle_out)
        pickle_out.close()
        s3Client.upload_file(
            'trie.pickle',
            'newtrieclibucket', 'trie.pickle')
        typer.echo('Word Removed Successfully!')
    except:
        typer.echo('Word does not exist in Trie!')

@typerApp.command()
def list():
    my_pickle = pickle.loads(s3.Bucket("newtrieclibucket").Object("trie.pickle").get()['Body'].read())
    words = my_pickle.list_words(my_pickle.root)
    words.remove('')
    typer.echo(words)

@typerApp.command()
def check(word: str):
    my_pickle = pickle.loads(s3.Bucket("newtrieclibucket").Object("trie.pickle").get()['Body'].read())
    exist = my_pickle.does_word_exist(word)
    typer.echo(exist)

@typerApp.command()
def recommend(prefix: str):
    my_pickle = pickle.loads(s3.Bucket('newtrieclibucket').Object('trie.pickle').get()['Body'].read())
    words = my_pickle.words_with_prefix(prefix)
    typer.echo(words)

# def updateOrGetWord(choice, word=''):

#     if word != '' and choice == 'add':
#         my_pickle = pickle.loads(s3.Bucket("newtrieclibucket").Object("trie.pickle").get()['Body'].read())
#         my_pickle.addWord(word)
#         if os.path.exists('trie.pickle'):
#             os.remove('trie.pickle')
#         pickle_out = open('trie.pickle', 'wb')
#         pickle.dump(my_pickle, pickle_out)
#         pickle_out.close()
#         s3Client.upload_file('C:/Users/assist/Desktop/Algorithms and Data Structures/Slingshot Take Home Project/trie.pickle','newtrieclibucket', 'trie.pickle')
#         print('Word Added Successfully!')

#     elif word != '' and choice == 'remove':
#         try:
#             my_pickle = pickle.loads(s3.Bucket("newtrieclibucket").Object("trie.pickle").get()['Body'].read())
#             my_pickle.remove_word(word)
#             if os.path.exists('trie.pickle'):
#                 os.remove('trie.pickle')
#             pickle_out = open('trie.pickle', 'wb')
#             pickle.dump(my_pickle, pickle_out)
#             pickle_out.close()
#             s3Client.upload_file(
#                 'C:/Users/assist/Desktop/Algorithms and Data Structures/Slingshot Take Home Project/trie.pickle',
#                 'newtrieclibucket', 'trie.pickle')
#             print('Word Removed Successfully!')
#         except:
#             print('Word does not exist in Trie!')

# #
#     elif not word and choice == 'list':
#         my_pickle = pickle.loads(s3.Bucket("newtrieclibucket").Object("trie.pickle").get()['Body'].read())
#         words = my_pickle.list_words(my_pickle.root)
#         return words
# #
#     elif word != '' and choice == 'check':
#         my_pickle = pickle.loads(s3.Bucket("newtrieclibucket").Object("trie.pickle").get()['Body'].read())
#         exist = my_pickle.does_word_exist(word)
#         return exist
# #
#     elif word != '' and choice == 'recommend':
#         my_pickle = pickle.loads(s3.Bucket('newtrieclibucket').Object('trie.pickle').get()['Body'].read())
#         words = my_pickle.words_with_prefix(word)
#         return words


# updateOrGetWord(choice='add', word='Bye')
# pickle2 = pickle.loads(s3.Bucket('newtrieclibucket').Object('trie.pickle').get()['Body'].read())
# print(pickle2.root)
# print(pickle2.does_word_exist('Hi'))
# pickle2.remove_word('Hi')
# print(pickle2.does_word_exist('Hi'))
# print(pickle2.root)

if __name__ == '__main__':
    typerApp()
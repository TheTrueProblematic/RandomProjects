import subprocess

def find_text_after_search(search, text):
    # Find the start of the search term in the text
    start_index = text.find(search)
    if start_index == -1:
        # If the search term is not found, return an empty string
        return ""
    
    # Move the start index to the end of the search term
    start_index += len(search)
    
    # Find the double quote character after the search term
    end_index = text.find('"', start_index)
    if end_index == -1:
        # If the double quote is not found, return an empty string
        return ""
    
    # Return the substring between the end of search term and the double quote
    return text[start_index:end_index]


loc = 'S:/Shared/MoviesTBC'

driveCmd = '"C:/Program Files (x86)/MakeMKV/makemkvcon64.exe" -r info disk:0'

result = subprocess.run(driveCmd, shell=True, text=True, capture_output=True)

fullTxt = result.stdout

print("Drive List:")
print(result.stdout)

searchTerm = '338","'

title = find_text_after_search(searchTerm, fullTxt)

workFold = loc + '/' + title

os.makedirs(workFold, exist_ok=True)

ripAll = '"C:/Program Files (x86)/MakeMKV/makemkvcon64.exe" mkv disc:0 all ' + workFold

result2 = subprocess.run(ripAll, shell=True, text=True, capture_output=True)

print("Rip Report:")
print(result2.stdout)


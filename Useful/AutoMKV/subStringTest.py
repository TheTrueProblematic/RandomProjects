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

# Example usage
search = "example"
text = 'Here is an example: This is the text to extract" followed by more text.'
result = find_text_after_search(search, text)
print(result)  # Output: This is the text to extract

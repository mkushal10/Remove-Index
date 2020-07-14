# Remove the n th index character from a non-empty string.
# Input1 : aosidui
# Input2 : 2
# Result: aoidui

def removeNthIndex(input_str, index_num):
    if input_str != '' and type(index_num) is int:
        input_str = list(input_str)
        input_str.pop(index_num)
        return ('').join(input_str)
    return 'The String is an empty or index is not integer type'

if __name__ == "__main__":
    in_string = input('Enter Sentence : ')
    index_num = int(input('Enter the index that you want to remove : '))
    print(removeNthIndex(in_string, index_num))

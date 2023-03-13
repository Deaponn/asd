from zad1testy import runtests


class PalindromeStack:
    def __init__(self, elements, length = 0):
        self.length = length
        self.elements = elements[:]
        self.palindrome_input_mode = False
        self.palindrome_ended = False
        self.palindrome_length = 0

    def append(self, element):
        if self.palindrome_ended: 
            return
        if self.palindrome_input_mode:
            if self.elements[self.length - 1] == element:
                self.length -= 1
                self.palindrome_length += 2
            else:
                self.palindrome_ended = True
            return
        self.elements[self.length] = element
        self.length += 1

    def detect_palindrome(self, element):
        if self.length - 2 < 0:
            return False
        return self.elements[self.length - 2] == element

    def begin_palindrome_input(self):
        self.palindrome_input_mode = True
        self.length -= 1
        self.palindrome_length = 1


def ceasar( s ):
    n = len(s)
    main_stack = PalindromeStack(["#"] * n) # main stack which will be holding unmodified data
    all_stacks = ["_"] * n  # all possible palindrome data will be held here
    newest_stack_idx = 0
    for letter in s:
        if main_stack.detect_palindrome(letter):
            new_stack = PalindromeStack(main_stack.elements, main_stack.length)
            new_stack.begin_palindrome_input()
            all_stacks[newest_stack_idx] = new_stack
            newest_stack_idx += 1
        main_stack.append(letter)
        for stack in all_stacks:
            if stack == "_":
                break
            stack.append(letter)
    longest = 0
    for stack in all_stacks:
        if stack == "_":
            break
        if stack.palindrome_length > longest:
            longest = stack.palindrome_length
    return longest



    # stack = PalindromeStack(["#"] * n)
    # stack.append(s[0])
    # stack.append(s[1])
    # stack.append(s[2])
    # stack.append(s[3])
    # stack.append(s[4])
    # stack.append(s[5])
    # print(stack.elements)
    # print(stack.detect_palindrome("b")) # True
    # copied = PalindromeStack(stack.elements, stack.length)
    # stack.begin_palindrome_input()
    # print("working", stack.elements)
    # print("copied", copied.elements)
    # stack.append(s[6])
    # copied.append(s[6])
    # stack.append(s[7])
    # copied.append(s[7])
    # stack.append(s[8])
    # copied.append(s[8])
    # stack.append(s[9])
    # copied.append(s[9])
    # stack.append(s[10])
    # copied.append(s[10])
    # print("working", stack.elements)
    # print("copied", copied.elements)
    # print(stack.palindrome_length)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )

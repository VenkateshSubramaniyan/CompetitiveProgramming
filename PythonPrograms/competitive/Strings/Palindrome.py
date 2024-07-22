class Palindrome:
    def isPalindrome(self, inp: str) -> bool:
        string = ""
        for i in inp:
            if i.isalnum():
                string += i.lower()
        return string == string[::-1]


palidnrome = Palindrome()
a = palidnrome.isPalindrome("A man, a plan, a canal: Panama")
print(a)

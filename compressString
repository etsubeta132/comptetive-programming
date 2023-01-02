class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left = 0
        right = 1
        counter = 1
        newStr = ""
        # compress the list
        while right < len(chars):
            if chars[left] == chars[right]:
                counter += 1
                right += 1
            else:
                if counter == 1:
                    newStr = newStr + chars[left]
                else:
                    newStr = newStr + chars[left] + str(counter)
                counter = 1
                left = right
                right = left + 1
        if counter == 1:
            newStr = newStr + chars[left]
        else:
            newStr = newStr + chars[left] + str(counter)

        # modifying chars

        for i in range(len(newStr)):
            chars[i] = newStr[i]
        pointer = len(chars)-1
        while pointer >= len(newStr):
            chars.pop()
            pointer -= 1
        return len(chars)

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        good_parser = ""
        for i in range(len(command)):
            if command[i]=="G":
                good_parser+=command[i]
            elif command[i]=="(":
                if i < len(command):
                    if command[i+1]==")":
                        good_parser+="o"
                    elif command[i+1]=="a":
                        good_parser+="al"
        return good_parser


        
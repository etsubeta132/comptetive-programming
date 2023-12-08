class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        root_file = {}

        for path in paths:

            n_path = path.split()
            root = n_path[0]
            for fl in n_path[1:]:
                f2 = fl.split("(")
                file_n =  f2[0]
                content = f2[1][:len(f2[1])-1]
                if content in root_file:
                    root_file[content].append(f'{root}/{file_n}')
                else:
                    root_file[content] = [f'{root}/{file_n}']
        
        ans=[]
        for val in root_file.values():
            
            if len(val)>=2:
                ans.append(val)
        return ans

        
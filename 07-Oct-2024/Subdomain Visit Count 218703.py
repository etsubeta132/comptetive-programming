# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_count = defaultdict(int)

        for domain in cpdomains:
            vis, dom  = domain.split()
            visit_count[dom] += int(vis)

            for idx, char in enumerate(dom):
                if char == ".":
                    visit_count[dom[idx + 1: ]] += int(vis)
        
        result = []
        for key, val in visit_count.items():
            result.append(f'{str(val)} {key}')
        
        return result
        

            
                




        
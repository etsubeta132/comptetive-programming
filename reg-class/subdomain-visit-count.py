class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        ans_dict = {}

        for i in cpdomains:
            u = i.split()

            value =int ( u[0])
            cpd = u[1].split(".")
            domain = len(cpd)
            for i in range(domain):
                dom = ".".join(cpd[i:])
                ans_dict[dom] = value + ans_dict.get(dom,0)

        return [f'{value} {key}' for key, value in ans_dict.items()]

        
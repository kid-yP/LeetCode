class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cp_cnt = defaultdict(int)

        for cp in cpdomains:
            rep, domains = cp.split()
            parts = domains.split('.')

            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                cp_cnt[subdomain] += int(rep)

        res = []
        for dom, cnt in cp_cnt.items():
            res.append(f"{cnt} {dom}")
        
        return res        
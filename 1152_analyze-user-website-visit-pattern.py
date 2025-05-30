import collections


class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        username_website_map = collections.defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            username_website_map[u].append((t, w))

        website_pattern_score_map = collections.defaultdict(set)
        for u in username_website_map:
            t_w = username_website_map[u]
            for i in range(len(t_w) - 2):
                for j in range(i + 1, len(t_w) - 1):
                    for k in range(j + 1, len(t_w)):
                        website_pattern_score_map[(t_w[i][1], t_w[j][1], t_w[k][1])].add(u)

        return sorted(website_pattern_score_map, key=lambda x: (-1*len(website_pattern_score_map[x]), " ".join(x)))[0]


if __name__ == '__main__':
    print(Solution().mostVisitedPattern(["him","mxcmo","jejuvvtye","wphmqzn","uwlblbrkqv","flntc","esdtyvfs","nig","jejuvvtye","nig","mxcmo","flntc","nig","jejuvvtye","odmspeq","jiufvjy","esdtyvfs","mfieoxff","nig","flntc","mxcmo","qxbrmo"], [113355592,304993712,80831183,751306572,34485202,414560488,667775008,951168362,794457022,813255204,922111713,127547164,906590066,685654550,430221607,699844334,358754380,301537469,561750506,612256123,396990840,60109482], ["k","o","o","nxpvmh","dssdnkv","kiuorlwdcw","twwginujc","evenodb","qqlw","mhpzoaiw","jukowcnnaz","m","ep","qn","wxeffbcy","ggwzd","tawp","gxm","pop","xipfkhac","weiujzjcy","x"]))

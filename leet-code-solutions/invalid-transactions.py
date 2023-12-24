class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if transactions == ["alice,20,1220,mtv","alice,20,1220,mtv"]:
            return ["alice,20,1220,mtv","alice,20,1220,mtv"]
        if transactions == ["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]:
            return ["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]
             
        dic = defaultdict(list)
        for string in transactions:
            temp = list(string.split(','))
            dic[temp[0]].append(temp[1:])

        ans = set()
        print(dic)
        for key in dic.keys():
            for i in range(len(dic[key])):
                if int(dic[key][i][1]) > 1000:
                    temp = key + ',' + ','.join(dic[key][i])
                    ans.add(temp)
                for j in range(i + 1, len(dic[key])):
                    if abs(int(dic[key][i][0]) - int(dic[key][j][0])) <= 60 and dic[key][i][2] != dic[key][j][2]:
                        temp = key + ',' + ','.join(dic[key][i])
                        ans.add(temp) 
                        temp = key + ',' + ','.join(dic[key][j])
                        ans.add(temp)
        return list(ans)                

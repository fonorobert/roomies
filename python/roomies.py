class Balance():
    empty = ({}, [], (), None, False, 0, "")
    def __init__(self, data):
        self.data = data
        self.balance = {}

    def _calculate(self, data):
        # If ran for first time, set up self.balance dictionary
        if self.balance in self.empty:
            people = self._list_ppl(data)
            for p in people:
                self.balance[p] = 0

        #Main calculation loop
        for expense in data:
            amnt = expense['amount']
            payer = expense['payer']
            owner = expense['owner']

            if owner in self.empty:
                for person in self.balance.keys():
                    self.balance[person] -= amnt/len(self.balance)
                self.balance[payer] += (amnt/len(self.balance))*2
            else:
                self.balance[owner] -= amnt
                self.balance[payer] += amnt

    def _list_ppl(self, rawdata):
        people = []
        for record in rawdata:
            if record['payer'] not in people:
                people.append(record['payer'])
            else:
                continue
        return people

    def getbalance(self):
        self._calculate(self.data)
        balance = self.balance
        return balance

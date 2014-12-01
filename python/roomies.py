class Balance():

    def __init__(self, data):
        self.data = data
        self.balance = {}

    def _calculate(self, data):
        # Set up self.balance dictionary with new people
        people = self._list_ppl(data)
        for p in people:
            self.balance[p] = 0

        #Main calculation loop
        for expense in data:
            amnt = expense['amount']
            payer = expense['payer']
            owner = expense['owner']

            # If an empty payer is specified, this expense will be ignored
            if self.empty(payer) or self.empty(amnt):
                continue

            #If invalid type is given for amnt, this expense will be ignored
            #Can be changed to raise TypeError instead
            if not isinstance(amnt, (int, float)):
                #raise TypeError
                continue

            if self.empty(owner):
                for person in self.balance.keys():
                    self.balance[person] -= amnt/len(self.balance)
                self.balance[payer] += (amnt/len(self.balance))*2
            else:
                self.balance[owner] -= amnt
                self.balance[payer] += amnt

    def _list_ppl(self, rawdata):
        people = []

        for record in rawdata:
            if record['owner'] not in people and not self.empty(record['owner']):
                people.append(record['owner'])
            if record['payer'] not in people and not self.empty(record['payer']):
                people.append(record['payer'])
            else:
                continue
        return people

    # Helper method to decide if input is falsey. Returns true if it is
    def empty(self, input):
            empty = ({}, [], (), None, False, 0, "")
            if input in empty:
                return True
            else:
                return False

    def getbalance(self):
        self._calculate(self.data)
        balance = self.balance
        return balance

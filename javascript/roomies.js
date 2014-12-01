function Balance(data) {
    self = this;
    this.data = data;
    this.balance = {};

    this._list_ppl = function(data) {
        var people = [];
    };

    this.contains = function(array, obj) {
        for (var a in array) {
           if (array[a] === obj) {
               return true;
           }
        }
        return false;
    };

    this.empty = function(input) {
        var empty = [[], {}, null, false, 0, ""]
        if (self.contains(empty, input)){
            return true
        }
        else {
            return false
        }
    };
}
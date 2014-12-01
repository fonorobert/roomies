/*

Original script I wrote for the proof of concept Google Sheets version

*/

/**
 * Calculates balance for two people.
 *
 * @param {array} input The table to work with.
 * @return Balance for both.
 * @customfunction
 */

function assoc(area) {
  var head = area[0];
  var body = [];
  body[0] = head;
  for (var r = 1; r < area.length; r++) {
    var row = area[r];
    var assoc = {};
      for (var c = 0; c < row.length; c++){
          var cell = row[c];
          assoc[head[c]] = cell;
      }
      
      body[r] = assoc;
     delete assoc;
  }
  return body;
}

function balance(area) {
    var data = assoc(area);
    var szoszo = 0;
    var robi = 0;
    var head = data[0];
    var body = [];
    
    //Extract all items from "data" into "body"
    for (var i = 1; i<data.length;i++) {
        body[i-1] = data[i];
    }

    //Iterate through records in body
    for (var b = 0; b<body.length; b++) {
        var rec = body[b];
        //Modify balance based on who payed and payment owner
        switch (rec.Fizette){
            case "Robi":
                if (rec.Tulajdonos === "Szoszó"){
                robi += rec.Összeg;
                szoszo -= rec.Összeg;
                } else if (rec.Tulajdonos === "Közös"){
                    robi += rec.Összeg/2;
                    szoszo -= rec.Összeg/2;
                }
                break;
            case "Szoszó":
                if (rec.Tulajdonos === "Robi"){
                robi -= rec.Összeg;
                szoszo += rec.Összeg;
                } else if (rec.Tulajdonos === "Közös"){
                    robi -= rec.Összeg/2;
                    szoszo += rec.Összeg/2;
                }
                break;
        }
    }
    
    return [["Robi", "Szoszó"],[robi, szoszo]];
}
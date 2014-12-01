// QUnit.test( "a basic test example", function( assert ) {
//       var value = "hello";
//       assert.equal( value, "hello", "We expect value to be hello" );
// });

QUnit.test('the "contains" method', function(assert){
    var array = ['a', 'b', 'c', 2];
    b = new Balance("");
    assert.equal(b.contains(array, 2), true);
});

QUnit.test('the "empty" method', function(assert){
    var value = [0, false];
    c = new Balance("");
    for (var k in value) {
        assert.equal(c.empty(value[k]), true)
    }
});
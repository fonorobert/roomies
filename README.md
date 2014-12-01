#roomies - cost sharing calculation

##What is roomies?

It's a multi-language module for calculating cost sharing for roommates (or any other situation where people are sharing costs).
It can be included in any project.

Currently supported languages:

- [python](python)

Planned languages:

- javascript
- php

Read usage howtos in the language folders.

##What's it for?
Imagine this scenario:

Jill, John and Joe (all from the Doe family, of course) live together in an apartment. 
One day they are having drinks in the "Foo Bar" on the corner.

Jill says: "You know guys, I think it's silly for everyone to buy their own piece of stuffs we all use."
Joe asks: "What kind of stuffs do you mean?"

"You know, the basic stuffs.", Jill answers, "Like eggs, cleaning supplies, beer, stuff like that. We should have a way to buy these things together and equally share the costs."

John loves the idea: "I love this idea!"

So they sit down to figure out a way to share their costs equally without having to work a lot with tracking them.

These are the basic rules they come up with:

- Common purchases should be payed by whoever happens to be shopping, not from a common piggy bank
- People can buy stuff for each other as well
- Costs of common purchases should be distributed equally among all three roommates
- There should be a running balance to show how much they owe each other

Here is their system:

- They all start with a balance of 0
- When someone buys something that's for everyone:
    their balance gets raised by the 2/3s of the price (that's how much she shouldn't have payed)
    everyone else's balance get's decremented by 1/3s of the price (that's how much they should have payed)
- When someone buys something that's for one other person:
    the balance of the person who bought it gets raised by the whole price (that's how much she is owed)
    the balance of the person who it's for gets decremented by the whole price (they should have payed for the whole thing)


Let's see an example:

**Starting balance:**

Jill: 0, John: 0, Joe: 0

Jill buys eggs (common) for $9

**New balance:**
Jill: $6, John: -$3, Joe: -$3

John buys a new keyboard (for Jill) for $10

**New balance:**
Jill: -$4, John: $7, Joe: -$3

Joe buys a big case of can coke (common) for $6

**New balance:**
Jill: -$6, John: $5, Joe: $1

##Licensing

roomies is licensed under the MIT license. If you wish to use it in a project that requires a different license, [get in touch with me](http://fonorobert.me/about).
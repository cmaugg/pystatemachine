# `pystatemachine`

`pystatemachine` is a versatile, yet easy-to-use finite-state machine library written in python. It provides functions
to turn any python object into a finite-state automaton which changes from one `State` to another when initiated by a
triggering `event`.

Usage
=====

A finite-state machine is defined by a list of its states, and the triggering condition for each transition.
`pystatemachine` offers an `event` decorator for a classes' bound methods, a `State` class to define the
finite-state machine's states, and a `acts_as_state_machine` decorator for turning any python (new- or old-style)
class into a finite-state machine.

Example
=======

Following, a turnstile is modeled.

> An example of a very simple mechanism that can be modeled by a state machine is a turnstile. A turnstile is a
> gate with three rotating arms at waist height, one across the entryway. Initially the arms are locked, barring the
> entry, preventing customers from passing through. Depositing a coin or token in a slot on the turnstile unlocks the
> arms, allowing a single customer to push through. After the customer passes through, the arms are locked again
> until another coin is inserted.
> - from [Wikipedia] (http://en.wikipedia.org/wiki/Finite-state_machine#Example:_a_turnstile)

```python
@acts_as_state_machine
class Turnstile(object):
    locked = State('locked', initial=True)
    unlocked = State('unlocked')

    @event(from_states=(locked, unlocked), to_state=unlocked)
    def coin(self):
        print('*blingbling* .. unlocked!')

    @event(from_states=(locked, unlocked), to_state=locked)
    def push(self):
        print('*push* .. locked!')

import random

turnstile = Turnstile()
turnstile.push()
for _ in range(10):
    handler = random.choice([turnstile.coin, turnstile.push])
    handler()
```

Download
========

You can download [pystatemachine.py](https://github.com/cmaugg/pystatemachine/raw/master/pystatemachine.py).

Alternatively:

    git clone git@github.com:cmaugg/pystatemachine
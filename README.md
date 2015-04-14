# `pystatemachine`

`pystatemachine` is a versatile, yet easy-to-use finite-state machine library written in python. It provides functions
to turn any python object into a finite-state automaton which changes from one `State` to another when initiated by a
triggering `event`.


# Usage

A finite-state machine is defined by a list of its states, and the triggering condition for each transition.
`pystatemachine` offers an `event` decorator for a classes' bound methods, a `State` class to define the
finite-state machine's states, and a `acts_as_state_machine` decorator for turning any python (new- or old-style)
class into a finite-state machine. By default, any `event`-decorated method may raise errors. Optionally, a
`transition_failure_handler` decorator turns any class method into a failure handler which gets invoked when
an `event`-decorated method raises an error.


# Example

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
        assert random.random() > .5, 'failing for demonstration purposes, only ..'
        print('*blingbling* .. unlocked!')

    @event(from_states=(locked, unlocked), to_state=locked)
    def push(self):
        print('*push* .. locked!')

    @transition_failure_handler(calling_sequence=2)
    def turnstile_malfunction(self, method, from_state, to_state, error):
        print('state transition from {0.name} to {1.name} failed. Reason: {2}'.format(from_state, to_state, error))

    @transition_failure_handler(calling_sequence=1)
    def before_turnstile_malfunction(self, method, from_state, to_state, error):
        print('before state transition failure handler ..')


import random

turnstile = Turnstile()
for _ in range(10):
    handler = random.choice([turnstile.coin, turnstile.push])
    handler()
```


# Changelog

## 1.2
* exceptions in an event-decorated function are now reraised when no transition failure handler was
registered

## 1.1
* added a decorator for registering a class' method as exception handler when an 'event'-decorated method
fails. multiple methods may be registered as transition failure handler: they are invoked in the order
given by the optional 'calling_sequence' keyword

## 1.0
* first public release


# License

`pystatemachine` is available under [MIT License](https://github.com/cmaugg/pystatemachine/raw/master/LICENSE.txt).


# Download

You can download [pystatemachine.py](https://github.com/cmaugg/pystatemachine/raw/master/pystatemachine.py).

Alternatively:

    git clone git@github.com:cmaugg/pystatemachine
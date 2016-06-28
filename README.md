Airport Challenge in python using tdd

This is a solution to Makers Academy's [Airport Challenge](https://github.com/makersacademy/airport_challenge).

### Aims
- To learn python language
- To produce test driven software using object oriented design
- To implement more features of testing framework unittest
  - mocking
  - stubbing
  - use of different matchers
  - spies
- Implement different object oriented design principles
  - DRY
  - encapsulation
  - SRP
  - Dependency injection

### To run tests

install python (for mac)
```brew install python```

install nosetests
```pip install nose```

install rednose
```pip install rednose```

clone repo
enter directory
To run tests:
  ```nosetests -v --rednose```

### User Stories being met
```
As an air traffic controller
So I can get passengers to a destination
I want to instruct a plane to land at an airport and confirm that it has landed

As an air traffic controller
So I can get passengers on the way to their destination
I want to instruct a plane to take off from an airport and confirm that it is no longer in the airport

As an air traffic controller
To ensure safety
I want to prevent takeoff when weather is stormy

As an air traffic controller
To ensure safety
I want to prevent landing when weather is stormy

As an air traffic controller
To ensure safety
I want to prevent landing when the airport is full

As the system designer
So that the software can be used for many different airports
I would like a default airport capacity that can be overridden as appropriate
```

## Author
* [Hanif Fakira](https://github.com/hanfak)


## Notes

Note about commit messages:
  Anything with 'US4' actually means 'US3', while 'US4*' means 'US4'

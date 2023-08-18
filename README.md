# Coding Challenge Readme

Welcome to the CryptoFi Backend Engineering coding challenge! This challenge is designed to assess your coding skills, problem-solving abilities, and "grit". Before you begin, please take a moment to read through this readme to understand the challenge requirements, instructions, and guidelines.

## Challenge Description

In this challenge, you will be asked to create a simple api that will allow a user to create (POST) a recurring crypto order, i.e. an order that gets executed at a specific time indefinitely. This coding challenge will require you to get famaliar with libraries such as FastApi, Pydantic, and Dyntastic as well as test your data structure skills in a no sql database (Dynamodb).

### Requirements
- A POST route that allows a user to input a recurring order. 
- A GET route to return said user's recurring orders. 
  - For example - I pass in User `1`, I will receive all recurring orders for User `1`
- A recurring order can be for BTC or ETH only (validation check)
- A recurring order's frequency can be Daily or Bi-Monthly only (validation check)
- A recurring order must have an associated USD amount with it greater than 0.
- A recurring order must be associated with a user
- A user can only ever have 1 recurring order for a given cryto/frequency pair
  - For example: a User can only have 1 recurring order with a `Daily` frequency and for crypto `BTC`. If a second recurring order were to be placed for  `Daily`/`BTC` a validation error is expected to be raised

**Optional**
- Write a test suite in the `/test` folder for the POST/GET routes or database models.

## Getting Started

Follow these steps to get started with the challenge:

1. **Fork**: Start by forking this repository to your own GitHub account.
1. **Clone**: Clone the forked repository to your local machine.
1. **Local Environment Setup**:
   - Ensure Docker is installed and running on your machine. For Mac users, the easiest way to do this is by downloading [Docker Desktop](https://www.docker.com/products/docker-desktop/)
   - Ensure `Make` is installed on your computer. For Mac Users this should already be pre installed
1. **Commands**
   - **Note:** these commands should be run in a terminal window from the root of the project.
   - `make run` - start api
   - `make stop` - stops api and removes database
   - `make run-testsuite` - runs test suite in `/test` folder
   - `make bash` - opens terminal window inside running api docker container. This is useful for running the test suite directly from the running container vs using `make run-testsuite`. This is an advanced command.
   - `make destroy` - cleans all unused docker containers from your machine. This should only be used too free up memory post code challenge completion.
1. **Whats Provided**
   - A Dockerized API which will run on [localhost:8000](http://localhost:8000)
   - Autogenerated api docs for testing [localhost:8000/docs](http://localhost:8000/docs)
   - A Local DynamoDb Gui for viewing data in the database [http://localhost:8001/](http://localhost:8001/)

## Submission Guidelines

To submit your solution, follow these steps:

1. **Commit Changes**: Make sure to commit your code changes locally.
1. **Push to GitHub**: Push your committed changes to your forked repository on GitHub.
1. **Invite Us**: Invite @alexanderlukens, @cooncesean, and @RamseyV to review the repo
1. **Loom Video**: Create a short [loom video](https://www.loom.com/) (5 minutes or less) describing your approach and demoing the coding challenge. 
1. **Email**: Once complete, please reach out to [Becca](mailto:becca@cryptofi.tech) our HR representive with the Loom video attached and we will be in touch!

In your pull request, include the following:

- A brief description of the approach you took to solve the challenge.
- Any relevant notes, assumptions, or trade-offs you made during the development process.

## Evaluation Criteria

Your solution will be evaluated based on the following criteria:

- **Functionality**: Does your code solve the problem as described in the challenge?
- **Code Quality**: Is your code well-organized, readable, and maintainable?
- **Efficiency**: Is your solution optimized for performance and resource usage? **Hint:** Think about how the data will need to be structured to efficiently query and place orders on a schedule.
- **Edge Cases**: Have you considered edge cases and potential error scenarios?
- **Documentation**: Have you provided clear and concise comments where necessary?

## Resources

- [Fast Api Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
- [Dyntastic Documentation](https://github.com/nayaverdier/dyntastic)
- [What is DynamoDb](https://medium.com/swlh/what-is-dynamodb-fbb3f6d14f18)

## Contact

If you have any questions or need clarification about the challenge, feel free to reach out to us at [alex@cryptofi.tech](mailto:alex@cryptofi.tech).

Good luck and we are excited to see what you come up with!

**CryptoFi**

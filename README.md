# Coding Challenge Readme

Welcome to the CryptoFi Backend Engineering coding challenge! This challenge is designed to assess your coding skills, problem-solving abilities, and "grit". Before you begin, please take a moment to read through this readme to understand the challenge requirements, instructions, and guidelines.

## Challenge Description

In this challenge, you will be asked to create a simple api that will allow a user to create (POST) a recurring crypto order, i.e. an order that gets executed at a specific time indefinitely. This coding challenge will require you to get famaliar with libraries such as FastApi, Pydantic, and Dyntastic as well as test your data structure skills in a no sql database (Dynamodb).

### Requirements
- A POST route that allows a user to input a recurring order. 
- A GET route to return a said user's recurring orders. 
  - For example - I pass in User `1`, I will receive all recurring orders for User `1`
- A recurring order can be for BTC or ETH only (validation check)
- A recurring order frequency can be Daily or Bi-Monthly only (validation check)
- A recurring order must have an associated USD amount with it greater than 0.
- A recurring order must be associated with a user
- A user can only ever have 1 recurring order for a given cryto/frequency pair
  - For example: a User can only have 1 recurring trade with a `Daily` frequency and for crypto `BTC`. If a second recurring order were to be placed for  `Daily`/`BTC` a validation error is expected to be raised

**Optional**
- Write a test suite in the `/test` folder for the POST/GET routes, database models, and their associated requirements.

## Getting Started

Follow these steps to get started with the challenge:

1. **Fork**: Start by forking this repository to your own GitHub account.
2. **Clone**: Clone the forked repository to your local machine using the following command:
3. **Setup**: [Provide any setup instructions required for the challenge. For example, installing dependencies, setting up a virtual environment, or configuring any tools.]

## Instructions

[Provide detailed instructions on how participants should approach the challenge. Break down the tasks or requirements clearly, so participants know what is expected of them.]

## Submission Guidelines

To submit your solution, follow these steps:

1. **Commit Changes**: Make sure to commit your code changes locally.
2. **Push to GitHub**: Push your committed changes to your forked repository on GitHub.
3. **Pull Request**: Create a pull request from your forked repository to the original challenge repository.

In your pull request, include the following:

- A brief description of the approach you took to solve the challenge.
- Any relevant notes, assumptions, or trade-offs you made during the development process.

## Evaluation Criteria

Your solution will be evaluated based on the following criteria:

- **Functionality**: Does your code solve the problem as described in the challenge?
- **Code Quality**: Is your code well-organized, readable, and maintainable?
- **Efficiency**: Is your solution optimized for performance and resource usage?
- **Edge Cases**: Have you considered edge cases and potential error scenarios?
- **Documentation**: Have you provided clear and concise comments where necessary?

## Resources

[List any resources or references that participants might find helpful while working on the challenge.]

## Contact

If you have any questions or need clarification about the challenge, feel free to reach out to us at [your-email@example.com](mailto:your-email@example.com).

Happy coding!

**[Your Name]**
**[Your Organization]**
**[Date]**

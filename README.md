# Superheroes Code Challenge

Welcome to the Superheroes Code Challenge! This application allows you to manage information about superheroes, their powers, and the relationships between them.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)  
- [Installation](#installation)
- [Database Models](#database-models)
- [Validations](#validations)
- [Routes](#routes)
- [Update (PATCH)](#update-patch)
- [Creating (POST)](#creating-post)  

## Getting Started

Follow these instructions to set up and run the Superheroes Code Challenge on your local machine.

### Prerequisites

Make sure you have the following prerequisites installed:

- Python (3.6 or higher)
- Pipenv (for managing Python dependencies)

### Installation  

1. Clone the repository:

    ```bash
    git clone https://github.com/<your-repo-url> 
    ```

2. Navigate to the project directory:

    ```bash
    cd superheroes-code-challenge
    ```

3. Install dependencies using Pipenv:

    ```bash  
    pipenv install
    ```

4. Activate the virtual environment:

    ```bash
    pipenv shell
    ```

## Database Models

The database contains three models - Hero, Power, and HeroPower with the following relationships:

- A Hero can have many HeroPowers
- A Power can have many HeroPowers 
- A HeroPower belongs to a Hero and Power in a many-to-many relationship

## Validations

Validations were added on the models:

- HeroPower
  - Validates strength is present and one of "Strong", "Weak", or "Average" 
- Power
  - Validates name is present and unique
  - Validates description is present and between 10-100 characters
  


## Update (PATCH)

Implemented a route to update a power: 

- PATCH /powers/:id - Updates power description and returns the updated power object

## Creating (POST) 

Implemented a route to create a hero-power association:

- POST /hero_powers - Creates a new HeroPower, validates data, and returns the created object
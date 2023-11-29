
# Advanced REST API with Authentication

## Overview
Building on the REST API from the previous project, this version introduces a robust authentication and authorization system. It uses JWT tokens to ensure that all contact operations are performed by registered and authenticated users, with users having access only to their own contacts.

## Features
- **User Authentication**:
  - Secure registration and login process.
  - Password hashing for enhanced security.
- **JWT Token-Based Authorization**:
  - Access and refresh tokens for secure API access.
  - Users can only access and modify their own contacts.
- **Error Handling**:
  - HTTP 409 Conflict for existing user registration attempts.
  - HTTP 401 Unauthorized for invalid login attempts.

## Technical Details
- **Authentication System**:
  - User credentials are securely stored with hashed passwords.
- **JWT Tokens**:
  - Generation and validation of JWT tokens for API access.
- **User-Specific Access**:
  - Users have access only to their contact operations.

## Usage
- **Registration**:
  - Users can register with an email and password.
  - The API returns HTTP 201 Created on successful registration.
- **Login**:
  - Upon successful login, users receive JWT access and refresh tokens.
- **Contact Operations**:
  - All contact operations require a valid JWT access token.
  - Endpoints include CRUD operations for contacts.

## Installation and Dependencies
- Clone the repository.
- Requires Python, FastAPI, SQLAlchemy, PostgreSQL, Pydantic, and a JWT library.
- Ensure proper setup of the PostgreSQL database and configure JWT token settings.
 

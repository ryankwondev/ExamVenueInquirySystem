# Exam Venue Inquiry System

The Exam Venue Inquiry System is a web application that helps students to check their exam schedules and exam rooms with ease. It supports two methods of inquiry: using a personal code or using an intranet account.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Database Schema](#database-schema)
- [License](#license)

## Features

- Simple web interface for easy access
- Search by personal code or intranet account
- Displays exam schedules and exam rooms
- Responsive design with Tailwind CSS

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/ExamVenueInquirySystem.git
```

2. Install the required packages:

```
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory of the project and configure the required environment variables. Check the provided example below.

4. Run the application:

```
uvicorn main:app --reload
```

## Usage

Open your browser and navigate to `http://localhost:8000` to access the Exam Venue Inquiry System. Choose one of the two methods (personal code or intranet account) to search for your exam schedule and exam rooms.

## Environment Variables

Create a `.env` file in the root directory of the project and configure the following variables:

```
DB_HOST=your_database_host
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DEV_MODE=True_or_False
DEMO_KEY=your_demo_key
```

Replace the placeholders with your actual values.

## Database Schema

The application supports PostgreSQL only. Use the following schema to create the required table:

```
create table public.examroom
(
code text,
subject text,
date text,
period text,
room text
);
```

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as you wish.

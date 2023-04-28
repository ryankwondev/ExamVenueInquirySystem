# Exam Venue Inquiry System

The Exam Venue Inquiry System is a web application that helps students to check their exam schedules and exam rooms with ease. It supports two methods of inquiry: using a personal code or using an intranet account.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Database Schema](#database-schema)
- [Deploy](#deploy)
- [License](#license)

## Features

- Simple web interface for easy access
- Search by personal code or intranet account
- Displays exam schedules and exam rooms
- Responsive design with Tailwind CSS

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ryankwondev/ExamVenueInquirySystem.git
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory of the project and configure the required environment variables. Check the provided example below.

4. Run the application:

```bash
uvicorn main:app --reload
```

## Usage

Open your browser and navigate to `http://localhost:8000` to access the Exam Venue Inquiry System. Choose one of the two methods (personal code or intranet account) to search for your exam schedule and exam rooms.

## Environment Variables

Create a `.env` file in the root directory of the project and configure the following variables:

```env
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

```sql
create table public.examroom (
  code text,
  subject text,
  date text,
  period text,
  room text
);
```

## Deploy

### Prerequisites

- A domain (e.g. example.com) pointing to your server
- Caddy server installed on your server (https://caddyserver.com/docs/install)

### Instructions

1. SSH into your server.

2. Install Caddy server following the instructions from the [official documentation](https://caddyserver.com/docs/install).

3. Create a Caddyfile with the reverse proxy configuration. Replace `example.com` with your domain, and `:8080` with the port your FastAPI application is running on.

```
example.com {
  reverse_proxy * :8080
} 
```

4. Save the Caddyfile in a directory of your choice (e.g. `/etc/caddy/Caddyfile`).

5. Start the Caddy server with the following command (assuming you saved the Caddyfile in `/etc/caddy/Caddyfile`):

```
sudo caddy start --config /etc/caddy/Caddyfile
```

6. Your FastAPI application should now be accessible through your domain (e.g. `https://example.com`).

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as you wish.

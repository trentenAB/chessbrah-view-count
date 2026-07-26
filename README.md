# chessbrah-view-count

### A simple web-app to practice full stack development

1. API Integration

- Making external API calls from Python to retrieve data
- Handling API keys securely (environment variables, not hardcoding)
- Parsing and processing API responses

2. Backend Web Development (Flask)

- Building a Python web server with Flask
- Routing (@app.route)
- Server-side rendering with Jinja2 templating ({{ }}, {% for %}, {% if %})
- Passing data from Python routes into HTML templates
- Serving static assets (CSS, images) via Flask's static file handling

3. Frontend Basics (HTML/CSS)

- HTML structure (<head>, <body>, metadata)
- Linking external stylesheets
- CSS styling (centering, border-radius, layout)
- Debugging rendering issues (paths, caching, selectors)

4. Database Management (PostgreSQL)

- Designing a schema (tables, columns, types, primary keys)
- Writing SQL (CREATE TABLE, INSERT, SELECT, ORDER BY, LIMIT)
- Connecting to Postgres from Python (psycopg2)
- Using psql — the CLI tool for direct database interaction
- Understanding the ORM concept (object-relational mapping) as an alternative to raw SQL
- Managed database hosting (Render Postgres) vs. self-hosted

5. Containerization (Docker)

- Writing a Dockerfile (base images, layers, caching strategy, WORKDIR, COPY, RUN, CMD)
- Building and running containers (docker build, docker run)
- Managing images (listing, removing, tagging)
- Multi-service orchestration with docker-compose.yml
- Passing secrets/config into containers safely (.env files, --env-file, env_file:)

6. Automation (Cron Jobs)

- Scheduling a script to run periodically (e.g., every hour/day) to pull fresh data automatically
- Decoupling data collection (the cron script) from data serving (the Flask app) — a classic pattern in real systems

7. Environment & Configuration Management

- Separating config/secrets from code (.env files, environment variables)
- Managing different environments (local vs. containerized vs. Render production)
.gitignore / .dockerignore hygiene to avoid leaking secrets or bloating images

8. Deployment / DevOps

- Deploying a containerized app to a cloud platform (Render)
- Understanding free-tier tradeoffs (spin-down, cold starts)
- Connecting a deployed app to a managed database (internal vs. external connection strings, SSL requirements)
- Git-based deployment workflows (push to GitHub → auto-deploy)
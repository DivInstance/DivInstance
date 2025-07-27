# GitHub Profile README Generator

## Overview

This repository contains a Python script that generates dynamic content for a GitHub profile README. The system uses GitHub's GraphQL API to fetch user statistics and generates an SVG-based profile display that adapts to light and dark themes.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Architecture
- **Language**: Python 3.x
- **API Integration**: GitHub GraphQL v4 API
- **Output Format**: SVG generation for GitHub profile display
- **Theme Support**: Dual-mode SVG files (light_mode.svg and dark_mode.svg)
- **Deployment**: GitHub Actions workflow for automated updates

### Design Philosophy
The application follows a simple, functional approach with minimal dependencies. It's designed to run as a scheduled job that updates profile statistics automatically.

## Key Components

### 1. Profile Statistics Calculator (`today.py`)
- **Purpose**: Calculates and formats personal statistics
- **Key Functions**:
  - `daily_readme()`: Calculates time elapsed since a birthday
  - `format_plural()`: Handles grammatically correct pluralization
  - `simple_request()`: Manages GitHub API requests with error handling
  - `graph_commits()`: Retrieves commit statistics via GraphQL

### 2. GitHub API Integration
- **Authentication**: Personal Access Token via environment variables
- **Rate Limiting**: Query count tracking to monitor API usage
- **Error Handling**: Comprehensive error checking for API responses

### 3. SVG Profile Display
- **Dual Theme Support**: Separate SVG files for light and dark modes
- **Responsive Design**: Uses GitHub's `prefers-color-scheme` media query
- **Dynamic Content**: Profile statistics updated automatically

## Data Flow

1. **Environment Setup**: Reads GitHub credentials from environment variables
2. **API Queries**: Fetches user data using GitHub GraphQL API
3. **Data Processing**: Calculates statistics and formats display strings
4. **SVG Generation**: Updates SVG files with current statistics
5. **GitHub Display**: README.md references SVG files for dynamic display

## External Dependencies

### Python Packages
- `datetime` and `dateutil`: Date/time calculations
- `requests`: HTTP client for GitHub API
- `lxml`: XML/HTML parsing (likely for SVG manipulation)
- `hashlib`: Cryptographic hashing (for data verification/caching)

### GitHub Services
- **GitHub GraphQL API v4**: Primary data source
- **GitHub Actions**: Automated execution environment
- **GitHub Pages/Raw Content**: SVG file hosting

### Environment Variables
- `ACCESS_TOKEN`: GitHub Personal Access Token
- `USER_NAME`: GitHub username (defaults to 'divyaranjan')

## Deployment Strategy

### Automation Approach
- **Scheduled Execution**: Likely runs on GitHub Actions cron schedule
- **Serverless**: No persistent infrastructure required
- **Self-Updating**: Commits changes back to repository automatically

### Security Considerations
- Token-based authentication with minimal required permissions
- Environment variable management for sensitive data
- Query rate limiting to prevent API abuse

### Scalability
- Lightweight Python script with minimal resource requirements
- Stateless execution model
- Efficient API usage with query counting

## Development Notes

### Code Structure
The codebase follows a functional programming style with clear separation of concerns. Each function has a single responsibility, making the code maintainable and testable.

### API Usage Optimization
The system implements query counting to monitor GitHub API usage, which is crucial for staying within rate limits and avoiding service interruptions.

### Error Handling
Robust error handling ensures the system continues to function even when API responses fail or return unexpected data.

## Recent Changes

### July 27, 2025 - Terminal-Style Profile README Created
- Created Andrew6rant-style terminal README with personalized information
- Updated SVG files with your specific details:
  - OS: Windows 10, Linux, Android 14  
  - Uptime: Calculated from November 11, 2003 birthday
  - Languages: Programming (C++, Java, Python, JavaScript), Speaking (English, Hindi, German)
  - Hobbies: Software (Cybersec Jailbreaking, Valorant Grinding), Hardware (Photography, Cooking, Basketball, Trekking)
  - Contact: divyaranjan20175@gmail.com, LinkedIn: divyaranjan~sahoo
- ASCII art profile picture area with terminal aesthetic
- GitHub Stats section prepared for future API integration
- Both light and dark mode SVG files created and working
- Python script successfully updates uptime automatically



















<h1 align="center">Hi there👋, I'm Divyaranjan Sahoo</h1>
<h3 align="center">A cybersecurity aficionado passionate about technology, hackathons, CTFs, IoT projects, and ethical hacking.</h3>

- 🔭 I’m currently working on [DevOps Metrics Reporter](https://github.com/DivInstance/DevOps-Metrics-Reporter)

- 🌱 I’m currently learning **Frameworks, course**

- 👯 I’m looking to collaborate on [PROJECT NAME](https://github.com/DivInstance/DevOps-Metrics-Reporter)

- 🤝 I’m looking for help with [PROJECT NAME](https://github.com/DivInstance/DevOps-Metrics-Reporter)

- 👨‍💻 All of my projects are available at [https://divyaranjansahoo.vercel.app/](https://divyaranjansahoo.vercel.app/)

- 💬 Ask me about **react, vue**

- 📫 How to reach me **divyaranjan20175@gmail.com**

- ⚡ Fun fact **People say I make funny tech jokes**

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/divyaranjan~sahoo" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="divyaranjan~sahoo" height="30" width="40" /></a>
<a href="https://stackoverflow.com/users/https://stackoverflow.com/users/31154691/divyaranjan-sahoo" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg" alt="https://stackoverflow.com/users/31154691/divyaranjan-sahoo" height="30" width="40" /></a>
<a href="https://instagram.com/diev.vied" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="diev.vied" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> <a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" alt="typescript" width="40" height="40"/> </a> </p>

<p><img align="left" src="https://github-readme-stats.vercel.app/api/top-langs?username=divinstance&show_icons=true&locale=en&layout=compact" alt="divinstance" /></p>

<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=divinstance&show_icons=true&locale=en" alt="divinstance" /></p>

<p><img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user=divinstance&" alt="divinstance" /></p>

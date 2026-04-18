# DevOps System Monitoring App 🚀

## Description
This is a simple Python-based system monitoring application containerized using Docker.

## Features
- Displays system uptime
- Shows disk usage (df -h)
- Shows memory usage

## Tech Stack
- Python
- Flask
- Docker

## How to Run

```bash
docker build -t myapp .
docker run -p 5000:5000 myapp

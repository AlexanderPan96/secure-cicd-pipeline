# 🚀 Secure CI/CD Pipeline with Automated Security Scanning

[![CI/CD Pipeline](https://github.com/alexanderpan96/secure-cicd-pipeline/actions/workflows/ci-cd-pipeline.yml/badge.svg)](https://github.com/alexanderpan96/secure-cicd-pipeline/actions)
[![Docker Image](https://img.shields.io/docker/v/alexanderpan96/secure-cicd-pipeline?label=docker)](https://hub.docker.com/r/alexanderpan96/secure-cicd-pipeline)
[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready CI/CD pipeline demonstrating DevSecOps best practices with automated testing, security scanning, containerization, and Azure deployment.

## Overview

This project showcases an enterprise-grade CI/CD pipeline that automatically:
- Runs unit tests with code coverage
- Performs static code analysis and linting
- Scans for security vulnerabilities (filesystem & container)
- Builds and pushes Docker images
- Deploys to Azure Container Instances
- Generates security reports

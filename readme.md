# Syslabo Organization Chart Application

## Overview

This application is designed to automatically generate an organizational chart based on user data, aligning with the structure outlined in the provided "組織図 (Organization Chart).xlsx". It also supports the maintenance of user and department information in a simple, accessible format, ensuring ease of use for individuals who may not have authored the application.

### Key Features

- **Automated Chart Generation**: Generates an organizational chart from data stored in relational databases.
- **User and Department Management**: Simple functionality to maintain records of "sys_users" and "cmn_department", with support for managing change history.
- **Concurrent Duty Management Proposal**: While the implementation is not required, the design proposal includes a structure to manage concurrent duties.

### Technical Highlights

1. **Relational Database**: The user and department data provided in the xlsx files are implemented using a relational database to ensure efficient storage and retrieval.
2. **Django Template Engine**: Used to render data dynamically on the frontend, maintaining a clean separation between backend logic and presentation.
3. **Optional Fields**: Certain fields were made optional to streamline the rendering process, especially where data was sparse or non-essential for the organizational chart.
4. **Dockerized Setup**: The application is containerized using Docker, making it easy to deploy and manage.

### Project Setup Instructions

#### Prerequisites

- Ensure that Docker and Docker Compose are installed on the host machine.
- Windows users: Please use **Git Bash** to run `.sh` files, as Windows does not natively support them.

#### Setup Steps

1. Clone the project repository.
2. Run the following command to build and start the application:

   ```bash
   docker-compose up --build
   ```

   This will initialize both the database and the web application.

### Technology Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, Bootstrap 4.6
- **Database**: PostgreSQL
- **Containerization**: Docker

### Future Enhancements

- **Modern Frontend**: Implementing a modern frontend framework (such as React or Vue.js) could enhance dynamic data rendering and improve the user interface.
- **NoSQL Integration**: For managing the asymmetric data structure of an organization hierarchy, switching to a NoSQL database like MongoDB could provide better optimization and scalability.

### Limitations

While the application fulfills the core requirements, there are areas for improvement, particularly on the frontend. Adding features like drag-and-drop UI functionality would greatly enhance the user experience. Additionally, exploring NoSQL solutions would better support complex hierarchical data.

Despite these limitations, the current implementation ensures that the primary functionality is in place, and the system is easy to extend and maintain.

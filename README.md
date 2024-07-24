<h1 style="font-size:2em;">🌟 Image Processing Application 🌟</h1>
<p>Unlock the full potential of your images with my cutting-edge application! Upload, store, and analyze your photos with advanced object detection capabilities.</p>

## 🚀 Key Features

**1. Seamless Image Storage**

- Effortlessly upload and securely store your images in the application.

**2. Advanced Object Detection**

- Analyze your photos with state-of-the-art detection algorithms to identify humans, cats, dogs, cars, and more.

**3. Real-Time Progress Tracking**

- Monitor the progress of your tasks with a visual progress bar and have the ability to stop a task at any time.

## ⚙️ Technologies 

**Frontend: React.js**

**Backend: Django**

**Database: PostgreSQL**

**Tools:**
- **Celery**: An asynchronous task queue/job queue for managing and executing background tasks.
- **Redis**: A fast, in-memory data structure store used as a message broker for Celery.

## ⚙️ Backend Architecture

I utilize a layered architecture in my backend, featuring two primary modules: Image Processing and Long Running Task. Each module is structured with its own:

- **ORM (Object Relational Mapper)**
- **Repository Class**
- **Service Class**
- **REST Controller (View)**

### Background Tasks

I have a system of REST APIs that allow users to:
- Submit tasks
- Get progress updates
- Stop a task

<img width="968" alt="Backend Architecture" src="https://github.com/user-attachments/assets/794875ac-ae3a-4c81-acfc-1bfe4a1542bb">

### API Endpoints

1. **Task Creation Endpoint**
   - Receives the task in the URL and an array of image IDs in the request body as JSON.
   
2. **Task Progress Endpoint**
   - Receives a task ID in the URL. This endpoint checks if the task exists in the database. If not, it returns a not found error code; otherwise, it returns the corresponding progress to the client.
   
3. **Delete Endpoint**
   - Receives a task ID in the URL. This endpoint checks if the task exists in the Redis server. If it does, it sends a revoke signal to stop the task; otherwise, it returns a not found error code.

## Demo

[![Watch the video](![image](https://github.com/user-attachments/assets/d02673a2-4d20-45d0-933c-001bf841f9cc)](https://www.youtube.com/watch?v=example)

# To-Do List Application

A modern, full-stack To-Do List application built with Python Flask backend and responsive frontend using Cascade-inspired styling with Tailwind CSS.

## Features

- ✅ Add new tasks with character limit
- 🗑️ Delete tasks with smooth animations
- 📱 Fully responsive design
- 🎨 Modern UI with slate and indigo color palette
- ⚡ Real-time task management
- 🕐 Task timestamps

## Technology Stack

### Backend
- **Python 3.7+**
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing

### Frontend
- **HTML5** - Semantic markup
- **Tailwind CSS** - Utility-first CSS framework
- **Vanilla JavaScript** - No framework dependencies
- **Cascade-inspired styling** - Clean, utility-based design

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | Retrieve all tasks |
| POST | `/api/tasks` | Create a new task |
| DELETE | `/api/tasks/<task_id>` | Delete a specific task |

## Installation & Setup

### 1. Clone or Download the Project
```bash
# If using git
git clone <repository-url>
cd To-Do

# Or download and extract the files
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

### 4. Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. **Adding Tasks**: Type your task in the input field and click "Add Task" or press Enter
2. **Deleting Tasks**: Hover over any task and click the delete icon (🗑️)
3. **Character Limit**: Tasks are limited to 100 characters for consistency
4. **Real-time Updates**: Task count updates automatically

## Project Structure

```
To-Do/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML template
└── README.md             # This file
```

## Styling Features

### Cascade-inspired Design Elements
- **Color Palette**: Slate (#334155) and Indigo (#4f46e5)
- **Responsive Utilities**: Mobile-first design with Tailwind
- **Modern Components**: Rounded corners, shadows, and smooth transitions
- **Hover States**: Interactive feedback on all clickable elements
- **Typography**: Clean, readable font hierarchy

### UI Components
- **Input Field**: Centered, with focus states and character counter
- **Add Button**: Prominent call-to-action with hover effects
- **Task List**: Vertical layout with hover-revealed delete buttons
- **Empty State**: Friendly message when no tasks exist
- **Footer**: Attribution and technology credits

## Development Notes

- Tasks are stored in memory (reset on server restart)
- In production, replace with a database (SQLite, PostgreSQL, etc.)
- The application uses Flask's development server
- CORS is enabled for potential future API separation
- All JavaScript is vanilla (no frameworks required)

## Potential Enhancements

- [ ] Database persistence
- [ ] Task completion toggle
- [ ] Task editing
- [ ] Task categories/tags
- [ ] Due dates
- [ ] User authentication
- [ ] Drag-and-drop reordering
- [ ] Export functionality

## License

This project is open source and available under the MIT License.

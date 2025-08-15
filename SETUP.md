# 🛠️ Development Environment Setup Guide

This guide will help you set up your development environment for Python certification preparation.

## 📋 Prerequisites

### Required Software
1. **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
2. **Git** - [Download Git](https://git-scm.com/downloads/)
3. **VS Code** - [Download VS Code](https://code.visualstudio.com/)

### Verify Installation
Open a terminal/command prompt and run:
```bash
python --version    # Should show Python 3.8+
git --version      # Should show Git version
code --version     # Should show VS Code version
```

## 🚀 Quick Setup

### 1. Clone Repository
```bash
git clone https://github.com/tanushrin/python-certification-prep.git
cd python-certification-prep
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Open in VS Code
```bash
code .
```

### 4. Install Recommended Extensions
When you open the project in VS Code, you'll be prompted to install recommended extensions. Click "Install All" or install them manually:

- **Python** (ms-python.python)
- **Pylance** (ms-python.vscode-pylance)
- **Jupyter** (ms-toolsai.jupyter)
- **Black Formatter** (ms-python.black-formatter)
- **Pylint** (ms-python.pylint)

## 📓 Jupyter Notebook Setup

### Start Jupyter Lab
```bash
jupyter lab
```

### Start Jupyter Notebook (Alternative)
```bash
jupyter notebook
```

### Using Notebooks in VS Code
1. Open any `.ipynb` file
2. Select Python kernel when prompted
3. Run cells with `Shift+Enter`

## 🧪 Testing Your Setup

### 1. Run Interactive Examples
```bash
python interactive_examples.py
```

### 2. Test VS Code Debugging
1. Open `interactive_examples.py`
2. Set a breakpoint (click left margin)
3. Press `F5` to start debugging
4. Select "Python: Current File"

### 3. Test Jupyter Integration
1. Open `notebooks/PCEP/01_getting_started.ipynb`
2. Run all cells to verify everything works

## 🔧 VS Code Configuration

The repository includes pre-configured settings:

### Settings (`.vscode/settings.json`)
- Python interpreter path
- Code formatting with Black
- Pylint linting
- Jupyter integration
- Auto-save and format on save

### Launch Configuration (`.vscode/launch.json`)
- Debug current Python file
- Debug tests with pytest
- Run interactive examples

### Recommended Extensions (`.vscode/extensions.json`)
- Python development tools
- Jupyter notebook support
- Markdown editing
- Git integration

## 🐛 Troubleshooting

### Python Not Found
**Problem**: `python` command not recognized

**Solutions**:
1. Add Python to your system PATH
2. Use `python3` instead of `python`
3. Use `py` on Windows

### Pip Install Fails
**Problem**: Permission errors or package conflicts

**Solutions**:
1. Use virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Use `--user` flag:
   ```bash
   pip install --user -r requirements.txt
   ```

### VS Code Python Extension Issues
**Problem**: Python extension not working properly

**Solutions**:
1. Reload VS Code window: `Ctrl+Shift+P` → "Developer: Reload Window"
2. Select correct Python interpreter: `Ctrl+Shift+P` → "Python: Select Interpreter"
3. Reinstall Python extension

### Jupyter Kernel Issues
**Problem**: Jupyter kernel not starting

**Solutions**:
1. Ensure Jupyter is installed: `pip install jupyter`
2. Restart kernel: In notebook, select "Kernel" → "Restart"
3. Select correct kernel: Click kernel name in top-right corner

## 💡 Tips for Effective Learning

### VS Code Tips
1. Use `Ctrl+Shift+P` to access command palette
2. Use `F5` for debugging, `F9` for breakpoints
3. Use `Ctrl+` ` (backtick) to open integrated terminal
4. Use `Ctrl+/` to comment/uncomment lines

### Jupyter Tips
1. Use `Shift+Enter` to run cells
2. Use `A` to add cell above, `B` for below
3. Use `M` to convert to markdown, `Y` for code
4. Use `DD` to delete cells

### Learning Workflow
1. Read markdown chapters in `Certs/` folder
2. Practice with interactive notebooks
3. Run and modify example code
4. Use debugger to understand code flow
5. Create your own examples

## 🎯 Next Steps

1. **Start Learning**: Open [PCEP Chapter 1](Certs/PCEP/Chapter01_Fundamental_Concepts.md)
2. **Practice**: Work through `notebooks/PCEP/01_getting_started.ipynb`
3. **Experiment**: Modify `interactive_examples.py`
4. **Test**: Run examples and practice debugging

Happy learning! 🐍✨
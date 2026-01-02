# Log Analysis Agent

An intelligent, fully local log analysis system for Windows application logs with anomaly detection, pattern recognition, and automated insights.

## Features

- **Offline Operation**: 100% local processing, no internet required
- **Multi-Interface**: Both CLI and GUI interfaces
- **Anomaly Detection**: ML-based anomaly detection using Isolation Forest
- **Pattern Recognition**: Time-series analysis and rule-based pattern matching
- **Automated Reporting**: Generates actionable insights and recommendations
- **Windows Native**: Optimized for Windows server application logs

## Target Use Cases

- Document conversion application monitoring
- File extraction process analysis
- Production automation tool monitoring
- Proactive failure prediction

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Add your log files** to `data/sample_logs/`

## Usage

### Quick Test
```bash
python main.py
```

### CLI Mode (coming soon)
```bash
python -m src.cli.cli_app --log-file data/sample_logs/app.log
```

### GUI Mode (coming soon)
```bash
python -m src.gui.gui_app
```

## Author

Shahan - Data Scientist & ML Engineer  
PixelForge | Conduent IT Production Control

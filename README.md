
# Python Document Analytics & Visualization Tool

A Python-based desktop application for analyzing document readership data, exploring visitor behavior, and visualizing document engagement patterns.

Built with **Python, Pandas, Matplotlib, Tkinter, and Graphviz**, the application processes JSON Lines datasets to generate insights into geographic readership, browser usage, reading activity, document popularity, and relationships between readers and documents.

The project combines data processing, statistical analysis, data visualization, and graph-based relationship analysis through a graphical user interface (GUI) and command-line interface (CLI).

## Features

### 1. Geographic Readership Analysis

Analyze the geographic distribution of document views.

- Filter readership data by document UUID.
- Count document views originating from different countries.
- Group country-level data into continents.
- Generate bar charts displaying geographic engagement.
- Identify regions with higher document readership.

The continent analysis uses a predefined country-to-continent mapping.

### 2. Browser Usage Analytics

Analyze the browsers visitors use to access documents.

- Extract browser information from user-agent strings.
- Identify browser names and versions.
- Generate detailed browser usage charts.
- Compare simplified browser categories.
- Display the most frequently used browsers.
- Group less frequently used browsers into an "Other" category.

Browser information is processed using `httpagentparser` and regular expressions.

### 3. Reader Activity Analysis

Identify highly engaged readers based on their reading activity.

- Filter document events by reading-time activity.
- Aggregate reading time for individual visitors.
- Calculate total reading time per visitor.
- Identify the top 10 readers.
- Display reading durations in minutes.

Reader identifiers are represented using visitor UUIDs.

### 4. Document Relationship Analysis

Explore relationships between documents based on shared readership.

- Find readers associated with a particular document.
- Retrieve documents read by a specified visitor.
- Identify documents visited by overlapping audiences.
- Generate ranked lists of related documents.
- Display the top 10 related documents.

This functionality provides a simple collaborative-filtering-style approach to discovering related content.

### 5. Graph-Based Relationship Visualization

Generate reader-document relationship graphs using the Graphviz DOT format.

- Create directed graphs connecting readers to documents.
- Represent readers and documents using different node shapes.
- Highlight selected readers and documents.
- Shorten UUID labels to their final four characters.
- Export graph definitions as `.dot` files.

Example command for rendering a generated graph:

```bash
dot -Tpng also_likes_graph.dot -o also_likes_graph.png
```

Graphviz must be installed separately to render the exported DOT file.

### 6. Additional Analytics

The application also includes several supplementary analytics features:

| Analysis | Description |
|----------|-------------|
| Device Analytics | Identifies the most frequently used visitor devices |
| Traffic Source Analysis | Displays the distribution of visitor traffic sources |
| Country Popularity | Identifies the most common visitor countries |
| Referrer Analysis | Displays the top 10 referring sources |
| Document Popularity | Identifies the top 10 most visited documents |

Results are presented using bar charts and histograms.

### 7. Graphical User Interface

A desktop interface built with Tkinter provides access to the analytics functionality.

Features include:

- JSON dataset selection using a file browser.
- Input fields for document and visitor UUIDs.
- Buttons for different analytics functions.
- Pop-up messages for errors and results.
- Matplotlib chart windows.
- Graphviz DOT file generation.

### 8. Command-Line Interface

The project also includes command-line functionality for accessing analysis operations without using the graphical interface.

The CLI implementation is contained in `Main.py`.

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core application development |
| Pandas | Data processing, filtering, and aggregation |
| Matplotlib | Statistical charts and visualizations |
| Tkinter | Desktop graphical user interface |
| httpagentparser | Browser and user-agent identification |
| Graphviz DOT | Reader-document graph representation |
| argparse | Command-line argument handling |
| JSON Lines | Input data format |

### File Descriptions

| File | Responsibility |
|------|----------------|
| `Main.py` | GUI, application initialization, user interaction, and CLI |
| `DataHandler.py` | JSON Lines loading and dataset filtering |
| `VisualizationHandler.py` | Matplotlib chart generation |
| `Task1.py` | Country and continent analysis |
| `Task2.py` | Browser usage analysis |
| `Task3.py` | Reader activity and reading-time analysis |
| `Task4.py` | Reader-document relationships and related document analysis |
| `Task5.py` | Graphviz DOT file generation |
| `TaskExtra1.py` | Device popularity |
| `TaskExtra2.py` | Visitor traffic sources |
| `TaskExtra3.py` | Country popularity |
| `TaskExtra4.py` | Referrer analysis |
| `TaskExtra5.py` | Most visited documents |

## Installation

### Prerequisites

Ensure Python 3 is installed on your system.

The application requires the following Python packages:

```text
pandas
matplotlib
httpagentparser
```

Tkinter is included with many Python installations, although it may need to be installed separately on Linux.

Graphviz is optional for generating images from exported DOT files.

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/python-document-analytics.git
cd python-document-analytics
```

### Step 2: Install Dependencies

```bash
pip install pandas matplotlib httpagentparser
```

Alternatively, create a `requirements.txt` file containing:

```text
pandas
matplotlib
httpagentparser
```

Then install using:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

Launch the graphical interface:

```bash
python Main.py
```

The application opens a Tkinter window containing the data-analysis tools.

## How to Use

### Loading a Dataset

1. Launch the application.
2. Click **Load JSON File**.
3. Select a supported JSON Lines dataset.
4. Wait for the file to load.
5. Use the available analysis features.

The input file must contain newline-delimited JSON records, with one JSON object per line.

### Example Dataset Format

```json
{"subject_doc_id":"doc-001","visitor_uuid":"visitor-001","visitor_country":"US","visitor_device":"desktop","visitor_source":"direct","visitor_referrer":"example.com","visitor_useragent":"Mozilla/5.0","event_type":"read","event_readtime":120}
{"subject_doc_id":"doc-002","visitor_uuid":"visitor-002","visitor_country":"GB","visitor_device":"mobile","visitor_source":"search","visitor_referrer":"example.org","visitor_useragent":"Mozilla/5.0","event_type":"pagereadtime","event_readtime":180}
```

These are illustrative records. The actual required fields depend on the analysis being performed.

### Geographic Analysis

1. Load a dataset.
2. Enter a document UUID.
3. Select **View by Country** or **View by Continent**.
4. Examine the generated chart.

### Browser Analysis

1. Load the dataset.
2. Select **Browser Analysis (Detailed)** to examine browser names and versions.
3. Select **View Browser (Simplified)** to compare broader browser categories.

### Reader Analysis

Select **View Top Readers** to calculate and display the top readers by total recorded reading time.

### Related Document Analysis

1. Enter a document UUID.
2. Optionally provide a visitor UUID.
3. Select an "Also Likes" analysis option.
4. View the related document results.

### Generate a Relationship Graph

1. Enter a document UUID.
2. Optionally enter a visitor UUID.
3. Select **Generate DOT File**.
4. Locate the generated `also_likes_graph.dot` file.

To convert the DOT file into a PNG image:

```bash
dot -Tpng also_likes_graph.dot -o graph.png
```

## Implementation Details

### Chunked JSON Data Loading

The application uses Pandas to load newline-delimited JSON data in chunks.

```python
for chunk in pd.read_json(
    file_path,
    lines=True,
    chunksize=100000
):
    chunks.append(chunk)

self.data = pd.concat(chunks, ignore_index=True)
self.data = self.data.convert_dtypes()
```

Chunked reading helps manage the loading process for larger files.

However, because the chunks are concatenated into a single DataFrame, the complete dataset must still fit in available memory.

### Reader Activity Aggregation

Reading-time records are filtered and grouped by visitor UUID.

```python
read_time_data = data[
    data["event_type"] == "pagereadtime"
]

total_reading_time = read_time_data.groupby(
    "visitor_uuid"
)["event_readtime"].sum()

top_readers = total_reading_time.nlargest(10)
```

This provides a ranked list of the most active readers by recorded reading time.

### Browser Identification

User-agent strings are processed with `httpagentparser`.

```python
import httpagentparser

parsed = httpagentparser.detect(user_agent)

browser_info = parsed.get("browser", {})

name = browser_info.get("name", "Other")
version = browser_info.get("version", "")
```

A simplified analysis is also available using regular expressions.

### Related Document Discovery

The related-document analysis uses shared readership.

The process involves:

1. Identifying readers of an input document.
2. Retrieving other documents associated with those readers.
3. Counting related document occurrences.
4. Ranking documents based on the selected analysis method.

This is a readership-overlap analysis rather than a content-based recommendation model.

### Data Visualization

Charts are generated using Matplotlib.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.bar(
    data.keys(),
    data.values(),
    color="skyblue"
)

plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

The visualization functions are centralized in `VisualizationHandler.py` to avoid repeating plotting logic across the analysis modules.


## Skills Demonstrated

This project demonstrates practical experience with:

- Python programming
- Object-oriented software design
- Data analytics and aggregation
- Pandas DataFrames
- Data visualization with Matplotlib
- JSON data processing
- GUI development with Tkinter
- Command-line interfaces
- Graph-based data representation
- Recommendation concepts
- Modular application architecture
- Handling and analyzing structured datasets

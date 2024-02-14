# Technical-Repo-Analyzer
This project is a full stack project which takes up a github profile link and return the most technical complex repository out of it.

Technical-Repo-Analyzer is a Python tool that helps identify the most technically complex repositories on GitHub. It analyzes repositories based on code complexity parameters, including the number of nesting levels, lines of code, and the number of new paths generated. This tool assists companies and developers in prioritizing repositories that may require more attention, potentially containing errors, or needing optimization.

Additionally, we have a Streamlit-hosted web interface for this tool, making it even more accessible.

## Features

- Full-stack application with code complexity analysis.
- Integration with OpenAI API, Github API, and Langchain.
- User-friendly Streamlit-hosted web interface.
- Automated error detection for efficient code review cycles.
- Prototype tool designed for developers, customizable for specific folders within a repository.
- Significantly reduces manual effort, saving over 20 hours per code review cycle.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/lonewolf235/Technical-Repo-Analyzer.git
Navigate to the project directory:

  ```bash
   cd technical-repo analyzer
```
Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```
# Streamlit Web Interface Usage
Access the Streamlit-hosted web interface by following this link: [Technical-Repo Analyzer on Streamlit](https://technicalcoder.streamlit.app/) (currently api key is removed).

Enter the GitHub username in the input field and click the "Analyze" button.

The tool will perform the analysis and display the results in a user-friendly web interface.

# Contributing
We welcome contributions to this project. If you would like to contribute, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and test them thoroughly.
Submit a pull request.
Please make sure to follow the Contributor Covenant Code of Conduct in all your interactions with the project.

# Contact
If you have any questions or suggestions regarding this project, please feel free to contact us at prakashvstomar@gmail.com

## Note : 1
The tool uses the OpenAI API key. If needed, it can be replaced by any open-source LLM model, provided maintenance of servers is available on a broader level.

## Note : 2
The output may seem less detailed, as this tool is intended as a prototype for developers. It facilitates error detection and can be customized to target specific folders in a repository.


Happy coding!






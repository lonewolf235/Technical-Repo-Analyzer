import os
import requests
import subprocess
import nbformat
import tempfile
import streamlit as st


## Function to return all repositories of a profile
def repoaccess(user):
    username = user.split("/")[-1]
    url = "https://api.github.com/users/{}/repos".format(username)
    response = requests.get(url)
    repo=[]
    if response.status_code == 200:
        repositories=response.json()
        for repository in repositories:
            repo.append(repository['html_url'])
        return repo
    else:
        print("Enter valid github username")

## function to extract code cells for jupyter notebook
def extract_code_cells(notebook_path):
    nb = nbformat.read(notebook_path, nbformat.NO_CONVERT)
    code_cells = []

    for cell in nb.cells:
        if cell.cell_type == 'code':
            source = cell.source.strip()
            code_cells.append(source)

    return code_cells

## function to format code cells
def format_code_cells(code_cells):
    formatted_code = []

    for code_cell in code_cells:
        formatted_code.append(f"{code_cell}")

    return '\n'.join(formatted_code)

## function to check if value is float or not
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

## function to delete unwanted files
def delete_files_except_extensions(directory, extensions):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            if file_extension not in extensions:
                os.remove(file_path) 
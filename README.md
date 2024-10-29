# GraphRAG-Practice

## Save the ouput in csv file
* This section explains how to save output text in a CSV file. The 'response_output.csv' file contains two columns: `Query` and `Response`. If the output includes unnecessary text, such as “SUCCESS: Local Search Response:”, it will be removed to keep the content clean. Moreover, since the output text may span multiple lines and contain extra spaces, we condense it into a single, clear sentence by removing redundant spaces.

1. **Local**
```Bash
echo "Query,Response" > response_output.csv
query="Among patients with septic shock and relative adrenal insufficiency, do corticosteroids reduce 28-day mortality?"
response=$(python -m graphrag.query --root . --method local "$query" | sed -n '/SUCCESS: Local Search Response:/,$p' | tr '\n' ' ' | sed 's/  */ /g' | sed 's/SUCCESS: Local Search Response: //')
echo "\"$query\",\"$response\"" >> response_output.csv
```

- echo "Query,Response" > response_output.csv adds a header to the CSV file.
- query="..." stores the query to be used in a variable.
- response=$(...) saves the response to the response variable. Here, sed and tr commands are used to replace line breaks with spaces and remove unnecessary text.
- echo "\"$query\",\"$response\"" >> response_output.csv appends both Query and Response to the response_output.csv file in CSV format.

2. **Global**
```Bash
echo "Query,Response" > response_output.csv
query="Among patients with septic shock and relative adrenal insufficiency, do corticosteroids reduce 28-day mortality?"
response=$(python -m graphrag.query --root . --method global "$query" | sed -n '/SUCCESS: Global Search Response:/,$p' | tr '\n' ' ' | sed 's/  */ /g' | sed 's/SUCCESS: Global Search Response: //')
echo "\"$query\",\"$response\"" >> response_output.csv
```

- echo "Query,Response" > response_output.csv adds a header to the CSV file.
- query="..." stores the query text in a variable.
- response=$(...) saves the response in the response variable:
    - `python -m graphrag.query --root . --method global "$query"` runs the global query.
	- sed -n '/SUCCESS: Global Search Response:/,$p' extracts the response starting from the line containing SUCCESS: Global Search Response:.
	- tr '\n' ' ' converts line breaks to spaces, consolidating the response into a single line.
	- sed 's/  */ /g' reduces multiple spaces to a single space for cleaner formatting.
	- sed 's/SUCCESS: Global Search Response: //' removes the introductory text from the response.
- echo "\"$query\",\"$response\"" >> response_output.csv appends both Query and Response to the CSV file in a clean format.

import React, { useState, useEffect } from "react";
import "./App.css";
import AceEditor from "react-ace";

import "ace-builds/src-noconflict/mode-json";
import "ace-builds/src-noconflict/mode-python";
import "ace-builds/src-noconflict/theme-monokai";

const apiUrl = "http://localhost:8000";
const invalidJsonMessage = "# invalid json";

type RequestBody = {
  data: string;
};

function App() {
  const [jsonObject, setJsonObject] = useState('{\n\t"foo": 5 \n}');
  const [pydanticModel, setPydanticModel] = useState("");

  useEffect(() => {
    translate();
  }, [jsonObject]);

  function onChange(newValue: string) {
    console.log(newValue);
    setJsonObject(newValue);
  }

  function translate() {
    const requestBody: RequestBody = { data: jsonObject };
    const url = new URL(apiUrl);
    const opts = {
      method: "POST",
      body: JSON.stringify(requestBody),
    };

    fetch(url.toString(), opts)
      .then((response) => {
        console.log(response.status);
        if (response.status === 422) {
          setPydanticModel(invalidJsonMessage);
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        setPydanticModel(data.model);
      });
  }

  return (
    <div className="App">
      <h1>Json to Pydantic Converter</h1>
      <div className="editor-container">
        <div className="editor">
          <h3>Json</h3>
          <AceEditor
            value={jsonObject}
            mode="json"
            theme="monokai"
            onChange={onChange}
            name="json-editor"
            editorProps={{ $blockScrolling: true }}
          />
        </div>
        <div className="editor">
          <h3>Pydantic</h3>
          <AceEditor
            value={pydanticModel}
            mode="python"
            theme="monokai"
            name="python-editor"
            editorProps={{ $blockScrolling: true }}
          />
        </div>
      </div>
    </div>
  );
}

export default App;

import React from 'react';
import logo from './logo.svg';
import './App.css';
import AceEditor from "react-ace";

import "ace-builds/src-noconflict/mode-json";
import "ace-builds/src-noconflict/theme-monokai";

function onChange(newValue: string) {
  console.log(newValue);
}

function App() {
  return (
    <div className="App">
        <AceEditor
          mode="json"
          theme="monokai"
          onChange={onChange}
          name="left-editor"
          editorProps={{ $blockScrolling: true }}
        />
    </div>
  );
}

export default App;

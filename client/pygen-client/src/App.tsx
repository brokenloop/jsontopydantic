import "./App.css";
import AceEditor from "react-ace";

import "ace-builds/src-noconflict/mode-json";
import "ace-builds/src-noconflict/theme-monokai";

const apiUrl = "http://localhost:8000";

type RequestBody = {
  data: string;
};

function onChange(newValue: string) {
  const requestBody: RequestBody = { data: newValue };
  console.log(newValue);
  const url = new URL(apiUrl);
  // url.search = new URLSearchParams(requestBody).toString();
  const blah = { data: { hello: 5 } };
  const s = JSON.stringify(blah);
  console.log(s);
  const opts = {
    method: "POST",
    body: s,
    // body: JSON.stringify(requestBody),
  };

  console.log(url.toString());
  console.log(opts);
  fetch(url.toString(), opts).then((x) => console.log(x));
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

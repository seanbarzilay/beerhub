import React from 'react'
import { render } from 'react-dom'
const {Surface} = require("gl-react-dom");
const {HelloGL} = require('./Example.jsx');

require('bootstrap/dist/css/bootstrap.css');

render(<Surface width={300} height={200}>
    <HelloGL />
</Surface>, document.getElementById('react-app'));

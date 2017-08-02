import * as React from "react";
import {Switch, Redirect, Route} from "react-router-dom";


const Home = () => (
  <div>
    <h2>Home</h2>
  </div>
);

const About = () => (
  <div>
    <h2>About</h2>
  </div>
);

function Routes() {
  return (
    <Switch>
        <Route exact path="/" component={Home}/>
        <Route path="/about" component={About}/>
        <Redirect from="*" to="/"/>
    </Switch>
  )
}

export default Routes;
